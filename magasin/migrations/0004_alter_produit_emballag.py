# Generated by Django 3.2 on 2021-06-07 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_auto_20210604_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='emballag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.emballage'),
        ),
    ]
