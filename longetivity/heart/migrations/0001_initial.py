# Generated by Django 3.2.5 on 2022-01-11 10:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=15)),
                ('profile_picture', models.ImageField(default='static/images/user.jpeg', upload_to='')),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('vote', models.IntegerField(choices=[('+1', 'UPVOTE'), ('-1', 'DOWNVOTE')])),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heart.details')),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='tags',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='heart.tags'),
        ),
    ]
