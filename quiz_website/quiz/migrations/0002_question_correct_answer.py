# Generated by Django 5.1 on 2024-08-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
