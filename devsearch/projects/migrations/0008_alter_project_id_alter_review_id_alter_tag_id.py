# Generated by Django 4.0.4 on 2022-05-12 22:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_feature_image_alter_project_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e6cf05d3-0f67-491d-8cb2-1efd2b64a069'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('219626dc-0aac-43c2-99af-5df5f3963d06'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.UUID('79533712-aee8-44be-a6c1-ab8c4b56cb35'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
