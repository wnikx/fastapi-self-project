import pytest

from src.services.division import add_new_position_service, change_position_sevice, check_ceo_exist
from tests.fakes import TEST_CHANGE_POSITION_PARAMS, fake_new_position_schema


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
        new_pos = await change_position_sevice(data=data, position_id=pos_id, token=fake_token)
        assert new_pos == True
