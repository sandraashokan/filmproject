# Generated by Django 4.2.1 on 2023-05-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
    ]
