from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)

    def serialize_task(self):
        return {
            "title": self.title,
            "body": self.body,
        }