# Generated by Django 3.2.3 on 2021-05-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('name', models.CharField(max_length=49, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'banks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('bank_id', models.BigIntegerField(null=True)),
                ('branch', models.CharField(max_length=74, null=True)),
                ('address', models.CharField(max_length=195, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'branches',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Banks',
        ),
        migrations.DeleteModel(
            name='Branches',
        ),
    ]
