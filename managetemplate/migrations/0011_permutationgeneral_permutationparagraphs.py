# Generated by Django 2.2.4 on 2020-09-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetemplate', '0010_permutationprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermutationGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('update_status', models.BooleanField()),
                ('apply_to_all_para', models.BooleanField()),
                ('min_ele_to_keep', models.IntegerField()),
                ('max_ele_to_keep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PermutationParagraphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('section_name', models.CharField(max_length=100)),
                ('section_visibility', models.BooleanField()),
                ('paragraph_type', models.CharField(max_length=100)),
                ('number_of_elements', models.IntegerField()),
                ('permutation_rule', models.CharField(max_length=100)),
                ('min_ele_to_keep', models.IntegerField()),
                ('max_ele_to_keep', models.IntegerField()),
            ],
        ),
    ]
