# Generated by Django 4.1.1 on 2022-10-14 16:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_bot_model_channel_model_agent_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversations_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sender_id', models.PositiveIntegerField(blank=True, null=True)),
                ('sender_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.CharField(max_length=100, null=True)),
                ('Channel', models.CharField(max_length=100)),
                ('agent', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('Bot_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.bot_model')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile_Module',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sender_id', models.PositiveIntegerField(blank=True, null=True)),
                ('Channel', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.CharField(max_length=100, null=True)),
                ('option', models.BooleanField(default=True)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Message_Module',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sender_id', models.PositiveIntegerField(blank=True, null=True)),
                ('Channel', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.CharField(max_length=100, null=True)),
                ('autor', models.CharField(max_length=100)),
                ('autor_type', models.CharField(choices=[('user', 'user'), ('agent', 'agent')], default='user', max_length=10)),
                ('conversation_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.conversations_model')),
            ],
        ),
    ]