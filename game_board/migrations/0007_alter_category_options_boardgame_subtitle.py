# Generated by Django 4.2.7 on 2023-11-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_board', '0006_remove_boardgame_category_boardgame_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='boardgame',
            name='subtitle',
            field=models.CharField(default='aaa', max_length=200),
            preserve_default=False,
        ),
    ]
