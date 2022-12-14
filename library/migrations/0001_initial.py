# Generated by Django 4.0.5 on 2022-07-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=64)),
                ('full_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email_id', models.CharField(max_length=64)),
                ('mobile_number', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
            ],
        ),
    ]
