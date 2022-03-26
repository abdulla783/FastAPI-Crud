

import sqlalchemy
metadata = sqlalchemy.MetaData()
from database import Base


address_ = sqlalchemy.Table(
    "address",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("address", sqlalchemy.String),
    sqlalchemy.Column("longitude", sqlalchemy.String),
    sqlalchemy.Column("latitude", sqlalchemy.String),
    sqlalchemy.Column("is_published", sqlalchemy.Boolean),
    # sqlalchemy.Column("created", sqlalchemy.DateTime),
    # sqlalchemy.Column("updated", sqlalchemy.DateTime),
)
