import requests
import allure
import pytest
from data import *
from utils import *
from schemas import *
from collections import Counter
from jsonschema import validate

# this check seems not needed but well...
task_id = 'api-10'
@allure.title('get /categories')
@allure.description('Verify categories with parameters to check 16 available records')
@allure.testcase('F-1')
@pytest.mark.parametrize("test_data", get_categories_all_parameters)
# @pytest.mark.skip()
def test_get_categories_all_params_first_16(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}

  # get all categories
  data = get_all_categories(url, headers=headers)
  all_categories = data['categories']

  # get categories with params
  response = requests.get(f'{url}/categories', headers=headers, params=test_data)
  assert response.status_code == 200
  parameterized_categories = response.json()
  start, end = param_testing(test_data, 19)

  # verify sliced all_categories are the same as parameterized_categories
  assert all_categories[start:end] == parameterized_categories['categories']
  assert parameterized_categories['meta']['total'] == 16


task_id = 'api-10'
@allure.title('get /categories/{category_uuid}/games')
@allure.description('Verify categories and games are in sync')
@allure.testcase('F-2')
# @pytest.mark.skip()
def test_get_categories_uuid_games(url):
  headers = auth_header | {'X-Task-Id': task_id}

  # get all categories' uuids
  data = get_all_categories(url, headers=headers)
  all_categories = data['categories']
  categories_uuids = [i['uuid'] for i in all_categories]

  # get all games
  data = get_all_games(url, headers=headers)
  all_games = data['games']

  # verify games' categories are legit and present in categories list
  for game in all_games:
    categories = set(game['category_uuids'])
    assert categories.issubset(categories_uuids)

  for category_uuid in categories_uuids:
    response = requests.get(f'{url}/categories/{category_uuid}/games', 
                                        headers=headers, params={ 'limit': 100 })
    assert response.status_code == 200
    header_data = response.headers
    assert int(header_data['content-length']) == len(response.content)
    assert header_data['content-type'] == 'application/json'
    data = response.json()
    games_in_category = data['games']

    # can be checked as games array always small
    assert len(games_in_category) == data['meta']['total']

    # verify sorted games from /categories/{category_uuid}/games 
    # are in line with filtered and sorted games from /games
    sorted_games_from_categories = sorted(games_in_category, key=lambda x: x['uuid'])
    filtered_and_sorted_games = sorted(filter(lambda x: category_uuid in x['category_uuids'], 
                                                                      all_games), key=lambda x: x['uuid'])
    assert sorted_games_from_categories == filtered_and_sorted_games
    validate(instance=data, schema=category_uuid_games_schema)


task_id = 'api-10'
@allure.title('get /categories/{category_uuid}/games')
@allure.description('Verify /categories/{category_uuid}/games with parameters')
@allure.testcase('F-3')
@pytest.mark.parametrize("test_data", get_categories_all_parameters)
# @pytest.mark.skip()
def test_get_categories_uuid_games_all_params(test_data, url):
  headers = auth_header | {'X-Task-Id': task_id}

  # get most used category in games 
  data = get_all_games(url, headers=headers)
  all_games = data['games']

  category_uuids = [] 
  for game in all_games:
    category_uuids.extend(game["category_uuids"])

  category_counter = Counter(category_uuids)
  most_common_category = category_counter.most_common(1)[0]

  # get all games from given category
  response = requests.get(f'{url}/categories/{most_common_category[0]}/games', headers=headers, params={ 'limit': 100 })
  assert response.status_code == 200

  category_all_games = response.json()

  # get games from categories with params
  response = requests.get(f'{url}/categories/{most_common_category[0]}/games', headers=headers, params=test_data)
  assert response.status_code == 200
  header_data = response.headers
  assert int(header_data['content-length']) == len(response.content)
  assert header_data['content-type'] == 'application/json'

  data = response.json()
  start, end = param_testing(test_data, 3)

  # verify sliced games from categories are the same as parameterized games from categories
  assert category_all_games['games'][start:end] == data['games']
  assert most_common_category[1] == data['meta']['total']
  validate(instance=data, schema=category_uuid_games_schema)


task_id = 'api-10'
@allure.title('get /categories/{category_uuid}/games')
@allure.description('Verify /categories/{category_uuid}/games with parameters')
@allure.testcase('F-4')
# @pytest.mark.skip()
def test_get_categories_uuid_games_no_auth(url):
  headers = auth_header | {'X-Task-Id': task_id}

  # get any category
  data = get_all_categories(url, headers=headers)
  category = data['categories'][0]['uuid']

  headers['Authorization'] = headers['Authorization'][:-10]
  print(headers)
  # get all games from given category without proper authorization 
  response = requests.get(f'{url}/categories/{category}/games', headers=headers, params={ 'limit': 100 })
  assert response.status_code == 404