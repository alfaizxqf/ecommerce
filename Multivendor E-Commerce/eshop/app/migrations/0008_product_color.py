# Generated by Django 4.2.3 on 2023-09-19 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_color_alter_product_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.color'),
        ),
    ]
