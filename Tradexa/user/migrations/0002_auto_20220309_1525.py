# Generated by Django 2.2 on 2022-03-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]