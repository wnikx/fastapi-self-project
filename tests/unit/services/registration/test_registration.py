import pytest

from src.services.registration import add_account_with_invite_token, check_free_email, email_free
from tests.fakes import (
    TEST_CHECK_EMAIL_FREE_PARAMS,
    TEST_EMAIL_FREE_PARAMS,
    fake_email_schemas,
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
