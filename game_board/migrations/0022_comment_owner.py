# Generated by Django 4.2.7 on 2023-11-12 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_board', '0021_remove_comment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_board.profile'),
            preserve_default=False,
        ),
    ]
