# Generated by Django 4.1.7 on 2023-04-24 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_library', '0002_alter_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='main',
        ),
    ]
