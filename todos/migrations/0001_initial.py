# Generated by Django 3.1.5 on 2021-03-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('is_comolete', models.BooleanField(default=False)),
                ('craeted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]