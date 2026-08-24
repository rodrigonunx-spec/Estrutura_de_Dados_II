from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    matricula: int
    nota1: float
    nota2: float
    def calcular_media(self) -> float:
        return (self.nota1 + self.nota2) / 2

alunos = [
    Aluno("Maria", 2098, 8.5, 9.5),
    Aluno("João", 2176, 7.0, 7.9),
    Aluno("Silviane", 1943, 9.2, 7.3),
    Aluno("Ryuu", 5408, 8.4, 9.7),
    Aluno("Amanda", 8709, 4.6, 9.7)
]

for aluno in alunos:
    if aluno.calcular_media() > 7.0:
        print(aluno.nome)