from src.schemas.task import TaskSchema

fake_task_schema = TaskSchema(
    title="test",
    author_id=1,
    assignee_id=1,
    observers=[1],
    performers=[1],
    deadline="2024-04-24",
    status="To Do",
    estimated_time=1,
)
