# Generated by Django 5.1 on 2024-08-11 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(max_length=255, verbose_name="Nome da pessoa"),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Email da pessoa"),
                ),
                (
                    "data_nascimento",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de nascimento"
                    ),
                ),
                (
                    "ativo",
                    models.BooleanField(
                        default=True, verbose_name="A pessoa está ativa?"
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=6,
                        null=True,
                        verbose_name="Valor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pessoa",
                "verbose_name_plural": "Pessoas",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("email", "data_nascimento"), name="unique_person"
                    )
                ],
            },
        ),
    ]
