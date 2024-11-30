import pytest
import requests
import os

ENV_LINK = 'https://release-gs.qa-playground.com/api/v1'
# ENV_LINK = 'https://dev-gs.qa-playground.com/api/v1'

@pytest.fixture
def url():
    return ENV_LINK

def pytest_sessionstart():
    email = os.getenv('EMAIL')
    auth_header = { 'Authorization': f'Bearer qahack2024:{email}' }
    requests.post(f'{ENV_LINK}/setup', headers=auth_header)