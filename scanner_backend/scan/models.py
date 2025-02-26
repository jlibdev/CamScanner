from django.db import models

class ScannedDocument(models.Model):
    image = models.ImageField(upload_to="scanned/")
    processed_image = models.ImageField(upload_to=("proccessed/"))
