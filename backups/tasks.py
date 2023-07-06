from os import path
import shutil

from django.utils import timezone
from django.apps import apps

from apscheduler.schedulers.background import BackgroundScheduler

from taxi.settings import DATABASES


def create_db_backup():
    db = DATABASES["default"]["NAME"]
    app_path = apps.get_app_config("backups").path
    backup_folder_name = "db_backups"

    backup_name = f"{timezone.now().date()}.bak"

    backup_path = path.join(app_path, backup_folder_name, backup_name)
    shutil.copy2(db, backup_path)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(create_db_backup, "interval", weeks=1)
    scheduler.start()
