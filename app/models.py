# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleta(models.Model):
    id_boleta = models.FloatField(primary_key=True)
    detalle_boleta = models.CharField(max_length=100)
    valor_boleta = models.FloatField()
    id_recepcion = models.ForeignKey('RecepcionProducto', models.DO_NOTHING, db_column='id_recepcion')
    id_pago = models.ForeignKey('PagoFiado', models.DO_NOTHING, db_column='id_pago')
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'boleta'


class Cliente(models.Model):
    id_cliente = models.FloatField(primary_key=True)
    nombre_cliente = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    rut = models.FloatField()
    dv_rut = models.CharField(max_length=1)
    fechar_registro = models.DateField()
    deuda = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cliente'


class CodigoBarra(models.Model):
    id_codigo_barra = models.FloatField(primary_key=True)
    img_codigo = models.BinaryField()
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'codigo_barra'


class Comprobante(models.Model):
    nc = models.FloatField(primary_key=True)
    fecha_comprobante = models.CharField(max_length=50)
    valor = models.FloatField()
    id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='id_empleado')
    id_detalle = models.ForeignKey('DetalleBoleta', models.DO_NOTHING, db_column='id_detalle')

    class Meta:
        managed = False
        db_table = 'comprobante'


class DetalleBoleta(models.Model):
    id_detalle = models.FloatField(primary_key=True)
    numboleta = models.FloatField()
    producto = models.FloatField()
    cantidad = models.FloatField()
    precio = models.FloatField()
    id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='id_boleta')

    class Meta:
        managed = False
        db_table = 'detalle_boleta'


class Empleado(models.Model):
    id_empleado = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apelido_paterno = models.FloatField()
    apellido_materno = models.FloatField()
    rut = models.FloatField()
    dv_rut = models.CharField(max_length=1)
    direccion = models.CharField(max_length=50)
    telefono = models.FloatField()
    fecha_contrato = models.CharField(max_length=50)
    fecha_termino_contrato = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50)
    sueldo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Fiado(models.Model):
    id_fiado = models.FloatField(primary_key=True)
    monto = models.FloatField()
    plazo = models.CharField(max_length=50)
    id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='id_boleta')
    id_detalle = models.ForeignKey(DetalleBoleta, models.DO_NOTHING, db_column='id_detalle')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_orden = models.ForeignKey('OrdenPedido', models.DO_NOTHING, db_column='id_orden')
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')

    class Meta:
        managed = False
        db_table = 'fiado'


class Informe(models.Model):
    id_informe = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'informe'


class OrdenPedido(models.Model):
    id_orden = models.FloatField(primary_key=True)
    detalle_orden = models.CharField(max_length=100)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_informe = models.ForeignKey(Informe, models.DO_NOTHING, db_column='id_informe')

    class Meta:
        managed = False
        db_table = 'orden_pedido'


class PagoFiado(models.Model):
    id_pago = models.FloatField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    estado_pago = models.CharField(max_length=1)
    valor_abono = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pago_fiado'


class Pedido(models.Model):
    id_pedido = models.FloatField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_detalle = models.ForeignKey(DetalleBoleta, models.DO_NOTHING, db_column='id_detalle')

    class Meta:
        managed = False
        db_table = 'pedido'


class Producto(models.Model):
    id_producto = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha_vencimiento = models.DateField()
    id_tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo_producto')
    id_orden = models.ForeignKey(OrdenPedido, models.DO_NOTHING, db_column='id_orden')
    id_recepcion = models.ForeignKey('RecepcionProducto', models.DO_NOTHING, db_column='id_recepcion')
    stock = models.FloatField()
    barcode = models.FloatField()
    img_producto = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.FloatField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    telefono = models.FloatField()
    correo = models.CharField(max_length=50)
    id_informe = models.FloatField()

    class Meta:
        managed = False
        db_table = 'proveedor'


class RecepcionProducto(models.Model):
    id_recepcion = models.FloatField(primary_key=True)
    detalle_recepcion = models.CharField(max_length=100)
    id_informe = models.ForeignKey(Informe, models.DO_NOTHING, db_column='id_informe')
    id_orden = models.ForeignKey(OrdenPedido, models.DO_NOTHING, db_column='id_orden')

    class Meta:
        managed = False
        db_table = 'recepcion_producto'


class TipoProducto(models.Model):
    id_tipo_producto = models.FloatField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50)
    img_tipo = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'
