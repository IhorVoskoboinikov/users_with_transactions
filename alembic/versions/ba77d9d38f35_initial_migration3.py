"""initial migration3

Revision ID: ba77d9d38f35
Revises: 263f3e0a5088
Create Date: 2024-09-25 21:16:36.083608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba77d9d38f35'
down_revision: Union[str, None] = '263f3e0a5088'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'transactions',  # Имя таблицы
        'transaction_amount',  # Имя поля
        type_=sa.Float(),
        postgresql_using='transaction_amount::float'
    )


def downgrade() -> None:
    op.alter_column(
        'transactions',
        'transaction_amount',
        type_=sa.String(255),
        postgresql_using='transaction_amount::text'
    )
