from fakes.services.manage_employee.fake_employee_data import (
    fake_check_email_schema,
    fake_data_for_token,
    fake_email,
    fake_new_name_schema,
    fake_sign_up_schema,
    fake_token,
    test_employee_schema,
)
from fakes.services.registration.fake_registration import (
    TEST_CHECK_EMAIL_FREE_PARAMS,
    TEST_EMAIL_FREE_PARAMS,
    fake_check_validation_data,
    fake_data_for_invite_row,
    fake_email_schemas,
    yes_success,
)
from fakes.services.registration.fake_user import fake_users_schemas
from fakes.services.task.fake_task_data import fake_task_schema
from fakes.services.verify.verify_fake_data import fake_company, fake_login_schema, fake_user
from tests.fakes.services.division.fake_division_data import (
    TEST_ADD_SUPERVISOR_SERVICE,
    TEST_CHANGE_DIVISION_NAME_SERVICE_PARAMS,
    TEST_CHANGE_POSITION_PARAMS,
    TEST_DELETE_DIVISION_PARAMS,
    TEST_DELETE_POSITION_PARAMS,
    fake_new_position_schema,
)

__all__ = [
    "fake_email_schemas",
    "TEST_CHECK_EMAIL_FREE_PARAMS",
    "TEST_EMAIL_FREE_PARAMS",
    "fake_data_for_invite_row",
    "yes_success",
    "fake_check_validation_data",
    "fake_users_schemas",
    "fake_user",
    "fake_company",
    "fake_login_schema",
    "test_employee_schema",
    "fake_data_for_token",
    "fake_sign_up_schema",
    "fake_token",
    "fake_email",
    "fake_check_email_schema",
    "fake_new_name_schema",
    "fake_task_schema",
    "fake_new_position_schema",
    "TEST_CHANGE_POSITION_PARAMS",
    "TEST_DELETE_POSITION_PARAMS",
    "TEST_CHANGE_DIVISION_NAME_SERVICE_PARAMS",
    "TEST_ADD_SUPERVISOR_SERVICE",
    "TEST_DELETE_DIVISION_PARAMS",
]
