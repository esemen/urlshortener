# Generated by Django 3.2.3 on 2021-05-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapi', '0012_alter_urls_shorturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='longUrl',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
