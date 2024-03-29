from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_add_basic_sctruture_version_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='guild',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.IntegerField(default=18, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='mode_game',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Mode Game'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='type_user',
            field=models.CharField(max_length=50, verbose_name='Type User'),
        ),
        migrations.CreateModel(
            name='GuildModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('size_players', models.IntegerField(default=1, verbose_name='Size Players')),
                ('guild_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usermodel')),
            ],
        ),
    ]
