# Generated by Django 3.1.7 on 2021-04-05 10:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntermediateTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер клиента')),
                ('address', models.CharField(max_length=40, verbose_name='Адрес клиента')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('product', models.ManyToManyField(related_name='products', through='webapp.IntermediateTable', to='webapp.Product', verbose_name='Товары')),
            ],
        ),
        migrations.AddField(
            model_name='intermediatetable',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='webapp.order'),
        ),
        migrations.AddField(
            model_name='intermediatetable',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intermediate_table', to='webapp.product'),
        ),
    ]
