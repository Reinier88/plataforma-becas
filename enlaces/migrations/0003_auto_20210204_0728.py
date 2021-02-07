# Generated by Django 3.1.4 on 2021-02-04 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("becas", "0002_auto_20210204_0724"),
        ("enlaces", "0002_auto_20210204_0727"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enlaces",
            name="university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="becas.universities",
                verbose_name="Universidad",
            ),
        ),
    ]