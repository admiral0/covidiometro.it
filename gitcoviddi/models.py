from django.db import models
from django.utils.translation import gettext_lazy as _


class GitUpdate(models.Model):
    timestamp = models.DateTimeField('update time')
    commit_id = models.CharField(max_length=256, unique=True)

    class Meta:
        verbose_name = _('gitcoviddi update')
        verbose_name_plural = _('gitcoviddi updates')

    def __str__(self):
        return self.commit_id + " from " + str(self.timestamp)


class ItalyCovidState(models.Model):
    timestamp = models.DateTimeField('measurement date')
    # TODO: add fields
