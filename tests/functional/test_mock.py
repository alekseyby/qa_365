import pytest
import requests
import json
from common.mockserver import MockServer


@pytest.fixture
def mock_server(request):
    server = MockServer()
    server.start()
    yield server
    server.shutdown_server()


@pytest.mark.api_test
def test_mock_server(mock_server):
    server = MockServer(port=1234)
    server.start()
    server.add_json_response("/json", dict(user_name="Mock_User"))
    response = requests.get(server.url + "/json")
    assert response.status_code == 200
    response = json.loads(response.text)
    assert response['user_name'] == 'Mock_User'

