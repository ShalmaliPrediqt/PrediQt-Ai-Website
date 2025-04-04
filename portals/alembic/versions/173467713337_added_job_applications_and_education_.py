"""Added job applications and education levels tables

Revision ID: 173467713337
Revises: 69a2a34c1fff
Create Date: 2025-03-25 14:30:30.715508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '173467713337'
down_revision: Union[str, None] = '69a2a34c1fff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_contact_form_email_address', table_name='contact_form')
    op.drop_index('ix_contact_form_full_name', table_name='contact_form')
    op.drop_index('ix_contact_form_id', table_name='contact_form')
    op.drop_table('contact_form')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_form',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email_address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('interest', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('find_us', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='contact_form_pkey')
    )
    op.create_index('ix_contact_form_id', 'contact_form', ['id'], unique=False)
    op.create_index('ix_contact_form_full_name', 'contact_form', ['full_name'], unique=False)
    op.create_index('ix_contact_form_email_address', 'contact_form', ['email_address'], unique=True)
    # ### end Alembic commands ###
