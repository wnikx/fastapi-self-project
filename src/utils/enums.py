import enum


class RoleName(enum.Enum):
    admin = "admin"
    user = "user"
    guest = "guest"


class StatusTask(enum.Enum):
    to_do = "To Do"
    in_progress = "In progress"
    done = "Done"
    closed = "Closed"
