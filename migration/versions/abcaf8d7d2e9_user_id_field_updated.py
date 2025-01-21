"""User id field updated

Revision ID: abcaf8d7d2e9
Revises: 8809ff7e0f84
Create Date: 2024-12-09 15:13:11.162508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abcaf8d7d2e9'
down_revision: Union[str, None] = '8809ff7e0f84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
