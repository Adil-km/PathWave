import os
from django.core.management.base import BaseCommand
from UploadFile.models import Upload
from django.core.files.storage import default_storage

class Command(BaseCommand):
    help = 'Deletes all records and associated media files from the Upload model.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Starting cold start cleanup...'))
        
        # 1. Delete associated media files first
        for upload in Upload.objects.all():
            # Delete image file
            if upload.original_image:
                default_storage.delete(upload.original_image.name)
            
            # Delete audio file
            if upload.generated_audio:
                default_storage.delete(upload.generated_audio.name)

        # 2. Delete all database records
        count, _ = Upload.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} Upload records and their media files.'))