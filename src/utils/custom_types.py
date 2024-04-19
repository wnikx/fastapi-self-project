import datetime
from typing import Annotated

from sqlalchemy import Integer, String, text
from sqlalchemy.orm import mapped_column

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

# varchar
str_256 = Annotated[str, mapped_column(String(length=256))]
