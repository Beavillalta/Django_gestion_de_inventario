# Generated by Django 5.0.2 on 2024-02-21 04:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_app', '0006_rename_detallepedido_detallepedidocompra_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DetallePedidoCompra',
            new_name='DetallePedido',
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('COMPRA', 'Compra'), ('VENTA', 'Venta')], max_length=6, null=True)),
                ('fecha_pedido', models.DateField()),
                ('descripcion', models.TextField(null=True)),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('productos', models.ManyToManyField(through='inventario_app.DetallePedido', to='inventario_app.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_app.proveedor')),
            ],
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_app.pedido'),
        ),
        migrations.DeleteModel(
            name='PedidoCompra',
        ),
    ]