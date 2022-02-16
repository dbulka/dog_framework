import json
import logging
from pathlib import Path


def get_schema(file_path: str):
    """This function loads the given schema available"""
    file_path = Path(__file__) / file_path
    with open(file_path, 'r') as file:
        schema = json.load(file)
    return schema


def validate_schemas(instance: object, file: object):
    """
    Validate keys and value types
    """
    missed_keys, wrong_types = True, True
    for key in instance.keys():
        if key not in file.keys():
            missed_keys = False
            logging.warning(f'Missed key in the file: {key}')
            continue
        if type(instance[key]) != type(file[key]):
            wrong_types = False
            logging.warning(
                f'Wrong key type in the file: {key} with type {type(file[key])} instead of {type(instance[key])}')
            continue
    if missed_keys and wrong_types:
        return True
    else:
        return False


def validate_json(instance_path: str, file: object):
    """
    Validate that the file equal to the instance
    """
    if type(file) is str:
        file = json.loads(file)
    instance_json = get_schema(instance_path)
    return validate_schemas(instance_json, file)


def get_resp_content(response):
    """
    Convert str to json
    """
    resp = response.content.decode('utf-8')
    return json.loads(resp)


def validate_all_breed(message: dict):
    """
    Validate message field format
    """
    for key in message.keys():
        assert type(key) is str
        assert type(message[key]) is list


def check_status_content(response, master_breeds):
    assert response.status_code == 200
    resp_content = get_resp_content(response)
    is_valid = validate_json(master_breeds, resp_content)
    assert is_valid is True
    return resp_content