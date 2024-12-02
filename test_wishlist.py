import requests
import allure
import pytest
from data import *
from schemas import whishlist_schema
from jsonschema import validate

# pytest.skip(allow_module_level=True)

task_ids = ['api-5', 'api-25']
@allure.title('post /users/{user_uuid}/wishlist/add with valid data')
@allure.description('Verify valid items can be added to and removed from wishlist')
@allure.testcase('E-1')
@pytest.mark.parametrize("test_data, task", [(post_users_valid[0], task) for task in task_ids])
# @pytest.mark.skip()
def test_users_uuid_wishlist_add_valid(test_data, task, url):
  headers = auth_header | {'X-Task-Id': task}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  # get existing games' uuids
  game_data = get_all_games(url, headers)
  game_uuids = [i['uuid'] for i in game_data['games']]

  # add them to a user
  for index, game_uuid in enumerate(game_uuids, start=1):
    response = requests.post(f'{url}/users/{new_user['uuid']}/wishlist/add', 
                                      headers=headers, json={ 'item_uuid': game_uuid })
    assert response.status_code == 200
    header_data = response.headers
    assert header_data['content-type'] == 'application/json'

    data = response.json()
    validate(instance=data, schema=whishlist_schema)

    # verify games are added to a user
    response = requests.get(f'{url}/users/{new_user['uuid']}/wishlist', headers=headers)
    assert response.status_code == 200
    
    data = response.json()
    assert len(data['items']) == index
    assert game_uuid in [i['uuid'] for i in data['items']]
  
  # verify list of existing games is now identical to a user's wishlist
  response = requests.get(f'{url}/users/{new_user['uuid']}/wishlist', headers=headers)
  assert response.status_code == 200

  user_games = response.json()
  assert sorted(game_data['games'], key=lambda x: x['uuid']) == sorted(user_games['items'], key=lambda x: x['uuid'])


task_id = 'api-8'
@allure.title('post /users/{user_uuid}/wishlist/remove with valid data')
@allure.description('Verify valid items can be removed from wishlist')
@allure.testcase('E-1')
@pytest.mark.parametrize("test_data", [post_users_valid[0]])
# @pytest.mark.skip()
def test_users_uuid_wishlist_remove_valid(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  # get existing games' uuids
  game_data = get_all_games(url, headers)
  game_uuids = [i['uuid'] for i in game_data['games']]

  # add them to a user
  for game_uuid in game_uuids:
    response = requests.post(f'{url}/users/{new_user['uuid']}/wishlist/add', 
                                      headers=headers, json={ 'item_uuid': game_uuid })
    assert response.status_code == 200
  
  # verify list of existing games is now identical to a user's wishlist
  response = requests.get(f'{url}/users/{new_user['uuid']}/wishlist', headers=headers)
  assert response.status_code == 200

  user_games = response.json()
  assert len(user_games['items']) == len(game_uuids)

  # remove games from wishlist
  for index, game in enumerate(user_games['items'], start=1):
    response = requests.post(f'{url}/users/{new_user['uuid']}/wishlist/remove', headers=headers, json={ 'item_uuid': game['uuid']} )
    assert response.status_code == 200
    header_data = response.headers
    assert header_data['content-type'] == 'application/json'

    data = response.json()
    validate(instance=data, schema=whishlist_schema)    

    # verify games are indeed removed
    response = requests.get(f'{url}/users/{new_user['uuid']}/wishlist', headers=headers)
    assert response.status_code == 200
    data = response.json()
    print(len(data['items']), len(user_games['items']) - index)
    assert len(data['items']) == len(user_games['items']) - index
    assert game not in data['items']

  # verify list now is empty
  response = requests.get(f'{url}/users/{new_user['uuid']}/wishlist', headers=headers)
  assert response.status_code == 200

  user_games = response.json()
  assert [] == user_games['items']
  

task_ids = ['api-5', 'api-25']
test_params = [(post_users_valid[0], game) for game in games_invalid_uuids]
test_params_with_task_ids = [val + (task, ) for val in test_params for task in task_ids]
@allure.title('post /users/{user_uuid}/wishlist')
@allure.description('Verify invalid items can not be added to a wishlist')
@allure.testcase('E-3')
@pytest.mark.parametrize("test_data, game, task", test_params_with_task_ids)
# @pytest.mark.skip()
def test_users_uuid_wishlist_add_invalid(test_data, game, task, url):
  headers = auth_header | {'X-Task-Id': task}
  delete_users(url, headers)
  new_user = create_user(url, headers, test_data)

  response = requests.post(f'{url}/users/{new_user['uuid']}/wishlist/add', 
                                    headers=headers, json={ 'item_uuid': game['item_uuid'] })
  assert response.status_code == game['code']
  
  # verify list is still empty
  response = requests.get(f'{url}/users/{new_user['uuid']}/wishlist', headers=headers)
  assert response.status_code == 200

  user_games = response.json()
  assert [] == user_games['items']