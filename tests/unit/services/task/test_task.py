import pytest

from src.services.task import create_task
from tests.fakes import fake_task_schema


async def test_create_task(
    fake_token,
    add_company,
    delete_company,
    add_position_and_role,
    delete_all_position_and_role,
    add_user,
    delete_user,
):
    await add_company()
    await add_position_and_role()
    await add_user()
    with pytest.raises(Exception):
        result = await create_task(fake_task_schema, fake_token)
        assert result == True

    await delete_user()
    await delete_all_position_and_role()
    await delete_company()
