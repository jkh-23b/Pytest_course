import requests
from src.enums.global_enums import GlobaErrorMessages
from configuration import SERVICE_URL
def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobaErrorMessages.WRONG_STATUS_CODE.value

    print(response.json())
