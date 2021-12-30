from django.db import migrations, models


def create_update_repo_task(apps, schema_editor):
    IntervalSchedule = apps.get_model('django_celery_beat', 'IntervalSchedule')
    PeriodicTask = apps.get_model('django_celery_beat', 'PeriodicTask')

    every_15_m = IntervalSchedule()
    every_15_m.every = 15
    every_15_m.period = 'minutes'
    every_15_m.save()

    update_git = PeriodicTask(
        name="update-gitcoviddi",
        task='gitcoviddi.tasks.update_repository',
        interval=every_15_m,
        description="""This is the entry point of gitcoviddi app. 
        It pulls the official git repo and saves data."""
    )
    update_git.save()


def remove_update_repo_task(apps, schema_editor):
    PeriodicTask = apps.get_model('django_celery_beat', 'PeriodicTask')

    PeriodicTask.objects.get(name='update-gitcoviddi').delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='update time')),
                ('commit_id', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItalyCovidState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='measurement date')),
            ],
        ),
        migrations.RunPython(create_update_repo_task, reverse_code=remove_update_repo_task)
    ]
