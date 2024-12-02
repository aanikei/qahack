# Test suite

`/user`
| ID | API | Summary | Test data | Expected result | Release | Dev | Defects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A-1 | api-6, api-21 | get /users, without any parameters | post_users_valid | 1. Status 200 <br/>2. Number of returned records corresponds to number of inserted records | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-21 |
| A-2 | api-6, api-21 | get /users, with parameters to check 20 records  | get_users_all_parameters | 1. Status 200 <br/>2. Corresponding number of records returned | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-6 |
| A-3 | api-22, api-3 | post /users | post_users_valid | 1. Status 200 <br/>2. Returned record contains the same fields, empty avatar_url and valid uuid | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Green}{\textsf{ Passed }}}}\$ | - |

`/users/{user_uuid}`
| ID | API | Summary | Test data | Expected result | Release | Dev | Defects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B-1 | api-23 | get /users/{user_uuid} | post_users_valid | 1. Status 200 <br/>2. Returned record contains the same fields, empty avatar_url and valid uuid | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Green}{\textsf{ Passed }}}}\$ | - |
| B-2 | api-4, api-24 | patch /users/{user_uuid} with valid data | patch_users_valid | 1. Status 200 <br/>2. Returned record contains the updated field and the rest of the fields is the same. Updated user can log in | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | Api-24 |
| B-3 | api-4, api-24 | patch /users/{user_uuid} with invalid data | patch_users_invalid | 1. Status 400 <br/>2. User is not updated | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Green}{\textsf{ Passed }}}}\$ |  |
| B-4 | api-1 | delete /users/{user_uuid} with or without authorization | post_users_valid | 1. Status 204 or 404 depending on authorization <br/>2. User is actually deleted and cannot be found or log in | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Green}{\textsf{ Passed }}}}\$ | - |

`/users/login`
| ID | API | Summary | Test data | Expected result | Release | Dev | Defects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | api-7 | get /users/{user_uuid} by valid email and password | post_users_valid | 1. Status 200 <br/>2. Returned record corresponding the same fields | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-7 |
| C-2 | api-7 | get /users/{user_uuid} by invalid email and password | post_users_login_invalid | 1. Status 400 or 404 <br/>2. Error message corresponds to invalid or missing field | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Green}{\textsf{ Passed }}}}\$ | - |

`/users/{user_uuid}/avatar`
| ID | API | Summary | Test data | Expected result | Release | Dev | Defects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D-1 | api-11 | put /users/{user_uuid}/avatar with valid data | put_images_valid | 1. Status 200 <br/>2. Avatar url is added <br/>3. Headers and schema are correct | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-11 |
| D-2 | api-11 | put /users/{user_uuid}/avatar with invalid data | put_images_invalid | 1. Status 413 <br/>2. Error message provided <br/>3. Headers and schema are correct | ${{\color{Green}{\textsf{ Passed* }}}}\$ | ${{\color{Green}{\textsf{ Passed* }}}}\$ | Prod issue, non-image file can be uploaded and file limit for jpeg is not honored |

`/users/{user_uuid}/wishlist`
| ID | API | Summary | Test data | Expected result | Release | Dev | Defects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E-1 | api-5, api-25 | post /users/{user_uuid}/wishlist with valid data | games in db | 1. Status 200 <br/>2. Games are successfully added to a wishlist <br/>3. Headers and schema are correct | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-5, api-25 |
| E-2 | Api-8 | post /users/{user_uuid}/wishlist/remove with valid data | - | 1. Status 200 <br/>2. Games are successfully removed to a wishlist <br/>3. Headers and schema are correct | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-8 |
| E-3 | api-5, api-25 | post/users/{user_uuid}/wishlist/add with invalid data | games_invalid_uuids | 1. Status 400 or 404 <br/>2. Error message provided | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-5 |

`get /categories/{category_uuid}/games`
| ID | API | Summary | Test data | Expected result | Release | Dev | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-1 | api-10 | get /categories/{category_uuid}/games | games in db | 1. Status 200 <br/>2. Number of games in category is in accordance with number of games with given category <br/>3. Headers and schema are correct | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | api-10  |
| F-2 | api-10 | get /categories/{category_uuid}/games | get_categories_all_parameters | 1. Status 200 <br/>2. Corresponding number of records returned <br/>3. Headers and schema are correct | ${{\color{Green}{\textsf{ Passed }}}}\$ | ${{\color{Green}{\textsf{ Passed }}}}\$ | - |
| F-3 | api-10 | get /categories/{category_uuid}/games | invalid authorisation | 1. Status 404 | ${{\color{Red}{\textsf{ Failed }}}}\$ | ${{\color{Red}{\textsf{ Failed }}}}\$ | Prod issue, status 200 |
| - |


Not tested:

`/users/{user_uuid}/cart:`

`/users/{user_uuid}/cart/change`

`/users/{user_uuid}/cart/remove`

`/users/{user_uuid}/cart/clear`

`/users/{user_uuid}/orders`

`/orders/{order_uuid}/status`

`/users/{user_uuid}/payments`


# Bug reports

| ID | Summary | Steps | Expected result | Actual result |
| --- | --- | --- | --- | --- |
| api-10 | Discrepancy between data in `/games` categories and `/categories/{category_uuid}/games` games  | 1. Gather all categories from games in `/games` endpoint <br/>2. Gather all games from `/categories/{category_uuid}/games` endpoint <br/>3. Reconcile data | Data from both endpoints can be reconciled | Difference in data |
| api-5 | 422 status while adding valid (either existing or non-existing) game uuid to users' wishlist | 1. Get an existing game's UUID or create one that is not present in games' UUIDs but is valid and post it to `/users/{user_uuid}/wishlist/add` | Status 404 | Status 422 |
| api-25 | A game added to user's wishlist is not saved (cannot reproduce manually) | 1. Get an existing game's UUID and post it to `/users/{user_uuid}/wishlist/add` of a new user <br/>2. Get items from `/users/{user_uuid}/wishlist/` and verify new item is present | Length of `items` array is 1 | Length is 0 |
| api-8 | Games are not removed from wishlist | 1. Add games to a user's wishlist <br/>2. Post any game's UUID that user have to `/users/{user_uuid}/wishlist/remove` <br/>3. Get items from `/users/{user_uuid}/wishlist/` and verify item was removed  | Length of `items` array is reduced by 1 | Length is not changed |
| api-11 | Dev env uses different avatar url | 1. Post any valid image to `/users/{user_uuid}/avatar` <br/>2. Verify https://gravatar.com url is returned in 'avatar_url' | https://gravatar.com url is present in 'avatar_url' | https://qa-playground.com url is used |
| api-7 | Cannot log in using valid credentials | 1. Create any new user <br/>2. Send post to `/users/login` using created user's credentiald | Status 200 and user returned | Status 404 |
| api-21 | meta/total is incorrectly calculated for `/users` | 1. Delete all users and start adding them <br/>2. Verify that ['meta']['total'] value for number of users less than 10 corresponds to length of ['users'] array (without using any parameters) | Numbers are matching | Numbers are not matching |
| api-6 | offset parameter has no effect while getting data from `/users` | 1. Set offset parameter to non-0 value and verify that data is returned corresponding to offset | Offset is honored | Offset has no effect |
| api-24 | Updated user cannot log in | 1. Update any field of a user <br/>2. Send post to `/users/login` | Response code 200 | Response code 404 |

# Setup instructions

**install python & git if not installed, then**

create a test directory

create virtual environment `python -m venv env`

activate virtual env (in CMD): `activate.bat`

clone repo into test directory `git clone https://github.com/aanikei/qahack.git`

install dependencies `pip install pytest requests allure-pytest python-dotenv pytest-retry jsonschema`

cd into `qahack` directory and create a .env file with content `EMAIL=your@mail.com`

run tests `pytest --alluredir allure-results --retries 6 --env dev` **(for dev env, --retries 6 is used because envs are not stable)**

`pytest --alluredir allure-results --retries 6 --env release` **(for release env)**

run report `allure serve allure-results`
