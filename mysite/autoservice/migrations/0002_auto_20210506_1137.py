# Generated by Django 3.2.1 on 2021-05-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
