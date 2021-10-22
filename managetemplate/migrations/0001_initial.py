# Generated by Django 2.2.7 on 2019-12-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_id', models.CharField(max_length=100)),
                ('condition_content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConversionRule',
            fields=[
                ('no', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srcpattern', models.CharField(max_length=100)),
                ('destpattern', models.CharField(max_length=100)),
                ('enabled', models.BooleanField()),
                ('case_sensitive', models.BooleanField()),
                ('exceptions', models.CharField(max_length=100)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VariableFields',
            fields=[
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]