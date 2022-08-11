# Guilherme Azambuja - 149 429

from itertools import product


class Automato:
	def __init__(self, nome: str = 'Nome Indefinido', alfabeto: set = None):
		self.nome = nome
		self.inicial = None
		self.final = set()
		self.estados = set()
		self.alfabeto = alfabeto
		self.linguagem = set()

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
		if self.final:
			aux = self.inicial
			for simbolo in cadeia:
				conjunto_estados = aux.ponteiros[simbolo].copy()
				aux = conjunto_estados.pop()
			else:
				if aux in self.final:
					return True
				else:
					return False
		else:
			raise Exception("Não há estado final.")

	def definir_linguagem(self, tam_max=6):
		for i in range(1, tam_max+1):
			for sequencia in product(self.alfabeto, repeat=i):
				cadeia = ''.join(sequencia)
				if self.reconhecer(cadeia):
					self.linguagem.add(cadeia)

	def mostrar_linguagem(self):
		self.definir_linguagem()
		lista = sorted(self.linguagem)
		print(sorted(lista, key=len))
