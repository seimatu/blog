# Generated by Django 2.2 on 2019-12-16 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('primaryCategory', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='cat_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(blank=True, upload_to='products/')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('preview_text', models.TextField(max_length=200)),
                ('detail_text', models.TextField(max_length=1000)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
    ]