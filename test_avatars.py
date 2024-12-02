import requests
import allure
import pytest
from data import *
from schemas import user_schema
from jsonschema import validate

# pytest.skip(allow_module_level=True)

task_id = 'api-11'
@allure.title('put /users/{user_uuid}/avatar')
@allure.description('Verify avatar can be added to a user using valid images')
@allure.testcase('D-1')
@pytest.mark.parametrize("test_data, file_data", [(post_users_valid[0], item) for item in put_images_valid])
# @pytest.mark.skip()
def test_put_users_uuid_avatar_valid(test_data, file_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  files = {'avatar_file': open(fr'./images/{file_data['image']}', 'rb')}

  response = requests.put(f'{url}/users/{new_user['uuid']}/avatar', headers=headers, 
                                      files=files)
  header_data = response.headers
  assert header_data['content-type'] == 'application/json'
  assert int(header_data['content-length']) == len(response.content)
  assert response.status_code == 200

  data = response.json()
  
  assert 'https://gravatar.com/avatar/' in data['avatar_url']
  validate(instance=data, schema=user_schema)


task_id = 'api-11'
@allure.title('put /users/{user_uuid}/avatar')
@allure.description('Verify avatar will not be added to a user using invalid images')
@allure.testcase('D-2')
@pytest.mark.parametrize("test_data, file_data", [(post_users_valid[0], item) for item in put_images_invalid])
# @pytest.mark.skip()
def test_put_users_uuid_avatar_invalid(test_data, file_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  files = {'avatar_file': open(fr'./images/{file_data['image']}', 'rb')}

  response = requests.put(f'{url}/users/{new_user['uuid']}/avatar', headers=headers, 
                                      files=files)
  header_data = response.headers
  assert int(header_data['content-length']) == len(response.content)
  assert response.status_code == file_data['code']

  data = response.json()  

  if response.status_code == 431:
    assert file_data['error'] in data['errorMessage']
    assert header_data['content-type'] == 'application/json; charset=utf-8'
  elif response.status_code == 400:
    assert file_data['error'] in data['message']
    assert header_data['content-type'] == 'application/json'

  response = requests.get(f'{url}/users/{new_user['uuid']}', headers=headers)
  data = response.json()
  assert '' == data['avatar_url']
  validate(instance=data, schema=user_schema)