# Generated by Django 4.1.7 on 2023-04-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='recommend',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wish',
            name='why',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddConstraint(
            model_name='wish',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='one why per user/book wish'),
        ),
    ]
