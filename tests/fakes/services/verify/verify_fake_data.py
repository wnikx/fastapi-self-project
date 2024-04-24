from src.models import Company, User
from src.schemas.login import LogInSchema
from src.utils.hash_pass import get_password_hash

fake_user = User(
    first_name="test",
    last_name="test",
    hashed_password=get_password_hash("test"),
    email="test@gmail.ru",
    company_id=1,
    position_id=1,
    role_id=1,
)
fake_company = Company(company_name="test")
fake_login_schema = LogInSchema(email="test@gmail.ru", password="test")
