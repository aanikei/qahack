import requests
import allure
import pytest
import uuid
from data import *
from schemas import *
from jsonschema import validate

task_id = 'api-6'
@allure.title('get /users')
@allure.description('Verify results without any parameters')
@allure.testcase('A-1')
# @pytest.mark.skip()
def test_get_users_no_params(url):
  headers = auth_header | {'X-Task-Id': task_id}
  response = requests.get(f'{url}/users', headers=headers)
  data = response.json()

  assert response.status_code == 200
  assert 11 == data['meta']['total'] #equals 11 after setup

  #delete all records
  for _ in range(2):
    response = requests.get(f'{url}/users', headers=headers)
    data = response.json()

    for user in data['users']:
      requests.delete(f'{url}/users/{user['uuid']}', headers=headers)
      response = requests.get(f'{url}/users', headers=headers)

      data = response.json()
      if len(data['users']) <= 10:
        assert data['meta']['total'] == len(data['users'])

  #check no records left
  response = requests.get(f'{url}/users', headers=headers)
  data = response.json()

  assert response.status_code == 200
  assert [] == data['users']
  assert 0 == data['meta']['total']

  # create 20 records
  for index, user in enumerate(post_users_valid[0:20]):
    requests.post(f'{url}/users', headers=headers, json=user)
    response = requests.get(f'{url}/users', headers=headers)
    data = response.json()
    if len(data['users']) <= 9:
      assert data['meta']['total'] == len(data['users'])

    assert data['meta']['total'] == index + 1  


task_id = 'api-21'
@allure.title('get /users')
@allure.description('Verify results with parameters to check 20 available records')
@allure.testcase('A-2')
@pytest.mark.parametrize("test_data", get_users_all_parameters)
# @pytest.mark.skip()
def test_get_users_all_params_first_20(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  response = requests.get(f'{url}/users', headers=headers, params={ 'limit': 100})
  data = response.json()
  #get current number of records and create new users to reach 20 users
  all_users = data['users']

  response = requests.get(f'{url}/users', headers=headers, params=test_data)

  assert response.status_code == 200
  data = response.json()
  
  if 'offset' not in test_data:
    test_data['offset'] = 0
  elif 'limit' not in test_data:
    test_data['limit'] = 10

  end_range = test_data['offset'] + test_data['limit']
  if end_range > 19:
    end_range = 19

  assert all_users[test_data['offset']:end_range] == data['users']


task_id = 'api-22'
@allure.title('post /users')
@allure.description('Verify creation of a new user')
@allure.testcase('A-3')
@pytest.mark.parametrize("test_data", post_users_valid)
# @pytest.mark.skip()
def test_post_users(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  response = requests.post(f'{url}/users', headers=headers, json=test_data)

  assert response.status_code == 200
  data = response.json()
  
  uuid.UUID(data['uuid']) #check uuid validity
  assert data['avatar_url'] == ''
  assert test_data['email'] == data['email']
  assert test_data['name'] == data['name']
  assert test_data['nickname'] == data['nickname']\
  



task_id = 'api-23'
@allure.title('get /users/{user_uuid}')
@allure.description('Verify a user can be retrieved by uuid')
@allure.testcase('B-1')
@pytest.mark.parametrize("test_data", post_users_valid)
# @pytest.mark.skip()
def test_get_users_uuid(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  response = requests.get(f'{url}/users/{new_user['uuid']}', headers=headers)
  header_data = response.headers
  data = response.json()

  assert response.status_code == 200
  assert int(header_data['content-length']) == len(response.content)
  assert header_data['content-type'] == 'application/json'
  compare_users(new_user, data)
  validate(instance=data, schema=user_schema)

  # delete created user to clear db
  requests.delete(f'{url}/users/{data['uuid']}', headers=headers)


task_id = 'api-4'
@allure.title('patch /users/{user_uuid}')
@allure.description('Verify a name of a user can be modified')
@allure.testcase('B-2')
@pytest.mark.parametrize("test_data, patch", [(post_users_valid[0], item) for item in patch_users_valid])
# @pytest.mark.skip()
def test_patch_users_uuid_valid(test_data, patch, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  patch_key = next(iter(patch))
  patch_value = patch[patch_key]

  new_user[patch_key] = patch_value

  response = requests.patch(f'{url}/users/{new_user['uuid']}', 
                                      headers=headers, 
                                      json={ patch_key: patch_value })
  header_data = response.headers
  data = response.json()
  assert response.status_code == 200

  assert int(header_data['content-length']) == len(response.content)
  assert header_data['content-type'] == 'application/json'
  compare_users(new_user, data)
  validate(instance=data, schema=user_schema)

  password = test_data['password'] if patch_key != 'password' else patch_value
  #verify updated user can still log in
  response = requests.post(f'{url}/users/login', headers=headers, 
                                      json= {'email': data['email'], 'password': password})
  
  assert response.status_code == 200
  data = response.json()

  compare_users(new_user, data)


@allure.title('patch /users/{user_uuid}')
@allure.description('Verify a name of a user should not be modified with invalid data')
@allure.testcase('B-3')
@pytest.mark.parametrize("test_data, patch", [(post_users_valid[0], item) for item in patch_users_invalid])
# @pytest.mark.skip()
def test_patch_users_uuid_invalid(test_data, patch, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  patch_key = next(iter(patch))
  patch_value = patch[patch_key]

  response = requests.patch(f'{url}/users/{new_user['uuid']}', 
                                      headers=headers, 
                                      json={ patch_key: patch_value })
  header_data = response.headers
  data = response.json()
  assert response.status_code == 400

  assert int(header_data['content-length']) == len(response.content)
  assert header_data['content-type'] == 'application/json'

  #verify updated user was not modified
  response = requests.get(f'{url}/users/{new_user['uuid']}', headers=headers)
  
  assert response.status_code == 200
  data = response.json()

  compare_users(new_user, data)
  validate(instance=data, schema=user_schema)


task_id = 'api-24'
@allure.title('delete /users/{user_uuid}')
@allure.description('Verify a user can be deleted')
@allure.testcase('B-4')
@pytest.mark.parametrize("test_data", post_users_valid)
# @pytest.mark.skip()
def test_delete_users_uuid(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  response = requests.delete(f'{url}/users/{new_user['uuid']}', headers=headers)
  
  assert response.status_code == 204




task_id = 'api-7'
@allure.title('post /users/login')
@allure.description('Verify a user can log in')
@allure.testcase('C-1')
@pytest.mark.parametrize("test_data", post_users_valid)
# @pytest.mark.skip()
def test_post_users_login_valid(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  response = requests.post(f'{url}/users/login', headers=headers, 
                                      json= {'email': test_data['email'], 'password': test_data['password']})
  
  assert response.status_code == 200
  data = response.json()

  compare_users(new_user, data)


@allure.title('post /users/login')
@allure.description('Verify an invalid user cannot log in')
@allure.testcase('C-2')
@pytest.mark.parametrize("test_data, errors", [(post_users_valid[0], item) for item in post_users_login_invalid])
# @pytest.mark.skip()
def test_post_users_login_invalid(test_data, errors, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  create_user(url, headers, test_data)

  login = {}
  if 'email' in errors:
    login['email'] = errors['email']
  if 'password' in errors:
    login['password'] = errors['password']
  if login == {}:
    login = None

  response = requests.post(f'{url}/users/login', headers=headers, json=login)
  
  assert response.status_code == errors['code']
  data = response.json()
  assert data['code'] == errors['code']
  assert errors['message'] == data['message']
  

def compare_users(new_user, data):
  assert new_user['uuid'] == data['uuid']
  assert new_user['avatar_url'] == data['avatar_url']
  assert new_user['email'] == data['email']
  assert new_user['name'] == data['name']
  assert new_user['nickname'] == data['nickname']