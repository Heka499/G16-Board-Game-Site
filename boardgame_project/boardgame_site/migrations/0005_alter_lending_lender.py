# Generated by Django 4.1.3 on 2022-12-09 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("boardgame_site", "0004_remove_boardgame_lending_obj_lending_game"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lending",
            name="lender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
