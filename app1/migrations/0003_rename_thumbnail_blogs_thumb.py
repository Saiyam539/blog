# Generated by Django 4.2.2 on 2023-06-08 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_content_img_blogs_content_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='thumbnail',
            new_name='thumb',
        ),
    ]