# Generated by Django 4.0.5 on 2022-07-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_productos_brand_alter_productos_prize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='brand',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Apple'), (2, 'Samsung'), (3, 'Huawei'), (4, 'Sony')], verbose_name='Brand'),
        ),
    ]
