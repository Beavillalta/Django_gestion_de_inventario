# Generated by Django 5.0.2 on 2024-02-21 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidocompra',
            name='cantidad',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
