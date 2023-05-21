"""
Initial

Revision ID: 11a4a30ddff3
Revises: 
Create Date: 2023-05-18 15:56:29.682606

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '11a4a30ddff3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AppealStatuses',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('Name', sa.VARCHAR(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='Appeals'
                    )
    op.create_table('Departments',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('Name', sa.VARCHAR(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='People'
                    )
    op.create_table('Roles',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('Name', sa.VARCHAR(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='People'
                    )
    op.create_table('TicketCategories',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('Name', sa.VARCHAR(length=100), nullable=False),
                    sa.Column('UpdateDateTime', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='Tickets'
                    )
    op.create_table('Users',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('Name', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('Surname', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('PhoneNumber', sa.Integer(), nullable=False),
                    sa.Column('TelegramChatID', sa.BIGINT(), nullable=False),
                    sa.Column('Role_ID', sa.Integer(), nullable=False),
                    sa.Column('IsActive', sa.Boolean(), nullable=False),
                    sa.ForeignKeyConstraint(['Role_ID'], ['People.Roles.ID'], ),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='People'
                    )
    op.create_table('TicketCategoryProperties',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('UpdateDateTime', sa.DateTime(), nullable=False),
                    sa.Column('TicketCategory_ID', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['TicketCategory_ID'], ['Tickets.TicketCategories.ID'], ),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='Tickets'
                    )
    op.create_table('Appeals',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('DateTime', sa.DateTime(), nullable=False),
                    sa.Column('User_ID', sa.Integer(), nullable=False),
                    sa.Column('AppealStatus_ID', sa.Integer(), nullable=False),
                    sa.Column('Text', sa.VARCHAR(), nullable=True),
                    sa.Column('MediaID', sa.Integer(), nullable=True),
                    sa.Column('Departament_ID', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['AppealStatus_ID'], ['Appeals.AppealStatuses.ID'], ),
                    sa.ForeignKeyConstraint(['Departament_ID'], ['People.Departments.ID'], ),
                    sa.ForeignKeyConstraint(['User_ID'], ['People.Users.ID'], ),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='Appeals'
                    )
    op.create_table('ProcessedMessages',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('DateTime', sa.DateTime(), nullable=False),
                    sa.Column('User_ID', sa.Integer(), nullable=False),
                    sa.Column('TelegramMessageID', sa.Integer(), nullable=False),
                    sa.Column('MessageData', sa.VARCHAR(), nullable=True),
                    sa.Column('Appeal_ID', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['Appeal_ID'], ['Appeals.Appeals.ID'], ),
                    sa.ForeignKeyConstraint(['User_ID'], ['People.Users.ID'], ),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='Appeals'
                    )
    op.create_table('Tickets',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('DateTime', sa.DateTime(), nullable=False),
                    sa.Column('User_ID', sa.Integer(), nullable=False),
                    sa.Column('Appeal_ID', sa.Integer(), nullable=False),
                    sa.Column('TicketCategory_ID', sa.Integer(), nullable=False),
                    sa.Column('Responsible_ID', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['Appeal_ID'], ['Appeals.Appeals.ID'], ),
                    sa.ForeignKeyConstraint(['TicketCategory_ID'], ['Tickets.TicketCategories.ID'], ),
                    sa.ForeignKeyConstraint(['User_ID'], ['People.Users.ID'], ),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='Tickets'
                    )
    op.create_table('TicketCategoryPropertyValues',
                    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('UpdateDateTime', sa.DateTime(), nullable=False),
                    sa.Column('Ticket_ID', sa.Integer(), nullable=False),
                    sa.Column('TicketCategoryProperty_ID', sa.Integer(), nullable=False),
                    sa.Column('Value', sa.VARCHAR(), nullable=False),
                    sa.ForeignKeyConstraint(['TicketCategoryProperty_ID'], ['Tickets.TicketCategoryProperties.ID'], ),
                    sa.ForeignKeyConstraint(['Ticket_ID'], ['Tickets.Tickets.ID'], ),
                    sa.PrimaryKeyConstraint('ID'),
                    sa.UniqueConstraint('ID'),
                    schema='Tickets'
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TicketCategoryPropertyValues', schema='Tickets')
    op.drop_table('Tickets', schema='Tickets')
    op.drop_table('ProcessedMessages', schema='Appeals')
    op.drop_table('Appeals', schema='Appeals')
    op.drop_table('TicketCategoryProperties', schema='Tickets')
    op.drop_table('Users', schema='People')
    op.drop_table('TicketCategories', schema='Tickets')
    op.drop_table('Roles', schema='People')
    op.drop_table('Departments', schema='People')
    op.drop_table('AppealStatuses', schema='Appeals')
    # ### end Alembic commands ###
