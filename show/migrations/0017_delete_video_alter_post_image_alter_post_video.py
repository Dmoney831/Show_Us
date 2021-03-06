# Generated by Django 4.0.3 on 2022-03-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0016_remove_post_video_post_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/post_videos'),
        ),
    ]
