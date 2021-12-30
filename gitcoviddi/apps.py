from django.apps import AppConfig
from .tasks import update_repository


class GitcoviddiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gitcoviddi'

    def ready(self):
        update_repository.delay()
