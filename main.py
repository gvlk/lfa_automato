from itertools import product


class Automato:
	def __init__(self, nome: str = 'Nome Indefinido', alfabeto: set = None):
		self.nome = nome
		self.inicial = None
		self.final = set()
		self.estados = set()
		self.alfabeto = alfabeto

	class Nodo:

		def __init__(self, nome: str):
			self.nome = nome
			self.ponteiros = dict()

	def inserir(self, estado: str, final=False, transicoes: dict = None):

		nodo = self.procurar_estado(estado)

		if nodo is None:
			nodo = self.Nodo(estado)
			self.estados.add(nodo)

		if transicoes is not None:
			self.criar_ponteiros(nodo, transicoes)
		else:
			return nodo

		if self.inicial is None:
			self.inicial = nodo

		if final:
			self.final.add(nodo)

	def criar_ponteiros(self, nodo, transicoes: dict):
		for simbolo, estado in transicoes.items():
			if estado == nodo.nome:
				nodo_apontado = nodo
			else:
				nodo_apontado = self.inserir(estado)
			ponteiro = {simbolo: {nodo_apontado}}
			nodo.ponteiros.update(ponteiro)

	def procurar_estado(self, estado):
		for nodo in self.estados:
			if nodo.nome == estado:
				return nodo
		else:
			return None

	def reconhecer(self, cadeia: str = 'λ'):
		aux = self.inicial
		for simbolo in cadeia:
			conjunto_estados = aux.ponteiros[simbolo].copy()
			aux = conjunto_estados.pop()
		else:
			if aux in self.final:
				return True
			else:
				return False

	def linguagem(self, tam_max):
		for i in range(1, tam_max+1):
			for sequencia in product(self.alfabeto, repeat=i):
				cadeia = ''.join(sequencia)
				if self.reconhecer(cadeia):
					print(cadeia)


teste1 = Automato(nome='teste1', alfabeto={'0', '1'})
teste1.inserir(estado='q0', final=False, transicoes={'0': 'q0', '1': 'q1'})
teste1.inserir(estado='q1', final=True, transicoes={'0': 'q0', '1': 'q2'})
teste1.inserir(estado='q2', final=False, transicoes={'0': 'q2', '1': 'q1'})

teste2 = Automato(nome='teste2', alfabeto={'a', 'b'})
teste2.inserir(estado='q0', final=False, transicoes={'a': 'q0', 'b': 'q1'})
teste2.inserir(estado='q1', final=True, transicoes={'a': 'q2', 'b': 'q2'})
teste2.inserir(estado='q2', final=False, transicoes={'a': 'q2', 'b': 'q2'})
