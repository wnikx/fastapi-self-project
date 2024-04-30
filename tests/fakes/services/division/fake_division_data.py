from contextlib import nullcontext as does_not_raise

import pytest
from fastapi import HTTPException

from src.schemas.division import AddNewPositionShema

fake_new_position_schema = AddNewPositionShema(new_position="fake_pos")


TEST_CHANGE_POSITION_PARAMS = [
    (1, AddNewPositionShema(new_position="fake_pos"), does_not_raise()),
    (99, AddNewPositionShema(new_position="fake_pos"), pytest.raises(HTTPException)),
]

TEST_DELETE_POSITION_PARAMS = [
    (1, does_not_raise()),
    (99, pytest.raises(HTTPException)),
]
