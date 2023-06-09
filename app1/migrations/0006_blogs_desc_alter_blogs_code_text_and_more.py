# Generated by Django 4.2.2 on 2023-06-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_blogs_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='code_text',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='content_photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='content_img/'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='h1_content',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='h2_content',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='h3_content',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='h4_content',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='heading_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='heading_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='heading_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='heading_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='thumb',
            field=models.ImageField(blank=True, default='', null=True, upload_to='thumbnail/'),
        ),
    ]