# Generated by Django 2.1.5 on 2020-07-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200709_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=models.TextField(),
        ),
    ]
