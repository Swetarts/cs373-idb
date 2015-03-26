"""empty message

Revision ID: 4217c51d1d6
Revises: 379284c3107
Create Date: 2015-03-26 21:09:50.241225

"""

# revision identifiers, used by Alembic.
revision = '4217c51d1d6'
down_revision = '379284c3107'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=4000), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('job_title', sa.String(length=4000), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('gender', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publisher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('alias', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=4000), nullable=True),
    sa.Column('description', sa.String(length=400000), nullable=True),
    sa.Column('gender', sa.String(length=255), nullable=True),
    sa.Column('origin', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('power',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comic_series',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=4000), nullable=True),
    sa.Column('launch_date', sa.DateTime(), nullable=True),
    sa.Column('publisher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character_team',
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], )
    )
    op.create_table('character_creator',
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['creator_id'], ['person.id'], )
    )
    op.create_table('character_enemy',
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('enemy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['enemy_id'], ['character.id'], )
    )
    op.create_table('character_powers',
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['power.id'], )
    )
    op.create_table('character_ally',
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('ally_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ally_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], )
    )
    op.create_table('comic_person',
    sa.Column('comic_id', sa.Integer(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comic_id'], ['comic_series.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], )
    )
    op.create_table('comic_characters',
    sa.Column('comic_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['comic_id'], ['comic_series.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comic_characters')
    op.drop_table('comic_person')
    op.drop_table('character_ally')
    op.drop_table('character_powers')
    op.drop_table('character_enemy')
    op.drop_table('character_creator')
    op.drop_table('character_team')
    op.drop_table('comic_series')
    op.drop_table('power')
    op.drop_table('team')
    op.drop_table('character')
    op.drop_table('publisher')
    op.drop_table('person')
    ### end Alembic commands ###
