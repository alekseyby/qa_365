import pytest
import requests
import json
import random
import allure
from common import log_helper
from tests.variables import USERS_URL, POSTS_URL


@pytest.fixture(scope='session')
def build_request_body():
    """Builder for api requests body"""
    def _build(title, body, user_id):
        return {
            'title': title,
            'body': body,
            'userId': user_id
        }
    return _build


@pytest.fixture(scope='session')
def get_random_user_id():
    """Get random user_id
    scope = 'session' will use same user id for all tests,
    otherwise set 'function' to get random users id for tests"""
    response = requests.get(url=USERS_URL)
    response_json = json.loads(response.text)
    assert response.status_code == 200
    user = random.choice(response_json)
    # add user email to allure report
    with allure.step(f' Test email is - {user["email"]}'):
        yield user['id']


class TestApiGateway:
    """Class to validate API responses"""

    @allure.title("Test: User's posts has correct id's")
    @allure.description("""Test checks that id field has valid type and number""")
    @pytest.mark.api_test
    def test_user_has_valid_post_ids(self, get_random_user_id):
        with allure.step('Get random user id from API'):
            user_id = get_random_user_id
        user_posts = requests.get(url=POSTS_URL + f'?userId={user_id}')
        user_posts = json.loads(user_posts.text)
        with allure.step('Check user has post_id in 1-100'):
            for post in user_posts:
                assert 1 <= post['id'] <= 100, 'post_id is NOT between 1-100'

    @allure.title("Test: POST request returns correct response")
    @allure.description("""Test checks that the topic is created and with the correct fields""")
    @pytest.mark.api_test
    @pytest.mark.parametrize(('title', 'body'), [('foo', 'bar'), ('spam', 'eggs')])
    def test_post_request_returns_correct_response(self, get_random_user_id, build_request_body, title, body):
        header = {'Content-type': 'application/json; charset=UTF-8'}
        api_data = build_request_body(title=title, body=body, user_id=get_random_user_id)
        with allure.step('Create user post via API'):
            response = requests.post(url=POSTS_URL, data=json.dumps(api_data), headers=header)
        created_post = json.loads(response.text)
        with allure.step('Verify user post created and has valid data'):
            assert response.status_code == 201
            assert created_post['title'] == title
            assert created_post['body'] == body
            assert created_post['userId'] == get_random_user_id
            assert type(created_post['id']) is int
        # log user post data
        log = log_helper.get_logger(__name__)
        log.info(f' Test user create post: {created_post}')

