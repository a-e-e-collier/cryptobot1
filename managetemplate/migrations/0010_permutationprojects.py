# Generated by Django 2.2.4 on 2020-09-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetemplate', '0009_variablecondition_variable_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermutationProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
