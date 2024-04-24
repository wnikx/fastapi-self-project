from src.services.manage_employee import add_new_employee_service
from tests.fakes import test_employee_schema


async def test_add_new_employee_service(
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
    result = await add_new_employee_service(test_employee_schema, fake_token)
    await delete_user()
    await delete_all_position_and_role()
    await delete_company()
    assert result == True
