# Generated by Django 4.1.3 on 2022-11-21 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_alter_pregunta_id_alter_respuesta_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='survey',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
    ]
