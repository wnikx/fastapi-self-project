from src.schemas.employee import AddNewEmployeeSchema, NewNameSchema
from src.schemas.registration import CheckEmailSchema, SignUpSchema

test_employee_schema = AddNewEmployeeSchema(
    email="test@mail.com",
    first_name="test",
    last_name="test",
    position="test",
)
fake_data_for_token = {"email": "test@gmail.ru", "role": "admin"}
fake_sign_up_schema = SignUpSchema(email="test@mail.ru", invite_token="test")
fake_token = fake_sign_up_schema.invite_token
fake_email = fake_sign_up_schema.email
fake_check_email_schema = CheckEmailSchema(email="new@test.com")
fake_new_name_schema = NewNameSchema(first_name="test", last_name="test")
