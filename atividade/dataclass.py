#Crie uma `dataclass` chamada `Aluno` com:

#```text
#nome
#matricula
#nota1
#nota2
#```

#Crie um método chamado `media()` que calcule a média das duas notas.

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    matricula: int
    nota1: float
    nota2: float
    def calcular_media(self) -> float:
        return (self.nota1 + self.nota2) / 2

aluno = Aluno(
    "Maria",
    1234,
    8.5,
    9.5
)

print(f"A média de {aluno.nome} é {aluno.calcular_media():.2f}")