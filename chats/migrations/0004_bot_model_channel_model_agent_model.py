# Generated by Django 4.1.1 on 2022-10-14 12:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_rename_organizations_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.CharField(max_length=100, null=True)),
                ('organization_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Channel_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.CharField(max_length=100, null=True)),
                ('Bot_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.bot_model')),
            ],
        ),
        migrations.CreateModel(
            name='Agent_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.CharField(max_length=100, null=True)),
                ('department_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.department')),
            ],
        ),
    ]