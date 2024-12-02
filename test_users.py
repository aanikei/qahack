import requests
import allure
import pytest
import uuid
from data import *
from schemas import user_schema
from utils import *
from jsonschema import validate

# pytest.skip(allow_module_level=True)

task_ids = ['api-6', 'api-21']
@allure.title('get /users')
@allure.description('Verify results without any parameters')
@allure.testcase('A-1')
@pytest.mark.parametrize("task", task_ids)
# @pytest.mark.skip()
def test_get_users_no_params(task,url):
  headers = auth_header | {'X-Task-Id': task}
  delete_users(url, headers=headers)

  #check no records left
  response = requests.get(f'{url}/users', headers=headers)
  data = response.json()

  assert response.status_code == 200
  assert [] == data['users']
  assert 0 == data['meta']['total']

  # create 20 records and verify they are added
  for index, user in enumerate(post_users_valid[0:20]):
    response = requests.post(f'{url}/users', headers=headers, json=user)
    data = response.json()
    assert response.status_code == 200

    response = requests.get(f'{url}/users', headers=headers)
    header_data = response.headers
    assert header_data['content-type'] == 'application/json'
    
    data = response.json()
    if len(data['users']) <= 9:
      assert data['meta']['total'] == len(data['users'])

    assert data['meta']['total'] == index + 1  


task_ids = ['api-6', 'api-21']
test_params = [(param, task) for param in get_users_all_parameters for task in task_ids]
@allure.title('get /users')
@allure.description('Verify results with parameters to check 20 available records')
@allure.testcase('A-2')
@pytest.mark.usefixtures("create_twenty_users")
@pytest.mark.parametrize("test_data, task", test_params)
# @pytest.mark.skip()
def test_get_users_all_params_first_20(test_data, task, url):
  headers = auth_header | {'X-Task-Id': task}

  #get current number of records
  response = requests.get(f'{url}/users', headers=headers, params={ 'limit': 100})
  data = response.json()
  all_users = data['users']

  #get parameterized records
  response = requests.get(f'{url}/users', headers=headers, params=test_data)

  assert response.status_code == 200
  data = response.json()
  
  start, end = param_testing(test_data, 19)

  assert all_users[start:end] == data['users']


task_ids = ['api-6', 'api-21']
test_params = [(user, task) for user in post_users_valid for task in task_ids]
@allure.title('post /users')
@allure.description('Verify creation of a new user')
@allure.testcase('A-3')
@pytest.mark.parametrize("test_data, task", test_params)
# @pytest.mark.skip()
def test_post_users(test_data, task, url):
  headers = auth_header | {'X-Task-Id': task}
  delete_users(url, headers)

  response = requests.post(f'{url}/users', headers=headers, json=test_data)
  header_data = response.headers
  assert header_data['content-type'] == 'application/json'
  assert response.status_code == 200
  assert int(header_data['content-length']) == len(response.content)
  data = response.json()
  
  uuid.UUID(data['uuid']) #check uuid validity
  assert data['avatar_url'] == ''
  assert test_data['email'] == data['email']
  assert test_data['name'] == data['name']
  assert test_data['nickname'] == data['nickname']
  validate(instance=data, schema=user_schema)




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
  assert response.status_code == 200
  assert int(header_data['content-length']) == len(response.content)
  assert header_data['content-type'] == 'application/json'

  data = response.json()

  compare_users(new_user, data)
  validate(instance=data, schema=user_schema)


task_ids = ['api-4', 'api-24']
test_params = [(post_users_valid[0], item) for item in patch_users_valid]
test_params_with_task_ids = [val + (task, ) for val in test_params for task in task_ids]
@allure.title('patch /users/{user_uuid}')
@allure.description('Verify a name of a user can be modified')
@allure.testcase('B-2')
@pytest.mark.parametrize("test_data, patch, task", test_params_with_task_ids)
# @pytest.mark.skip()
def test_patch_users_uuid_valid(test_data, patch, task, url):
  headers = auth_header | {'X-Task-Id': task}
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

  # get user again and verify that it's updated
  response = requests.get(f'{url}/users/{new_user['uuid']}', headers=headers)
  data = response.json()
  assert response.status_code == 200
  compare_users(new_user, data)
  
  # verify updated user can still log in
  response = requests.post(f'{url}/users/login', headers=headers, 
                                      json= {'email': data['email'], 'password': password})
  assert response.status_code == 200
  data = response.json()

  compare_users(new_user, data)


task_ids = ['api-4', 'api-24']
test_params = [(post_users_valid[0], item) for item in patch_users_invalid]
test_params_with_task_ids = [val + (task, ) for val in test_params for task in task_ids]
@allure.title('patch /users/{user_uuid}')
@allure.description('Verify a name of a user should not be modified with invalid data')
@allure.testcase('B-3')
@pytest.mark.parametrize("test_data, patch, task", test_params_with_task_ids)
# @pytest.mark.skip()
def test_patch_users_uuid_invalid(test_data, patch, task, url):
  headers = auth_header | {'X-Task-Id': task}
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

  # verify updated user was not modified
  response = requests.get(f'{url}/users/{new_user['uuid']}', headers=headers)
  
  assert response.status_code == 200
  data = response.json()

  compare_users(new_user, data)
  validate(instance=data, schema=user_schema)

  # verify user can still log in
  response = requests.post(f'{url}/users/login', headers=headers, 
                                      json= {'email': data['email'], 'password': test_data['password']})
  assert response.status_code == 200
  data = response.json()
  compare_users(new_user, data)


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

  invalid_auth = headers.copy()
  invalid_auth['Authorization'] = invalid_auth['Authorization'][:-10]
  response = requests.delete(f'{url}/users/{new_user['uuid']}', headers=invalid_auth)
  header_data = response.headers
  assert response.status_code == 404
  assert int(header_data['content-length']) == len(response.content)
  assert header_data['content-type'] == 'application/json'

  response = requests.delete(f'{url}/users/{new_user['uuid']}', headers=headers)
  assert response.status_code == 204

  # verify deleted user is actually deleted
  response = requests.get(f'{url}/users/{new_user['uuid']}', headers=headers)
  assert response.status_code == 404

  # verify deleted user cannot log in
  response = requests.post(f'{url}/users/login', headers=headers, 
                                      json= {'email': test_data['email'], 'password': test_data['password']})
  assert response.status_code == 404




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


task_id = 'api-7'
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