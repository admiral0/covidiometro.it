from celery import shared_task


@shared_task
def update_repository():
    print("hello world")
