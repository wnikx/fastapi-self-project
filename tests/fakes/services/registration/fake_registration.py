from src.schemas.registration import CheckEmailSchema

fake_email_schemas = [CheckEmailSchema(email="fake@test.com")]

# data, expected_result, expectation
TEST_CHECK_EMAIL_FREE_PARAMS = [
    (fake_email_schemas[0], False),
    (CheckEmailSchema(email="fake_1@test.com"), True),
]

# data, expected_result, expectation
TEST_EMAIL_FREE_PARAMS = [
    (fake_email_schemas[0], False),
    (CheckEmailSchema(email="fake_1@test.com"), True),
]

fake_data_for_invite_row = {"email": fake_email_schemas[0].email, "invite_token": "invite_token"}
yes_success = ("fake@test.com", "invite_token")
