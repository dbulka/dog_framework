from configs.config import ENDPOINT_URL, BREEDS_RESOURCE, ALL_BREEDS_JSON, RANDOM_VAR, RANDOM_CONST
from core.endpoint import Endpoint
from core.tools import validate_all_breed, check_status_content
import pytest


@pytest.mark.parametrize('ep', [(Endpoint(ENDPOINT_URL))])
def test_smoke_all_breeds_endpoint(ep):
    """
    Smoke test Endpoint
    """
    response = ep.run(resource="", method='GET')
    assert response.status_code == 200


@pytest.mark.dependency(depends=["test_smoke_all_breeds_endpoint"])
@pytest.mark.parametrize('ep, breeds_resource, all_breeds',
                         [(Endpoint(ENDPOINT_URL), BREEDS_RESOURCE, ALL_BREEDS_JSON)])
def test_all_breeds_endpoint(ep, breeds_resource, all_breeds):
    """
    Test all breeds including any sub breeds.
    """
    resource = breeds_resource + "/all"
    response = ep.run(resource, method='GET')
    resp_content = check_status_content(response, all_breeds)
    validate_all_breed(resp_content["message"])


@pytest.mark.dependency(depends=["test_smoke_all_breeds_endpoint"])
@pytest.mark.parametrize('ep, breeds_resource, all_breeds',
                         [(Endpoint(ENDPOINT_URL), BREEDS_RESOURCE, ALL_BREEDS_JSON)])
def test_random_breeds_endpoint(ep, breeds_resource, all_breeds):
    """
    Test random breed including any sub breeds.
    """
    resource = breeds_resource + "/all/random"
    response = ep.run(resource, method='GET')
    resp_content = check_status_content(response, all_breeds)
    validate_all_breed(resp_content["message"])
    assert len(resp_content["message"]) == RANDOM_CONST


@pytest.mark.dependency(depends=["test_smoke_all_breeds_endpoint"])
@pytest.mark.parametrize('ep, breeds_resource, all_breeds',
                         [(Endpoint(ENDPOINT_URL), BREEDS_RESOURCE, ALL_BREEDS_JSON)])
def test_10_random_breeds_endpoint(ep, breeds_resource, all_breeds):
    """
    Test 10 random breed including any sub breeds.
    """
    resource = breeds_resource + "/all/random/10"
    response = ep.run(resource, method='GET')
    resp_content = check_status_content(response, all_breeds)
    validate_all_breed(resp_content["message"])
    assert len(resp_content["message"]) == RANDOM_VAR





