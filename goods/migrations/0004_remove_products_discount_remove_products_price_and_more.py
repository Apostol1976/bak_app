# Generated by Django 4.2.7 on 2024-04-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0003_alter_categories_name_alter_categories_slug_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="discount",
        ),
        migrations.RemoveField(
            model_name="products",
            name="price",
        ),
        migrations.RemoveField(
            model_name="products",
            name="quantity",
        ),
        migrations.AddField(
            model_name="products",
            name="epdmgaskets",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                max_digits=2,
                verbose_name="Количество уплотнителей",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="insdepth",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                max_digits=2,
                verbose_name="Глубина профиля",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="numofchamb",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                max_digits=2,
                verbose_name="Количество камер",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="soundinstall",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                max_digits=2,
                verbose_name="Коэффициент звукоизоляции",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="thermaltransm",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=4,
                verbose_name="Коэффициент теплоотдачи",
            ),
        ),
    ]
