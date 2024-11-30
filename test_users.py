import requests
import allure
import pytest
import os
import time
import uuid
from pprint import pprint

email = os.getenv('EMAIL')
auth_header = { 'Authorization': f'Bearer qahack2024:{email}' }

task_id = 'api-6'
@allure.title('get /users')
@allure.description('Verify results without any parameters')
@allure.testcase('Users-1')
# @pytest.mark.skip()
def test_get_users_no_params(url):
  headers = auth_header | {'X-Task-Id': task_id}
  response = requests.get(f'{url}/users', headers=headers)

  assert response.status_code == 200
  data = response.json()
  # pprint(data)
  assert 10 == len(data['users'])



get_users_all_parameters= [ 
  {'offset': 0, 'limit': 2},
  {'offset': 0, 'limit': 10},
  {'offset': 1, 'limit': 5},
  {'offset': 1, 'limit': 9},
  {'offset': 8, 'limit': 2},
  {'offset': 9, 'limit': 1},
  {'limit': 1},
  {'limit': 2},
  {'limit': 10},
  {'offset': 0}
]
@allure.title('get /users')
@allure.description('Verify results with parameters to check first 10 records ')
@allure.testcase('Users-2')
@pytest.mark.parametrize("test_data", get_users_all_parameters)
# @pytest.mark.skip()
def test_get_users_all_params_first_ten(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  response = requests.get(f'{url}/users', headers=headers)
  data = response.json()
  all_users = data['users']
  # pprint(all_users)

  response = requests.get(f'{url}/users', headers=headers, params=test_data)

  assert response.status_code == 200
  data = response.json()
  # pprint(data)
  if 'offset' not in test_data:
    test_data['offset'] = 0
  elif 'limit' not in test_data:
    test_data['limit'] = 10

  assert all_users[test_data['offset']:test_data['offset'] + test_data['limit']] == data['users']
  time.sleep(2)



get_users_limit = [
  {'limit': 11},
  {'limit': 50},
  {'limit': 99},
  {'limit': 100},
]
# task_id = 'api-21'
@allure.title('get /users')
@allure.description('Verify results with limit more than 10')
@pytest.mark.parametrize("test_data", get_users_limit)
@allure.testcase('Users-3')
# @pytest.mark.skip()
def test_get_users_limit(url, test_data):
  headers = auth_header | {'X-Task-Id': task_id}
  response = requests.get(f'{url}/users', headers=headers, params={'offset': 0, 'limit': 100})

  assert response.status_code == 200
  data = response.json()
  # pprint(data)
  assert data['meta']['total'] == len(data['users'])
  time.sleep(2)


post_users_valid = [
  {'email': 'aatest0@testt.commx', 'password': 'password', 'name': 'aatest1', 'nickname': 'aatest1'},
  {'email': 'aatest1@testt.commx', 'password': 'pass word', 'name': 'aatest1', 'nickname': 'aatest1'},
  {'email': 'aatest2@testt.commx', 'password': '!@#$%^&*()1234567890', 'name': 'aatest2', 'nickname': 'aatest2'},
  {'email': 'aatest3@testt.commx', 'password': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`=-[]{}};\':",./<>?  \\|аб', 'name': 'aatest3', 'nickname': 'aatest3'},
  {'email': 'aatest4@testt.commx', 'password': 'password', 'name': 'aatest4', 'nickname': 'aa'},
  {'email': 'aatest5@testt.commx', 'password': 'password', 'name': 'aatest5', 'nickname': '_.+-'},
  {'email': 'aatest6@testt.commx', 'password': 'password', 'name': 'aatest6', 'nickname': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.+-ABCDEFGHIJKLMNOPQRSTUVWX'},
  # {'email': 'aatest7@testt.commx', 'password': 'password', 'name': 'A', 'nickname': 'aatest7'},
  {'email': 'aatest8@testt.commx', 'password': 'password', 'name': 'Ab', 'nickname': 'aatest8'},
  {'email': 'aatest9@testt.commx', 'password': 'password', 'name': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`=-[]{}};\':",./<>?  \\|аб', 'nickname': 'aatest9'},
  {'email': 'aatest10@testt.commx', 'password': 'password', 'name': 'aatest10', 'nickname': 'aatest10'},
  {'email': 'aate.st1@testt.comx', 'password': 'password', 'name': 'aatest11', 'nickname': 'aatest11'},
  {'email': 'aate_st2@testt.orgx', 'password': 'password', 'name': 'aatest12', 'nickname': 'aatest12'},
  {'email': 'aate-st3@testt.netx', 'password': 'password', 'name': 'aatest13', 'nickname': 'aatest13'},
  {'email': 'aate+st4@testt.c', 'password': 'password', 'name': 'aatest14', 'nickname': 'aatest14'},
  {'email': 'aate+st5@testt.co.uk', 'password': 'password', 'name': 'aatest15', 'nickname': 'aatest15'}
]
task_id = 'api-22'
@allure.title('post /users')
@allure.description('Verify creation of new user')
@allure.testcase('Users-4')
@pytest.mark.parametrize("test_data", post_users_valid)
# @pytest.mark.skip()
def test_post_users(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  response = requests.post(f'{url}/users', headers=headers, json=test_data)

  assert response.status_code == 200
  data = response.json()
  # pprint(data)
  uuid.UUID(data['uuid']) #check uuid validity
  assert data['avatar_url'] == ''
  assert test_data['email'] == data['email']
  assert test_data['name'] == data['name']
  assert test_data['nickname'] == data['nickname']

  requests.delete(f'{url}/users/{data['uuid']}', headers=headers)
  time.sleep(2)
  

