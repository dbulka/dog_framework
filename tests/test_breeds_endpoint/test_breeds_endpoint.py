from configs.config import ENDPOINT_URL, BREEDS_RESOURCE, MASTER_BREEDS_JSON, RANDOM_VAR
from core.endpoint import Endpoint
from core.tools import get_resp_content, check_status_content
import pytest


@pytest.mark.parametrize('ep', [(Endpoint(ENDPOINT_URL))])
def test_smoke_breeds_endpoint(ep):
    """
    Smoke test Endpoint
    """
    response = ep.run(resource="", method='GET')
    assert response.status_code == 200


@pytest.mark.dependency(depends=["test_smoke_breeds_endpoint"])
@pytest.mark.parametrize('ep, breeds_resource, master_breeds',
                         [(Endpoint(ENDPOINT_URL), BREEDS_RESOURCE, MASTER_BREEDS_JSON)])
def test_breeds_endpoint(ep, breeds_resource, master_breeds):
    """
    Test all master breed names
    """
    response = ep.run(breeds_resource, method='GET')
    check_status_content(response, master_breeds)


@pytest.mark.skip(reason="error is the last assert")
@pytest.mark.dependency(depends=["test_smoke_breeds_endpoint"])
@pytest.mark.parametrize('ep, breeds_resource, master_breeds',
                         [(Endpoint(ENDPOINT_URL), BREEDS_RESOURCE, MASTER_BREEDS_JSON)])
def test_random_breed_endpoint(ep, breeds_resource, master_breeds):
    """
    Test single random master breed
    """
    resource = breeds_resource + "/random"
    response = ep.run(resource, method='GET')
    assert response.status_code == 200
    resp_content = get_resp_content(response)
    assert resp_content["message"] is str


@pytest.mark.dependency(depends=["test_smoke_breeds_endpoint"])
@pytest.mark.parametrize('ep, breeds_resource, master_breeds',
                         [(Endpoint(ENDPOINT_URL), BREEDS_RESOURCE, MASTER_BREEDS_JSON)])
def test_10_random_breed_endpoint(ep, breeds_resource, master_breeds):
    """
    Test 10 random master breeds
    """
    resource = breeds_resource + "/random/10"
    response = ep.run(resource, method='GET')
    resp_content = check_status_content(response, master_breeds)
    assert len(resp_content["message"]) == RANDOM_VAR



