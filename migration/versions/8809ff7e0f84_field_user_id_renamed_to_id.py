"""field user_id renamed to id

Revision ID: 8809ff7e0f84
Revises: cd68bca2ab29
Create Date: 2024-12-09 10:00:31.517225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8809ff7e0f84'
down_revision: Union[str, None] = 'cd68bca2ab29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.BigInteger(), nullable=False))
    op.drop_column('users', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=False))
    op.drop_column('users', 'id')
    # ### end Alembic commands ###
