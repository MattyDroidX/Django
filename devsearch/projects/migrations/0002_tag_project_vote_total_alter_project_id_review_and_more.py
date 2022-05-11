# Generated by Django 4.0.4 on 2022-05-08 16:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.UUID('87035659-52d0-4a85-b794-0b37c8c07ff8'), editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('da6eb554-a0e7-448f-930a-65010c8f270e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.CharField(max_length=200)),
                ('value', models.CharField(choices=[('up', 'up vote'), ('down', 'down vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.UUID('409ec789-331f-4aa6-901b-67e2e16e4f4c'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.tag'),
        ),
    ]
