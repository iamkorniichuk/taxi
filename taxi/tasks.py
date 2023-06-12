import shutil
from datetime import timedelta
from django.utils import timezone

from taxi.settings import DATABASES, BASE_DIR
from taxi import celery_app


# TODO: To end
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    month = timedelta(weeks=4)

    sender.add_periodic_task(
        month, create_db_backup.s(),
        name='monthly_backup'
    )


@celery_app.task
def create_db_backup():
    db = DATABASES['default']['NAME']
    ext = db.suffix
    shutil.copy2(db, BASE_DIR / f'backups/{timezone.now().date()}{ext}')
