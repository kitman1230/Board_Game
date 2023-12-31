# Generated by Django 4.2.7 on 2023-11-10 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_edit_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('alternative_names', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_year', models.PositiveIntegerField(blank=True)),
                ('publisher', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('min_players', models.PositiveIntegerField()),
                ('max_players', models.PositiveIntegerField(blank=True)),
                ('min_time_period', models.PositiveIntegerField()),
                ('max_time_peroid', models.PositiveIntegerField(blank=True)),
                ('age_limit', models.PositiveIntegerField(default=3)),
                ('complexity_rating', models.PositiveIntegerField(default=0)),
                ('designer', models.CharField(blank=True, max_length=50)),
                ('artist', models.CharField(blank=True, max_length=50)),
                ('available_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('lend_limit_status', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_lended', models.DateTimeField(auto_now_add=True)),
                ('date_return', models.DateTimeField(blank=True)),
                ('board_game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game_board.boardgame')),
                ('debit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game_board.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Bad'), (2, 'Soso'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')])),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_edit_date', models.DateTimeField(auto_now=True)),
                ('board_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_board.boardgame')),
            ],
        ),
        migrations.AddField(
            model_name='boardgame',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game_board.category'),
        ),
        migrations.AddField(
            model_name='boardgame',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
