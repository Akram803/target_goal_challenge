# Generated by Django 3.0.7 on 2020-07-14 11:30

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
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.IntegerField()),
                ('what', models.CharField(max_length=50)),
                ('per', models.CharField(choices=[('d', 'day'), ('w', 'weak'), ('m', 'month')], max_length=1)),
                ('st_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'challenge',
                'verbose_name_plural': 'challenge',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('st_date', models.DateField(auto_now_add=True)),
                ('periority', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'target',
                'verbose_name_plural': 'target',
                'ordering': ['periority'],
                'unique_together': {('user', 'name'), ('user', 'periority')},
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('st_date', models.DateField(auto_now_add=True)),
                ('periority', models.IntegerField(default=0)),
                ('n_units', models.IntegerField(default=0)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_go_cha.Target')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'goal',
                'verbose_name_plural': 'goal',
                'ordering': ['periority'],
                'unique_together': {('user', 'target', 'periority'), ('user', 'target', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ChallengeLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('count', models.IntegerField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_go_cha.Challenge')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ta_go_cha.Goal')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ta_go_cha.Target')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'challengelogs',
                'verbose_name_plural': 'challengelogs',
            },
        ),
        migrations.AddField(
            model_name='challenge',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_go_cha.Goal'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ta_go_cha.Target'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]