# Generated by Django 3.0.5 on 2021-05-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20210504_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
