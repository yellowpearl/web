# Generated by Django 3.1 on 2020-08-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='UserName',
        ),
    ]