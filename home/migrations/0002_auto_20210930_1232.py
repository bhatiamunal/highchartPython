# Generated by Django 3.2.7 on 2021-09-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('dob', models.TextField()),
                ('mob', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=122)),
            ],
        ),
        migrations.DeleteModel(
            name='database',
        ),
    ]
