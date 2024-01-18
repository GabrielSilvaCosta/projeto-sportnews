# Generated by Django 4.2.3 on 2024-01-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_news"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="category",
            new_name="categories",
        ),
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
