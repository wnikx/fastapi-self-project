import datetime
from typing import Annotated

from sqlalchemy import Integer, mapped_column, text

# pk
int_pk = Annotated[int, mapped_column(Integer, primary_key=True)]


# datetime
created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    ),
]
