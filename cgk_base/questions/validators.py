import os
from mimetypes import MimeTypes

from django.core.exceptions import ValidationError


def validate_is_audio(file):
    _valid_mime_types = {
        ".mp3": "audio/mpeg",
        ".wav": "audio/x-wav",
    }
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in _valid_mime_types.keys():
        raise ValidationError("Unacceptable file extension.")
    file_type = MimeTypes().guess_type(file)[0]
    if file_type == _valid_mime_types[ext]:
        raise ValidationError("Invalid file type.")
    return
