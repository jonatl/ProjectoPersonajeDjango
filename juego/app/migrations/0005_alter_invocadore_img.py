# Generated by Django 4.1.7 on 2023-03-16 16:36

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_avisos_contacto_importante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invocadore',
            name='img',
            field=models.ImageField(blank=True, default=django.db.models.fields.NOT_PROVIDED, null=True, upload_to='personaje'),
        ),
    ]
