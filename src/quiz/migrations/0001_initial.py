# Generated by Django 2.2.3 on 2019-07-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(unique=True)),
                ('q1', models.TextField()),
                ('q2', models.TextField()),
                ('q3', models.TextField()),
                ('q4', models.TextField()),
                ('q5', models.TextField()),
                ('q6', models.TextField()),
                ('q7', models.TextField()),
                ('q8', models.TextField()),
                ('q9', models.TextField()),
                ('q10', models.TextField()),
            ],
        ),
    ]
