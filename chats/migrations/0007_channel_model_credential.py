# Generated by Django 4.1.1 on 2022-10-15 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_alter_conversations_model_sender_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel_model',
            name='credential',
            field=models.JSONField(default=dict, verbose_name='json'),
        ),
    ]
