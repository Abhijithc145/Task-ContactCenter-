# Generated by Django 4.1.1 on 2022-10-14 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_organizations_deleted_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Organizations',
            new_name='Organization',
        ),
    ]