# Generated by Django 3.2.3 on 2021-05-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urls',
            options={'verbose_name': 'Url', 'verbose_name_plural': 'Urls'},
        ),
        migrations.AlterField(
            model_name='urls',
            name='longUrl',
            field=models.CharField(max_length=255),
        ),
    ]
