from sqlalchemy import MetaData, Integer, String, Table, TIMESTAMP, ForeignKey, Column, JSON, Boolean
import datetime

metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column('username', String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)
