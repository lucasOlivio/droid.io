# Generated by Django 3.1.5 on 2021-02-02 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("demands", "0003_auto_20210201_1603"),
    ]

    operations = [
        migrations.AlterField(
            model_name="demand",
            name="user_updated",
            field=models.ForeignKey(
                blank=True,
                help_text="Último usuário que atualizou a demanda.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Ultimo atualizador",
            ),
        )
    ]
