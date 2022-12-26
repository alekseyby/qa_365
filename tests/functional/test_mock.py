import pytest
import requests
import json
from common.mockserver import MockServer


@pytest.fixture
def mock_server(request):
    # Setup: Flask server start
    server = MockServer()
    server.start()
    yield server
    # Teardown: server stop
    server.shutdown_server()


@pytest.mark.mock_test
def test_mock_server(mock_server):
    server = MockServer(port=1234)
    server.start()
    server.add_json_response("/mocked_url", dict(user_name="Mock_User"))
    response = requests.get(server.url + "/mocked_url")
    assert response.status_code == 200
    response = json.loads(response.text)
    assert response['user_name'] == 'Mock_User'

