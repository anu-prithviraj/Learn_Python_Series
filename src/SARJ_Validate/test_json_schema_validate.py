"""
pytest to check whether the json is getting validated aganist 
the given schema.
"""

from json_schema_validate import ValidateJson
import pytest
import pathlib
import os

get_abs_path = pathlib.Path().absolute()
valid_json_path = os.path.join(get_abs_path,"InputData","valid_json.json")
invalid_json_path = os.path.join(get_abs_path,"InputData","invalid_json.json")
schema_path = os.path.join(get_abs_path,"Schema","schema.json")

def test_happy_json_load():
    """
    Test method to load a given json file.
    Input:
        valid json
    Output:
        Return a python object   
    """
    
    loaded_json = ValidateJson(valid_json_path, schema_path)
    output = loaded_json.load_json(valid_json_path)
    assert output == ( {'contact_number': 1234567890, 'id': 10, 'name': 'Anu'}) 

def test_valid_json_validation():

    """
    Test method for validating a valid json.
    Input:
        valid json, schema to match
    Output:
        Return a True   
    """

    valid_json_object = ValidateJson(valid_json_path, schema_path)
    output = valid_json_object.validate_json()
    assert output == True 

def test_invalid_json_validation():

    """
    Test method for validating an invalid json.
    Input:
        valid json, schema to match
    Output:
        Return a False   
    """

    invalid_json_object = ValidateJson(invalid_json_path, schema_path)
    output = invalid_json_object.validate_json()
    assert output == False   