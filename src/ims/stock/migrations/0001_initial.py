# Generated by Django 5.0.13 on 2025-06-16 10:44

import django.db.models.deletion
import utils.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('tenant_id', models.CharField(default=None, max_length=128, null=True)),
                ('created_by', models.CharField(default=None, max_length=128, null=True)),
                ('updated_by', models.CharField(default=None, max_length=128, null=True)),
                ('updated_dtm', models.DateTimeField(auto_now=True)),
                ('created_dtm', models.DateTimeField(auto_now_add=True)),
                ('deleted_dtm', models.DateTimeField(default=None, null=True)),
                ('stock_id', models.CharField(default=utils.functions.get_uuid, max_length=36, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('reference_number', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('movement_type', models.CharField(choices=[('IN', 'In'), ('OUT', 'Out')], max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('supplier', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
            options={
                'db_table': 'stocks',
            },
        ),
    ]
