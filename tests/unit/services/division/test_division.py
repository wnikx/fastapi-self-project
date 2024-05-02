import pytest

from src.services.division import (
    add_new_position_service,
    add_supervisor_service,
    change_division_name_service,
    change_position_service,
    check_ceo_exist,
    delete_division_service,
    delete_position_sevice,
)
from tests.fakes import (
    TEST_ADD_SUPERVISOR_SERVICE,
    TEST_CHANGE_DIVISION_NAME_SERVICE_PARAMS,
    TEST_CHANGE_POSITION_PARAMS,
    TEST_DELETE_DIVISION_PARAMS,
    TEST_DELETE_POSITION_PARAMS,
    fake_new_position_schema,
)


async def test_check_ceo_exist(add_ceo_position, delete_ceo_position):
    ceo = await check_ceo_exist()

    assert ceo == False

    await add_ceo_position()
    assert ceo is not None

    await delete_ceo_position()


async def test_add_new_position_service(fake_token):
    new_fake_pos = await add_new_position_service(fake_new_position_schema, fake_token)
    assert new_fake_pos == True
    new_fake_pos_2 = await add_new_position_service(fake_new_position_schema, fake_token)
    assert new_fake_pos_2 == True


@pytest.mark.parametrize("pos_id, data, expectation", TEST_CHANGE_POSITION_PARAMS)
async def test_change_position_service(pos_id, data, expectation, fake_token):
    with expectation:
        new_pos = await change_position_service(data=data, position_id=pos_id, token=fake_token)
        assert new_pos == True


@pytest.mark.parametrize("pos_id, expectation", TEST_DELETE_POSITION_PARAMS)
async def test_delete_position_service(
    pos_id,
    expectation,
    add_position_and_role,
    delete_all_position_and_role,
    fake_token,
):
    await add_position_and_role()

    with expectation:
        del_pos = await delete_position_sevice(position_id=pos_id, token=fake_token)
        assert del_pos == True

    await delete_all_position_and_role()


@pytest.mark.parametrize("div_id, data, expectation", TEST_ADD_SUPERVISOR_SERVICE)
async def test_add_supervisor_service(
    div_id,
    data,
    expectation,
    add_ceo_position,
    delete_ceo_position,
    fake_token,
):
    await add_ceo_position()

    with expectation:
        add_dep = await add_supervisor_service(div_id, data, fake_token)
        assert add_dep == True

    await delete_ceo_position()


@pytest.mark.parametrize("div_id, data, expectation", TEST_CHANGE_DIVISION_NAME_SERVICE_PARAMS)
async def test_change_division_name_service(
    div_id,
    data,
    expectation,
    add_ceo_position,
    delete_ceo_position,
    fake_token,
):
    await add_ceo_position()

    with expectation:
        change_name = await change_division_name_service(div_id, data, fake_token)
        assert change_name == True

    await delete_ceo_position()


@pytest.mark.parametrize("div_id, expectation", TEST_DELETE_DIVISION_PARAMS)
async def test_delete_division_service(
    div_id,
    expectation,
    add_ceo_position,
    delete_ceo_position,
    fake_token,
):
    await add_ceo_position()

    with expectation:
        del_div = await delete_division_service(div_id, fake_token)
        assert del_div == True

    await delete_ceo_position()
