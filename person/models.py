from datetime import date, datetime

from django.db import models
from django.db.models.constraints import UniqueConstraint


class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome da pessoa", max_length=255)
    email = models.EmailField(
        verbose_name="Email da pessoa",
    )
    data_nascimento = models.DateField(
        verbose_name="Data de nascimento", null=True, blank=True
    )
    ativo = models.BooleanField(verbose_name="A pessoa está ativa?", default=True)
    valor = models.DecimalField(
        verbose_name="Valor", max_digits=6, decimal_places=2, null=True, blank=True
    )

    @property
    def idade(self):
        """
        Calcula a idade da pessoa.
        """
        if self.data_nascimento:
            if isinstance(self.data_nascimento, datetime):
                data_nascimento = self.data_nascimento.date()
            elif isinstance(self.data_nascimento, date):
                data_nascimento = self.data_nascimento
            else:
                try:
                    data_nascimento = datetime.strptime(
                        self.data_nascimento, "%Y-%m-%d %H:%M:%S"
                    ).date()
                except ValueError:
                    data_nascimento = datetime.strptime(
                        self.data_nascimento, "%Y-%m-%d"
                    ).date()
            hoje = datetime.now().date()

            idade = hoje.year - data_nascimento.year
            if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1
            return idade
        return None

    def calcular_valor(self):
        """
        Calcula o valor da pessoa conforme a idade.
        """
        if self.idade is None:
            return None
        if self.idade < 21:
            return 100.00
        elif self.idade < 60:
            return 150.00
        else:
            return 200.00

    def save(self, *args, **kwargs):
        self.valor = self.calcular_valor()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        constraints = [
            UniqueConstraint(fields=("email", "data_nascimento"), name="unique_person"),
        ]
