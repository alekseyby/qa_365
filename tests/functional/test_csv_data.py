import requests
import pytest
import json
import allure
from tests.variables import USERS_URL
from common.file_helper import read_test_data_from_csv


@allure.title("Test: getting user id from csv file, makes request to api and assert email from csv ")
@pytest.mark.api_test
@pytest.mark.parametrize("user_id,first_name,username, expected_email", read_test_data_from_csv('data/users.csv'))
def test_using_csv_get_user_id_check_email(user_id, first_name, username, expected_email):
    response = requests.get(USERS_URL + f'/{user_id}')
    response_json = json.loads(response.text)
    assert response.status_code == 200
    email = response_json['email']
    assert email == expected_email
