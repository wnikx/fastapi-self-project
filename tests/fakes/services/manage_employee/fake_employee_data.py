from src.schemas.employee import AddNewEmployeeSchema
from src.schemas.registration import SignUpSchema

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
