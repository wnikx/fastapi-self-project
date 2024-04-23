from contextlib import nullcontext as does_not_raise

from src.schemas.registration import CheckEmailSchema

fake_email_schemas = [CheckEmailSchema(email="fake@test.com")]

# data, expected_result, expectation
TEST_CHECK_EMAIL_FREE_PARAMS = [
    (fake_email_schemas[0], False, does_not_raise()),
    (CheckEmailSchema(email="fake_1@test.com"), True, does_not_raise()),
]
