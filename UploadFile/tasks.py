import os
from background_task import background
from django.core.files.storage import default_storage
from .models import Upload

# The 'schedule' parameter defaults to 0 (run immediately), 
# but we will override it when calling the function in the view.
@background(schedule=0) 
def delete_upload_data(upload_id):
    """
    Deletes the Upload object and its associated media files.
    """
    try:
        upload = Upload.objects.get(id=upload_id)
        
        # 1. Delete the associated files from storage (important!)
        if upload.original_image:
            # We use default_storage.delete() and the .name attribute for proper file cleanup.
            default_storage.delete(upload.original_image.name) 
        if upload.generated_audio:
            default_storage.delete(upload.generated_audio.name)
        
        # 2. Delete the database record
        upload.delete()
        
    except Upload.DoesNotExist:
        # The object might have been deleted by an administrator or another process
        pass