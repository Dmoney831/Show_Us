# Generated by Django 4.0.3 on 2022-03-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0006_post_dislikes_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/icons8-documentary-48.png', upload_to='upload/profile_pictures'),
        ),
    ]
