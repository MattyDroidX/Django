# Generated by Django 4.0.4 on 2022-05-17 15:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_owner_alter_project_id_alter_review_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a1afe56a-ef5e-4edb-af44-5807045b0944'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0af58dc8-fabc-454b-8b4d-1f1338cc22a9'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ac6087a2-7495-4040-8309-e8872e0180d0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
