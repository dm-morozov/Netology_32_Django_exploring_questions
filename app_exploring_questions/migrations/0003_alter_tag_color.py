# Generated by Django 5.1.1 on 2024-09-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_exploring_questions', '0002_alter_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
