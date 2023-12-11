from django.db import models


# Create your models here.
class PersonsModel(models.Model):
    class Meta:
        verbose_name='Funcionário'
        verbose_name_plural='Funcionários'
        
    pai = models.CharField(
        max_length=254,  blank=True, verbose_name='Nome do pai'
    )
    mae = models.CharField(max_length=254, verbose_name='Nome da mãe')
    nome = models.CharField(max_length=254, verbose_name='Nome completo')
    sexo = models.CharField(max_length=10, verbose_name='Sexo')
    nascimento = models.DateField(verbose_name='Data de Nascimento')
    rg = models.CharField(max_length=9, verbose_name='Identidade')
    cpf = models.CharField(unique=True, max_length=11, verbose_name='CPF')
    email = models.EmailField(blank=True, verbose_name='E-Mail')
    telefone = models.CharField(max_length=14, verbose_name='Telefone')
    endereco = models.CharField(max_length=254, verbose_name='Endereço')
    cargo = models.CharField(max_length=254, verbose_name='Cargo')
    salario = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Salário R$'
    )
    admissao = models.DateField(blank=True, null=True, verbose_name='Admissão')

    
    def __str__(self) -> str:
        return self.nome
        