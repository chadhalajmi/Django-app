# Generated by Django 3.0.2 on 2021-04-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('prix', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]