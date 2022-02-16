from core.endpoint import Endpoint
import pytest
from unittest.mock import sentinel


class TestRESTEndpoint:

    @pytest.mark.parametrize('endpoint', [(sentinel.endpoint)])
    def test_init(self, endpoint):
        result = Endpoint(endpoint)
        assert result._endpoint == sentinel.endpoint
