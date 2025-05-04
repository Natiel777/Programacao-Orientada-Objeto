from abc import ABC, abstractmethod

class Pessoa(ABC): 
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento

    @abstractmethod
    def exibir_dados(self):
        pass

    def _get_cpf(self):
        return self.__cpf


class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = []
        self.disciplinas = []

    def adicionar_nota(self, nota):
        self.__notas.append(nota)

    def exibir_dados(self):
        print("Aluno:", self.nome)
        print("Matrícula:", self.__matricula)
        print("CPF:", self._get_cpf())
        print("Nascimento:", self.data_nascimento)
        print("Notas:", self.__notas)
        nomes_disciplinas = [d.nome for d in self.disciplinas]
        print("Disciplinas:", nomes_disciplinas)
        print()


class Professor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, siape):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = []

    def exibir_dados(self):
        print("Professor:", self.nome)
        print("SIAPE:", self.__siape)
        print("CPF:", self._get_cpf())
        print("Nascimento:", self.data_nascimento)
        nomes_disciplinas = [d.nome for d in self.disciplinas]
        print("Disciplinas:", nomes_disciplinas)
        print()


class Disciplina:
    def __init__(self, codigo, nome, professor_responsavel):
        self.codigo = codigo
        self.nome = nome
        self.professor_responsavel = professor_responsavel
        self.alunos_matriculados = []
        professor_responsavel.disciplinas.append(self)

    def matricular_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)
        aluno.disciplinas.append(self)

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome} (Código: {self.codigo})")
        print("Professor:", self.professor_responsavel.nome)
        nomes_alunos = [a.nome for a in self.alunos_matriculados]
        print("Alunos:", nomes_alunos)
        print()
