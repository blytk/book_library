# Generated by Django 4.1.7 on 2023-04-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_library', '0002_wish_recommend_wish_why_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='one unique title per author'),
        ),
    ]
