import pytest

from src.services.registration import (
    add_account_with_invite_token,
    check_free_email,
    check_position,
    check_role,
    check_validation,
    email_free,
    finalize_registration,
)
from tests.fakes import (
    TEST_CHECK_EMAIL_FREE_PARAMS,
    TEST_EMAIL_FREE_PARAMS,
    fake_check_validation_data,
    fake_email_schemas,
    fake_users_schemas,
    yes_success,
)


@pytest.mark.parametrize("data, expected_result", TEST_CHECK_EMAIL_FREE_PARAMS)
async def test_check_free_email(data, expected_result, add_account, delete_all_the_accounts):
    await add_account()

    result = await check_free_email(data)
    assert result == expected_result

    await delete_all_the_accounts()


@pytest.mark.parametrize("data, expected_result", TEST_EMAIL_FREE_PARAMS)
async def test_email_free(data, expected_result, add_account, delete_all_the_accounts):
    await add_account()

    result = await email_free(data)
    assert result == expected_result

    await delete_all_the_accounts()


async def test_add_account_with_invite_token(check_invite_row, delete_all_the_invites):
    await add_account_with_invite_token(
        fake_email_schemas[0],
        "invite_token",
    )
    is_success = await check_invite_row()
    assert is_success == yes_success

    await delete_all_the_invites()


async def test_check_validation(check_invite_row, delete_all_the_invites, add_invite_row):
    await add_invite_row()

    added_row = await check_validation(fake_check_validation_data)
    result_row = (added_row.email, added_row.invite_token)
    fake_row = await check_invite_row()
    assert result_row == fake_row

    await delete_all_the_invites()


async def test_check_position(add_position_and_role, delete_all_position_and_role):
    await add_position_and_role()

    position_id = await check_position()
    assert position_id == 1
    await delete_all_position_and_role()

    new_position_id = await check_position()
    assert new_position_id == 1
    await delete_all_position_and_role()


async def test_check_role(add_position_and_role, delete_all_position_and_role):
    await add_position_and_role()

    role_id = await check_role()
    assert role_id == 2
    await delete_all_position_and_role()

    role_id = await check_role()
    assert role_id == 1
    await delete_all_position_and_role()


async def test_finalize_registration(add_position_and_role, delete_all_position_and_role):
    await add_position_and_role()

    row_added = await finalize_registration(fake_users_schemas[0])
    assert bool(row_added) == True

    await delete_all_position_and_role()
