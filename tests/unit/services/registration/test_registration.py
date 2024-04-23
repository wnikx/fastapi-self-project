import pytest

from src.schemas.registration import CheckEmailSchema
from src.services.registration import check_free_email
from tests.fakes import TEST_CHECK_EMAIL_FREE_PARAMS


@pytest.mark.parametrize("data, expected_result, expectation", TEST_CHECK_EMAIL_FREE_PARAMS)
async def test_check_free_email(data, expected_result, expectation):
    await add_account(async_session_maker)

    result = await check_free_email(CheckEmailSchema(email=data))

    assert result == expected_result
