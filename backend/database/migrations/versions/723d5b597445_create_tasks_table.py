"""create_tasks_table

Revision ID: 723d5b597445
Revises: 94d9daf7fc5f
Create Date: 2023-11-12 16:26:12.683782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '723d5b597445'
down_revision: Union[str, None] = '94d9daf7fc5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'task',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('user.id', name="task_user_id_fkey", ondelete="CASCADE"), nullable=True),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('memo', sa.Text(length=1000), nullable=True),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('finish_date', sa.Date(), nullable=False),
        sa.Column('is_check', sa.Boolean(), nullable=False, default=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    with op.batch_alter_table('task') as batch_op:
        batch_op.drop_constraint('task_user_id_fkey', type_='foreignkey')

    op.drop_table('task')
