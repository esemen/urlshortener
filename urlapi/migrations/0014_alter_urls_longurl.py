# Generated by Django 3.2.3 on 2021-05-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapi', '0013_alter_urls_longurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='longUrl',
            field=models.CharField(max_length=255),
        ),
    ]