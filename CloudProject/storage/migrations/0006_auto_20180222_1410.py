# Generated by Django 2.0.2 on 2018-02-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_auto_20180222_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerec',
            name='type',
            field=models.CharField(choices=[('U', 'upload'), ('D', 'download'), ('R', 'delete')], default='D', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='share_opt',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]