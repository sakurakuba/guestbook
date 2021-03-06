# Generated by Django 4.0.5 on 2022-07-03 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Unknown', max_length=50, verbose_name='Author')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('content', models.TextField(max_length=3000, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('status', models.CharField(choices=[('active', 'actual'), ('blocked', 'banned')], default='active', max_length=20, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book',
            },
        ),
    ]
