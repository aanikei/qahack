import os
import requests

email = os.getenv('EMAIL')
auth_header = { 'Authorization': f'Bearer qahack2024:{email}' }

get_users_all_parameters= [ 
  {'offset': 0, 'limit': 2},
  {'offset': 0, 'limit': 10},
  {'offset': 1, 'limit': 5},
  {'offset': 1, 'limit': 9},
  {'offset': 8, 'limit': 2},
  {'offset': 9, 'limit': 1},
  {'offset': 9, 'limit': 10},
  {'offset': 10, 'limit': 9},
  {'offset': 11, 'limit': 8},
  {'offset': 17, 'limit': 1},
  {'offset': 18, 'limit': 1},
  {'limit': 1},
  {'limit': 2},
  {'limit': 18},
  {'offset': 0},
  {'offset': 1},
  {'offset': 8},
  {'offset': 9}
]

post_users_valid = [
  #password
  {'email': 'aatest0@testt.commx', 'password': 'password', 'name': 'aatest0', 'nickname': 'aatest0'},
  {'email': 'aatest1@testt.commx', 'password': 'pass word', 'name': 'aatest1', 'nickname': 'aatest1'},
  {'email': 'aatest2@testt.commx', 'password': '!@#$%^&*()1234567890', 'name': 'aatest2', 'nickname': 'aatest2'},
  {'email': 'aatest3@testt.commx', 'password': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+`=-[]{}};\':",./<>? \\|аб', 'name': 'aatest3', 'nickname': 'aatest3'},
  # {'email': 'aatest16@testt.commx', 'password': '      ', 'name': 'aatest16', 'nickname': 'aatest16'},
  {'email': 'aatest17@testt.commx', 'password': '!@#$%^&*()[]{},./<>?\\|', 'name': 'aatest17', 'nickname': 'aatest17'},
  {'email': 'aatest18@testt.commx', 'password': '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ', 'name': 'aatest18', 'nickname': 'aatest18'},
  #nickname
  {'email': 'aatest4@testt.commx', 'password': 'password', 'name': 'aatest4', 'nickname': 'aa'},
  {'email': 'aatest4.@testt.commx', 'password': 'password', 'name': 'aatest4.', 'nickname': 'ABc'},
  {'email': 'aatest5@testt.commx', 'password': 'password', 'name': 'aatest5', 'nickname': '_.+-'},
  {'email': 'aatest6@testt.commx', 'password': 'password', 'name': 'aatest6', 'nickname': 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.+-'},
  {'email': 'aatest19@testt.commx', 'password': 'password', 'name': 'aatest19', 'nickname': '__'},
  {'email': 'aatest20@testt.commx', 'password': 'password', 'name': 'aatest20', 'nickname': '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'},
  #name
  {'email': 'aatest7@testt.commx', 'password': 'password', 'name': 'Sz', 'nickname': 'aatest7'},
  {'email': 'aatest8@testt.commx', 'password': 'password', 'name': 'Ab', 'nickname': 'aatest8'},
  {'email': 'aatest9@testt.commx', 'password': 'password', 'name': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`=-[]{}};\':",./<>?\\|аб', 'nickname': 'aatest9'},
  {'email': 'aatest21@testt.commx', 'password': 'password', 'name': 'Abc', 'nickname': 'aatest21'},
  {'email': 'aatest22@testt.commx', 'password': 'password', 'name': '10', 'nickname': 'aatest22'},
  {'email': 'aatest23@testt.commx', 'password': 'password', 'name': '~~', 'nickname': 'aatest23'},
  {'email': 'aatest24@testt.commx', 'password': 'password', 'name': '~!@#$%^&*()_+1234567890-={}|[]\\:";\'<>?,./رمزعبور', 'nickname': 'aatest24'},
  #email
  {'email': 'aatest10@testt.commx', 'password': 'password', 'name': 'aatest10', 'nickname': 'aatest10'},
  {'email': 'aate.st1@testt.comx', 'password': 'password', 'name': 'aatest11', 'nickname': 'aatest11'},
  {'email': 'aate_st2@testt.orgx', 'password': 'password', 'name': 'aatest12', 'nickname': 'aatest12'},
  {'email': 'aate-st3@testt.netx', 'password': 'password', 'name': 'aatest13', 'nickname': 'aatest13'},
  {'email': 'aate+st4@testt.c', 'password': 'password', 'name': 'aatest14', 'nickname': 'aatest14'},
  {'email': 'aate+st5@testt.co.uk', 'password': 'password', 'name': 'aatest15', 'nickname': 'aatest15'},
  {'email': 'veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeryyyyyy@loooooooooooooooooooooooooooooooong.emaaaaaaaaaaail', 'password': 'password', 'name': 'aatest22', 'nickname': 'aatest22'}
]

post_users_login_invalid = [
  {'email': 'aatest0@testt.commx', 'password': 'passwor', 'code': 404, 'message' : 'Could not find user with given credentials'},
  {'email': 'aatest0@testt.commx', 'password': '', 'code': 400, 'message' : 'request body has an error: doesn\'t match schema #/components/schemas/Login: Error at \"/password\": minimum string length is 6'},
  {'email': 'aatest0@testt.comm', 'password': 'password', 'code': 404, 'message' : 'Could not find user with given credentials'},
  {'email': '', 'password': 'password', 'code': 400, 'message' : 'request body has an error: doesn\'t match schema #/components/schemas/Login: Error at \"/email\": minimum string length is 5'},
  {'password': 'password', 'code': 400, 'message' : 'request body has an error: doesn\'t match schema #/components/schemas/Login: Error at \"/email\": property \"email\" is missing'},
  {'email': 'aatest0@testt.comm', 'code': 400, 'message' : 'request body has an error: doesn\'t match schema #/components/schemas/Login: Error at \"/password\": property \"password\" is missing'},
  {'code': 400, 'message' : 'request body has an error: value is required but missing'},
]

patch_users_valid = [
  #password
  {'password': 'password'},
  {'password': 'pass word'},
  {'password': 'p     '},
  {'password': '!@#$%^&*()1234567890'},
  {'password': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+`=-[]{}};\':",./<>? \\|аў'},
  {'password': '!@#$%^&*()[]{},./<>?\\|'},
  {'password': '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'},
  #nickname
  {'nickname': 'aa'},
  {'nickname': 'ABc'},
  {'nickname': '_.+-'},
  {'nickname': 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.+-'},
  {'nickname': '__'},
  {'nickname': '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'},
  #name
  {'name': 'Sz'},
  {'name': 'Ab'},
  {'name': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`=-[]{}};\':",./<>?\\|аб'},
  {'name': 'Abc'},
  {'name': '10'},
  {'name': '~~'},
  {'name': '~!@#$%^&*()_+1234567890-={}|[]\\:";\'<>?,./رمزعبور'},
  #email
  {'email': 'aatest10@testt.commx'},
  {'email': 'aate.st1@testt.comx'},
  {'email': 'aate_st2@testt.orgx'},
  {'email': 'aate-st3@testt.netx'},
  {'email': 'aate+st4@testt.c'},
  {'email': 'aate+st5@testt.co.uk'},
  {'email': 'veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeryyyyyy@loooooooooooooooooooooooooooooooong.emaaaaaaaaaaail'}
]

patch_users_invalid = [
  #password
  {'password': ''},
  {'password': None},
  {'password': 'p'},
  {'password': 'pa'},
  {'password': 'passw'},
  {'password': '     '},
  {'password': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+`=-[]{}};\':",./<>? \\|аў123456890-09876543'},
  {'password': '\r\n\t\f\b'},
  {'password': []},
  #nickname
  {'nickname': 'a'},
  {'nickname': '~!@#$%^&*()_+`=-[]{}};\':'},
  {'nickname': 'аў'},
  {'nickname': ''},
  {'nickname': '   '},
  {'nickname': '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'},
  {'nickname': None},
  #name
  {'name': 'S'},
  {'name': ' '},
  {'name': None},
  {'name': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`=-[]{}};\':",./<>?\\|абABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXY'},
  {'name': '\r\n\t\f\b'},
  {'name': ''},
  #email
  {'email': 'a@b.'},
  {'email': 'a@uk.'},
  {'email': '@co.uk'},
  {'email': '\r\n\t\f\b@testt.netx'},
  {'email': '~!@#$%^&*()_+`=-[]{}};\':@testt.c'},
  {'email': 'رمزعبور@testt.co.uk'},
  {'email': 'veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeryyyyyyveeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeryyyyyy@loooooooooooooooooooooooooooooooong.emaaaaaaaaaaail'}
]

put_images_valid = [
  {'image': 'jpeg_100560.jpeg'},
  {'image': 'jpeg_951357.jpeg'},
  {'image': 'jpeg_2089830.jpeg'},
  {'image': 'jpeg_2095249.jpeg'},
  {'image': 'png_100.png'},
  {'image': 'png_10000.png'},
  {'image': 'png_2097151.png'}
]

put_images_invalid = [
  {'image': 'png_2097155.png', 'code': 400, 'error': 'request body has an error'},
  {'image': 'png_5001740.png', 'code': 413, 'error': 'request entity is larger than limits'},
  # {'image': 'jpeg_2097905.jpeg', 'code': 400, 'error': 'request body has an error'}, #works in prod
  {'image': 'jpeg_4746513.jpeg', 'code': 413, 'error': 'request entity is larger than limits'},
  # {'image': 'image_generator.py', 'code': 413, 'error': '?'}  #works in prod
]

games_invalid_uuids = [
  { "item_uuid": "2990ecdd-4d3d-4de2-91b9-d45d794c82bc", 'code': 404 },
  { "item_uuid": "s378c074-92d6-4d8c-b6d3-878c08dbe27f", 'code': 400 },
  { "item_uuid": "03dbad48-433d-9901-dd5332f5d9ea", 'code': 400 },
  { "item_uuid": "cb620f56-daa4-43e0-b4a0-e80f8e5be27", 'code': 400 },
  { "item_uuid": "aca79a7c-5b66-4ff2b3b8-57e56fc053a7", 'code': 400 },
  { "item_uuid": "aca79a7c 5b66 4ff2 b3b8 57e56fc053a7", 'code': 400 },
]

get_categories_all_parameters= [ 
  {'offset': 0, 'limit': 2},
  {'offset': 0, 'limit': 10},
  {'offset': 1, 'limit': 5},
  {'offset': 1, 'limit': 9},
  {'offset': 8, 'limit': 2},
  {'offset': 9, 'limit': 1},
  {'offset': 9, 'limit': 10},
  {'offset': 10, 'limit': 9},
  {'offset': 14, 'limit': 1},
  {'limit': 1},
  {'limit': 2},
  {'limit': 15},
  {'offset': 0},
  {'offset': 1},
  {'offset': 5},
  {'offset': 6}
]

def create_user(url, headers, test_data):
  response = requests.post(f'{url}/users', headers=headers, json=test_data)
  assert response.status_code == 200
  return response.json()

def delete_users(url, headers):
  response = requests.get(f'{url}/users', headers=headers, params={ 'limit': 20})
  data = response.json()
  assert response.status_code == 200
  current_users = data['users']

  uuids = [user['uuid'] for user in current_users]

  for uuid_str in uuids:
    requests.delete(f'{url}/users/{uuid_str}', headers=headers)
    
def get_all_categories(url, headers):
  response = requests.get(f'{url}/categories', headers=headers, params={ 'limit': 100 })
  assert response.status_code == 200
  return response.json()

def get_all_games(url, headers):
  response = requests.get(f'{url}/games', headers=headers, params={ 'limit': 100 })
  assert response.status_code == 200
  return response.json()