# Generated by Django 4.2.2 on 2023-06-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_thumbnail_blogs_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='code_text',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='thumb',
            field=models.ImageField(default='', null=True, upload_to='thumbnail/'),
        ),
    ]
