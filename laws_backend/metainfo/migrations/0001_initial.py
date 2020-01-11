# Generated by Django 3.0.2 on 2020-01-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTemplate',
            fields=[
                ('type', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
                ('description', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('last_update_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ErrorDescription',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('last_update_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name=20)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('manual_guide', models.CharField(max_length=255)),
                ('last_update_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('setting_key', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('setting_value', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=10)),
                ('editable', models.BinaryField(verbose_name=1)),
                ('last_update_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SystemMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_message_id', models.BigIntegerField(verbose_name=20)),
                ('content', models.CharField(max_length=255)),
                ('last_update_time', models.DateTimeField()),
            ],
        ),
    ]
