# Generated by Django 2.1.5 on 2019-02-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=100)),
                ('created_at', models.CharField(max_length=50)),
            ],
        ),
    ]