# Generated by Django 4.1.7 on 2023-05-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_library', '0003_book_one unique title per author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='started_reading',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
