# Generated by Django 2.0.2 on 2018-02-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0008_auto_20180226_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='file',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='id',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='share_opt',
            field=models.BooleanField(default=0, primary_key='False', serialize=False),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Share',
        ),
    ]
