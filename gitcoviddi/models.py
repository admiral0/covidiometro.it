from django.db import models


class GitUpdate(models.Model):
    timestamp = models.DateTimeField('update time')
    commit_id = models.CharField(max_length=256)


class ItalyCovidState(models.Model):
    timestamp = models.DateTimeField('measurement date')
    # TODO: add fields
