# Generated by Django 5.0.3 on 2024-04-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Linkfeed', '0002_post_is_rss_feed_post_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.URLField(blank=True),
        ),
    ]
