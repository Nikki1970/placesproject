# Generated by Django 3.1.7 on 2021-04-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placesapp', '0003_auto_20210409_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]