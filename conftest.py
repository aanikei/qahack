import pytest
import requests
import os
from data import delete_users, create_user, post_users_valid

RELEASE_LINK = 'https://release-gs.qa-playground.com/api/v1'
DEV_LINK = 'https://dev-gs.qa-playground.com/api/v1'
env_link = DEV_LINK
# env_link = RELEASE_LINK

email = os.getenv('EMAIL')
auth_header = { 'Authorization': f'Bearer qahack2024:{email}' }

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")

@pytest.fixture
def url(request):
  global env_link
  if 'dev' == request.config.getoption("--env"):
    env_link = DEV_LINK
    return DEV_LINK
  elif 'release' == request.config.getoption("--env"):
    env_link = RELEASE_LINK
    return RELEASE_LINK
  else:
    return env_link

def pytest_sessionstart():
  requests.post(f'{env_link}/setup', headers=auth_header)

@pytest.fixture(scope='session')
def create_twenty_users():
  headers = auth_header | {'X-Task-Id': 'api-6'}
  delete_users(env_link, headers=headers)
  for user in post_users_valid[:20]:
    create_user(env_link, headers, user)