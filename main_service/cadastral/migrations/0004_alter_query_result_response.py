# Generated by Django 4.2 on 2023-09-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastral', '0003_alter_query_time_came_alter_query_time_went'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='result_response',
            field=models.BooleanField(blank=True, help_text='Ответ внешнего сервера', null=True, verbose_name='Ответ'),
        ),
    ]
