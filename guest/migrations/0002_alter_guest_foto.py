# Generated by Django 5.0.3 on 2024-03-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='foto',
            field=models.ImageField(default=False, null=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]