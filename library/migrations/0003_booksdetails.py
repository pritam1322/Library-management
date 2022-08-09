# Generated by Django 4.0.5 on 2022-07-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.CharField(max_length=64)),
                ('edition', models.CharField(max_length=64)),
                ('ISBN', models.PositiveIntegerField()),
                ('volume', models.IntegerField()),
                ('author', models.CharField(max_length=64)),
                ('available', models.CharField(max_length=4)),
                ('book_name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
    ]