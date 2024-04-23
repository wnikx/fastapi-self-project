import pytest

from src.schemas.registration import CheckEmailSchema
from src.services.registration import check_free_email
from tests.fakes import TEST_CHECK_EMAIL_FREE_PARAMS


@pytest.mark.parametrize("data, expected_result", TEST_CHECK_EMAIL_FREE_PARAMS)
async def test_check_free_email(data, expected_result, add_account):
    await add_account()
    result = await check_free_email(data)
    assert result == expected_result
