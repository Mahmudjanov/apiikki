# Generated by Django 4.2.5 on 2023-12-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_book_delete_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=255)),
                ('rate', models.IntegerField()),
                ('page', models.IntegerField()),
                ('year', models.DateField()),
                ('about', models.TextField()),
                ('time', models.TimeField()),
                ('mb', models.IntegerField()),
            ],
        ),
    ]
