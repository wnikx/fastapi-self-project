from contextlib import nullcontext as does_not_raise

import pytest
from fastapi import HTTPException

from src.schemas.division import AddNewDivisionSchema, AddNewPositionShema, AddNewSupervisor

fake_new_position_schema = AddNewPositionShema(new_position="fake_pos")


TEST_CHANGE_POSITION_PARAMS = [
    (1, AddNewPositionShema(new_position="fake_pos"), does_not_raise()),
    (99, AddNewPositionShema(new_position="fake_pos"), pytest.raises(HTTPException)),
]

TEST_DELETE_POSITION_PARAMS = [
    (1, does_not_raise()),
    (99, pytest.raises(HTTPException)),
]

TEST_ADD_SUPERVISOR_SERVICE = [
    (2, AddNewSupervisor(new_supervisor="fake_supervisor"), does_not_raise()),
    (1, AddNewSupervisor(new_supervisor="fake_supervisor"), pytest.raises(HTTPException)),
    (99, AddNewSupervisor(new_supervisor="fake_supervisor"), pytest.raises(HTTPException)),
]

TEST_CHANGE_DIVISION_NAME_SERVICE_PARAMS = [
    (2, AddNewDivisionSchema(division_title="fake_div"), does_not_raise()),
    (1, AddNewDivisionSchema(division_title="fake_div"), pytest.raises(HTTPException)),
    (99, AddNewDivisionSchema(division_title="fake_div"), pytest.raises(HTTPException)),
]
TEST_DELETE_DIVISION_PARAMS = [
    (2, does_not_raise()),
    (99, pytest.raises(HTTPException)),
    (1, pytest.raises(HTTPException)),
]
