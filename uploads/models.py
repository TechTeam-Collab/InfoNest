import os
import mimetypes
from django.db import models
from account.models import Account

def file_type_directory(instance, filename):
    """
    Determine the directory based on the file type.
    """
    # Get the file extension
    file_extension = os.path.splitext(filename)[1].lower()

    # Map file extensions to file types
    file_type_mapping = {
        '.jpg': 'images',
        '.jpeg': 'images',
        '.png': 'images',
        '.gif': 'images',
        '.pdf': 'documents',
        '.doc': 'documents',
        '.docx': 'documents',
        '.xls': 'documents',
        '.xlsx': 'documents',
        '.mp4': 'videos',
        '.avi': 'videos',
        '.mov': 'videos',
    }

    # Default to 'others' if the file type is not recognized
    file_type = file_type_mapping.get(file_extension, 'others')

    # Return the directory path
    return f'uploads/{file_type}/{filename}'

class UserUpload(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)  # Associate upload with a user
    file = models.FileField(upload_to=file_type_directory)  # Use the custom directory function
    description = models.TextField(blank=True, null=True)  # Optional description of the file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the file was uploaded

    def __str__(self):
        return f"{self.user.email} - {self.file.name}"