# Generated by Django 2.2.4 on 2020-08-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetemplate', '0005_auto_20200611_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariableCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_excel_for_fulfill', models.BooleanField()),
                ('text_for_fulfill', models.CharField(max_length=1000)),
                ('use_excel_for_not_fulfill', models.BooleanField()),
                ('text_for_not_fulfill', models.CharField(max_length=1000)),
            ],
        ),
    ]
