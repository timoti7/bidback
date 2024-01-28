# Generated by Django 4.0.4 on 2024-01-27 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.subcategory'),
            preserve_default=False,
        ),
    ]
