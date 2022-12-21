# Generated by Django 4.1.4 on 2022-12-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_title_tag_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Seleccione una imagen para mostrar', null=True, upload_to='app/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Etiqueta de comentario', max_length=200),
        ),
    ]
