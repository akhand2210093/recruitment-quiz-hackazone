# Generated by Django 5.1 on 2024-08-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_user_student_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='answer',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='answer_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
