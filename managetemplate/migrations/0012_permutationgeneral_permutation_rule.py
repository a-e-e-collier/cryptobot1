# Generated by Django 2.2.4 on 2020-09-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetemplate', '0011_permutationgeneral_permutationparagraphs'),
    ]

    operations = [
        migrations.AddField(
            model_name='permutationgeneral',
            name='permutation_rule',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
