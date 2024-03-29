# Generated by Django 4.2.5 on 2023-12-13 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_book_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='img/author/')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(blank=True, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('time', models.FloatField(blank=True, null=True)),
                ('storage', models.FloatField(blank=True, null=True)),
                ('like_tahririyat', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BDe',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='img/books/'),
        ),
        migrations.AddField(
            model_name='bookdetail',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(blank=True, to='main.book'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.bookcategory'),
            preserve_default=False,
        ),
    ]
