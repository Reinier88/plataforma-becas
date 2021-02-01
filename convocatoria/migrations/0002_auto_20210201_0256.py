# Generated by Django 3.1.4 on 2021-02-01 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('convocatoria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aspirantes',
            old_name='aspirante_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='aspirantes',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aspirantes',
            name='folio',
            field=models.CharField(max_length=16, unique=True, verbose_name='Folio'),
        ),
        migrations.AlterField(
            model_name='aspirantes',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Estudiante'),
        ),
    ]