import os
import datetime
from celery import shared_task
from django.conf import settings


@shared_task
def delete_old_media_files():
    media_root = settings.MEDIA_ROOT
    target_folder = os.path.join(media_root, 'checks/')
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(minutes=1)

    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_modified_time < cutoff:
                os.remove(file_path)
                print(f'Deleted {file_path}')
