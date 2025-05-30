"""Change cctv_info location to type

Revision ID: bbe4fc7674a5
Revises: 977c58ffc4cc
Create Date: 2025-02-25 21:50:24.927448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbe4fc7674a5'
down_revision: Union[str, None] = '977c58ffc4cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cctv_info', sa.Column('type', sa.String(length=20), nullable=True))
    op.drop_column('cctv_info', 'location')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cctv_info', sa.Column('location', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('cctv_info', 'type')
    # ### end Alembic commands ###
