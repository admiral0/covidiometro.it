from django.apps import AppConfig


class GitcoviddiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gitcoviddi'

    def ready(self):
        from .tasks import update_repository

        update_repository.delay()
