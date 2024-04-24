from src.services.verify import verify_data
from tests.fakes import fake_login_schema


async def test_verify_data(
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
    result = await verify_data(fake_login_schema)
    assert isinstance(result, str)
    await delete_user()
    await delete_all_position_and_role()
    await delete_company()
