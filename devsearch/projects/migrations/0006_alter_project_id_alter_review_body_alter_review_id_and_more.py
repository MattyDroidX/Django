# Generated by Django 4.0.4 on 2022-05-08 21:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_vote_ratio_alter_project_id_alter_review_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f02f2b52-b67d-4e5d-8782-3bd619eaeb81'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dbeb5cff-f4e2-4fed-90ff-442a95531d6c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.UUID('07d40603-4b88-40b9-bdb9-a7b80238d297'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]