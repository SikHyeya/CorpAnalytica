# Generated by Django 4.0 on 2023-09-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpanalytica', '0005_corp_total_info_delete_test_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='related_corp',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('corpname', models.CharField(max_length=50)),
                ('related_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'related_corp',
                'managed': False,
            },
        ),
    ]
