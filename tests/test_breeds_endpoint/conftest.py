import pytest
import random

from configs.config import MASTER_BREEDS_JSON
from core.tools import get_schema, get_resp_content, validate_json


@pytest.fixture
def random_breed():
    breeds = get_schema(MASTER_BREEDS_JSON)["message"]
    index = random.randint(0, len(breeds))
    return breeds[index]
