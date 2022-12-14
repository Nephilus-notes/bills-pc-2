"""Renewing database, fresh start for pokemon_move

Revision ID: f82aa50ddefe
Revises: 
Create Date: 2022-12-11 22:23:24.682654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f82aa50ddefe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('all_pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('type1', sa.String(length=45), nullable=False),
    sa.Column('type2', sa.String(length=45), nullable=True),
    sa.Column('reg_sprite', sa.String(length=600), nullable=False),
    sa.Column('shiny_sprite', sa.String(length=600), nullable=True),
    sa.Column('ability1', sa.String(length=60), nullable=False),
    sa.Column('ability2', sa.String(length=60), nullable=True),
    sa.Column('ability3', sa.String(length=60), nullable=True),
    sa.Column('has_shiny', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('move',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('effect', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pokemon_move',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('move_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['move_id'], ['move.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['all_pokemon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_move',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('move_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['move_id'], ['move.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('type1', sa.String(length=45), nullable=False),
    sa.Column('type2', sa.String(length=45), nullable=True),
    sa.Column('sprite', sa.String(length=600), nullable=False),
    sa.Column('ability', sa.String(length=60), nullable=False),
    sa.Column('move1', sa.Integer(), nullable=False),
    sa.Column('move2', sa.Integer(), nullable=True),
    sa.Column('move3', sa.Integer(), nullable=True),
    sa.Column('move4', sa.Integer(), nullable=True),
    sa.Column('date_caught', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['move1'], ['move.id'], ),
    sa.ForeignKeyConstraint(['move2'], ['move.id'], ),
    sa.ForeignKeyConstraint(['move3'], ['move.id'], ),
    sa.ForeignKeyConstraint(['move4'], ['move.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['all_pokemon.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_pokemon')
    op.drop_table('user_move')
    op.drop_table('pokemon_move')
    op.drop_table('user')
    op.drop_table('move')
    op.drop_table('all_pokemon')
    # ### end Alembic commands ###
