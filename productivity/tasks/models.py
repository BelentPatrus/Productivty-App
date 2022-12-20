from django.db import models


class task(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.id
