# Generated by Django 5.0.6 on 2024-05-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('grades', models.CharField(max_length=50)),
                ('age', models.FloatField()),
            ],
        ),
    ]
