from configs.config import ENDPOINT_URL, BREED_RESOURCE, MASTER_BREEDS_JSON
from core.endpoint import Endpoint
import pytest

from core.tools import get_resp_content, validate_json


@pytest.mark.parametrize('ep', [(Endpoint(ENDPOINT_URL))])
def test_smoke_breed_endpoint(ep):
    """
    Smoke test Endpoint
    """
    response = ep.run(resource="", method='GET')
    assert response.status_code == 200


@pytest.mark.parametrize('ep, breed_resource, master_breeds',
                         [(Endpoint(ENDPOINT_URL), BREED_RESOURCE, MASTER_BREEDS_JSON)])
def test_breed_endpoint(ep, breed_resource, master_breeds, random_breed):
    """
    Test all master breed names
    """
    resource = breed_resource + f'/{random_breed}/list'
    response = ep.run(resource, method='GET')
    assert response.status_code == 200
    resp_content = get_resp_content(response)
    is_valid = validate_json(master_breeds, resp_content)
    assert is_valid is True
