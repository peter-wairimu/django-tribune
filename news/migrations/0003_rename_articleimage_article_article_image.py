# Generated by Django 3.2.7 on 2021-10-05 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_article_image_article_articleimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='articleimage',
            new_name='article_image',
        ),
    ]
