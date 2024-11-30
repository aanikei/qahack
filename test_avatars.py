import requests
import allure
import pytest
from data import *

# all files are taken from https://sample-videos.com

task_id = 'api-11'
@allure.title('put /users/{user_uuid}/avatar')
@allure.description('Verify avatar can be added to a user')
@allure.testcase('D-1')
@pytest.mark.parametrize("test_data, file_data", [(post_users_valid[0], item) for item in put_images])
# @pytest.mark.skip()
def test_put_users_uuid_avatar(test_data, file_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  files = {'avatar_file': open(fr'./images/{file_data['image']}', 'rb')}

  response = requests.put(f'{url}/users/{new_user['uuid']}/avatar', headers=headers, 
                                      files=files)
  data = response.json()

  assert response.status_code == file_data['code']

  if file_data['code'] == 200:
    assert 'https://' in data['avatar_url'] and 'avatar' in data['avatar_url']
  else:
    assert file_data['error'] in data['errorMessage']

    response = requests.get(f'{url}/users/{new_user['uuid']}', headers=headers)
    data = response.json()
    assert '' == data['avatar_url']