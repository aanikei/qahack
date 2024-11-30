import pytest

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

@pytest.fixture
def url():
    return 'https://release-gs.qa-playground.com/api/v1'
    # return 'https://dev-gs.qa-playground.com/api/v1'