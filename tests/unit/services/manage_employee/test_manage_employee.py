from src.services.manage_employee import (
    add_new_employee_service,
    check_token,
    update_email,
    update_name,
)
from tests.fakes import (
    fake_check_email_schema,
    fake_email,
    fake_new_name_schema,
    fake_token,
    test_employee_schema,
)


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
    assert result == True

    await delete_user()
    await delete_all_position_and_role()
    await delete_company()


async def test_check_token(add_invite_token, delete_invite_token):
    await add_invite_token()

    email = await check_token(fake_token)
    assert email == fake_email

    await delete_invite_token()


async def test_update_email(
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

    result = await update_email(fake_check_email_schema, fake_token)
    assert result == True

    await delete_user()
    await delete_all_position_and_role()
    await delete_company()


async def test_update_name(
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

    result = await update_name(fake_new_name_schema, fake_token)
    assert result == True

    await delete_user()
    await delete_all_position_and_role()
    await delete_company()
