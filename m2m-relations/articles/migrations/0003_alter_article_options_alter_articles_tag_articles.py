# Generated by Django 5.0.4 on 2024-04-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_tag_articles_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articles_tag',
            name='articles',
            field=models.ManyToManyField(related_name='articles_tag', through='articles.Articles_scope', to='articles.article'),
        ),
    ]
