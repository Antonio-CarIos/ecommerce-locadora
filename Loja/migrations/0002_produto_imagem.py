# Generated by Django 5.1.1 on 2024-10-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default=1, upload_to='capas-filmes/'),
            preserve_default=False,
        ),
    ]
