# Generated by Django 2.2.4 on 2020-09-17 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managetemplate', '0014_auto_20200917_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permutationgeneral',
            old_name='permutation_rule',
            new_name='permutation_mode',
        ),
    ]
