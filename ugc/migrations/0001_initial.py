# Generated by Django 3.0.8 on 2022-02-07 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(unique=True, verbose_name='Id user in social')),
                ('name', models.TextField(verbose_name='User Name')),
                ('username', models.TextField(verbose_name='Username')),
                ('group', models.TextField(verbose_name='Group_id')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time got')),
                ('group', models.TextField(verbose_name='Group_id')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ugc.Profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
