"""add phone number to users

Revision ID: 0dd8d9b3df28

Revises: 001_initial

Create Date: 2026-08-21 11:30:16.154138
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0dd8d9b3df28"
down_revision: Union[str, Sequence[str], None] = "001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("phone_no", sa.String(length=15), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("users", "phone_no")