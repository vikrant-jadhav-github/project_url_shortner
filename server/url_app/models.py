from django.db import models

class UrlModel(models.Model):
    url = models.CharField(max_length=255)
    uuid = models.CharField(max_length=5)
    visitors = models.ForeignKey('account_app.VisitorModel', on_delete=models.CASCADE, related_name='visitors')

    def __str__(self):
        return self.url
