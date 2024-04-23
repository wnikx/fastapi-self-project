from src.schemas.registration import SignUpCompleteSchema

fake_users_schemas = [
    SignUpCompleteSchema(
        email="test@test.com",
        first_name="test",
        last_name="test",
        password="StrongPassword123!",
        company_name="test",
    ),
]
