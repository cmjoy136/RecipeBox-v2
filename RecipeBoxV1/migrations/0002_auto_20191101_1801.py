# Generated by Django 2.2.5 on 2019-11-01 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeBoxV1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitem',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]