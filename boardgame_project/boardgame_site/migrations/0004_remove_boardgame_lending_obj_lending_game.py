# Generated by Django 4.1.3 on 2022-12-09 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "boardgame_site",
            "0003_remove_lending_lent_game_boardgame_lending_obj_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="boardgame",
            name="lending_obj",
        ),
        migrations.AddField(
            model_name="lending",
            name="game",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="boardgame_site.boardgame",
            ),
            preserve_default=False,
        ),
    ]
