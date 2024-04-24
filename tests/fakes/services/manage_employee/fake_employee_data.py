from src.schemas.employee import AddNewEmployeeSchema

test_employee_schema = AddNewEmployeeSchema(
    email="test@mail.com",
    first_name="test",
    last_name="test",
    position="test",
)
fake_data_for_token = {"email": "test@gmail.ru", "role": "admin"}
