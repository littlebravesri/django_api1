# Generated by Django 3.0.8 on 2020-07-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analysis', '0002_delete_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlation', models.TextField(max_length=40)),
            ],
        ),
    ]
