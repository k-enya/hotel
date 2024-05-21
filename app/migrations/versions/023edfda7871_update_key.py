"""update key

Revision ID: 023edfda7871
Revises: 5a36f2733c0f
Create Date: 2024-05-17 12:26:08.615618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '023edfda7871'
down_revision: Union[str, None] = '5a36f2733c0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rooms', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rooms', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
