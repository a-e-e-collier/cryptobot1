# Generated by Django 2.2.4 on 2020-10-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetemplate', '0015_auto_20200917_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='permutationparagraphs',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
