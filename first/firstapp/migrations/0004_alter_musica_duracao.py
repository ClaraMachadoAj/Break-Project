# Generated by Django 5.0.6 on 2024-06-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_album_ano_lancamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.CharField(max_length=5, null=None),
        ),
    ]
