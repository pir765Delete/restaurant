# Generated by Django 5.0.4 on 2024-04-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]