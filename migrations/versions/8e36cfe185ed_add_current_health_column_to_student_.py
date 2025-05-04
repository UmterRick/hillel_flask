from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8e36cfe185ed"
down_revision = "e1fcf6d13299"
branch_labels = None
depends_on = None


def upgrade():
    # Добавляем новые колонки
    op.add_column("students", sa.Column("course_name", sa.String(), nullable=True))
    op.add_column("students", sa.Column("photo_url", sa.String(), nullable=True))
    op.add_column(
        "students",
        sa.Column("current_health", sa.Integer(), default=100, nullable=True),
    )


def downgrade():
    # Удаляем добавленные колонки
    op.drop_column("students", "course_name")
    op.drop_column("students", "photo_url")
    op.drop_column("students", "current_health")
