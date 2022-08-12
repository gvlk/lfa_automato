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
		self.verificar = True

	class Nodo:

		def __init__(self, nome: str):
			self.nome = nome
			self.ponteiros = dict()

	def inserir(self, estado: str, final=False, transicoes: dict = None):

		nodo = self.procurar_estado(estado)

		if nodo is None:
			nodo = self.Nodo(estado)
			self.estados.add(nodo)

		if self.inicial is None:
			self.inicial = nodo

		if final:
			self.final.add(nodo)

		if transicoes is not None:
			self.criar_ponteiros(nodo, transicoes)
		else:
			return nodo

	def criar_ponteiros(self, nodo, transicoes: dict):
		if 'lambda' in transicoes or 'λ' in transicoes:
			self.alfabeto.add('λ')
			if 'lambda' in transicoes:
				transicoes['λ'] = transicoes.pop('lambda')
		for simbolo, estados in transicoes.items():
			if simbolo in self.alfabeto:
				if type(estados) is not set:
					estados = {estados}
				for estado in estados:
					if estado == nodo.nome:
						nodo_apontado = nodo
					else:
						nodo_apontado = self.inserir(estado)
					ponteiro = {simbolo: {nodo_apontado}}
					if simbolo in nodo.ponteiros:
						nodo.ponteiros[simbolo].add(nodo_apontado)
					else:
						nodo.ponteiros.update(ponteiro)
			else:
				raise ValueError(f"'{simbolo}' não está no dicionário do autômato '{self.nome}'")

	def procurar_estado(self, estado):
		for nodo in self.estados:
			if nodo.nome == estado:
				return nodo
		else:
			return None

	def reconhecer(self, cadeia: str, aux=None):

		if self.final:  # Verificar se o autômato possui estado final
			if aux is None:
				aux = self.inicial
			if 'λ' in aux.ponteiros:  # Se o estado atual possui uma lambda-transição
				conjunto_estados = aux.ponteiros['λ'].copy()
				while conjunto_estados:
					estado_alternativa = conjunto_estados.pop()  # Seleciona um estado aleatorio do conjunto
					if self.reconhecer(cadeia, estado_alternativa):
						return True

			for i, simbolo in enumerate(cadeia):
				try:
					conjunto_estados = aux.ponteiros[simbolo].copy()
					aux = conjunto_estados.pop()
					subcadeia = cadeia[i+1:]
					if 'λ' in aux.ponteiros:  # Se o novo estado possui uma lambda-transição
						if self.reconhecer(subcadeia, aux):
							return True
					while conjunto_estados:  # Loop até que não existam mais estados no conjunto
						estado_alternativa = conjunto_estados.pop()
						if self.reconhecer(subcadeia, estado_alternativa):
							return True
				except KeyError:
					return False
			else:
				if aux in self.final:
					return True
				else:
					return False
		else:
			raise Exception("Não há estado final.")

	def verificar_cadeia(self, cadeia):
		if all(ca in self.alfabeto for ca in cadeia):
			self.verificar = False
			return True
		else:
			return False

	def definir_linguagem(self, tam_max):
		self.verificar = False
		for i in range(1, tam_max+1):
			for sequencia in product(self.alfabeto.difference({'λ'}), repeat=i):
				cadeia = ''.join(sequencia)
				if self.reconhecer(cadeia):
					self.linguagem.add(cadeia)

	def mostrar_linguagem(self, tam_max=5):
		self.definir_linguagem(tam_max)
		lista = sorted(self.linguagem)
		print(sorted(lista, key=len))

	def comparar_l(self, comparado):
		if self.linguagem == comparado.linguagem:
			return True
		else:
			return False
