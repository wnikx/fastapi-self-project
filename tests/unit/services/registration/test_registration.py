import pytest

from src.services.registration import check_free_email, email_free
from tests.fakes import TEST_CHECK_EMAIL_FREE_PARAMS, TEST_EMAIL_FREE_PARAMS


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
