# Guilherme Azambuja - 149 429
from __future__ import annotations
from itertools import product
from random import choice


class Automato:

	def fcadeias(self):
		cadeias = list()
		cadeias_existentes = self.linguagem.union(self.cnrs)
		tam_max = self.tam_predefinido[1]
		for tam in range(0, tam_max + 1):
			if tam == 0:
				cadeias.insert(tam, set())
				continue
			self.tams.add(tam)
			cadeias_msmtam = set()
			sequencias = set(product(self.alfabeto - {'λ'}, repeat=tam))
			for sequencia in sequencias:
				cadeia = ''.join(sequencia)
				cadeias_msmtam.add(cadeia)
			cadeias.insert(tam, cadeias_msmtam.difference(cadeias_existentes))
		return tuple(cadeias)

	def __init__(self, nome: str = 'Nome Indefinido', alfabeto: set = None):
		self.nome = nome
		self.inicial = None
		self.final = set()
		self.estados = set()
		self.alfabeto = alfabeto.union({'λ'})
		self.linguagem = set()
		self.cnrs = set()
		self.tam_predefinido = (1, 10)  # Tamanho padrão das cadeias
		self.tams = set()  # Tamanhos de cadeia que possuem cadeias ainda não testadas
		self.cadeias = self.fcadeias()  # Lista vai virar tupla com todas as cadeias ainda não testadas de tamanho [1, 10]
		self.boolverificar = True

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

	def procurar_estado(self, estado) -> Nodo | None:
		for nodo in self.estados:
			if nodo.nome == estado:
				return nodo
		else:
			return None

	def verificar(self, cadeia: str) -> bool:
		if self.boolverificar:
			if self.final:  # Verificar se o autômato possui estado final
				if all(ca in self.alfabeto for ca in cadeia):
					self.boolverificar = False
					return self.reconhecer(cadeia)
				else:
					return False
			else:
				raise Exception("Não há estado final.")

	def reconhecer(self, cadeia: str, aux: Nodo = None) -> bool:

		if self.boolverificar:
			if not self.verificar(cadeia):
				return False
			else:
				self.boolverificar = True
				return True

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
				subcadeia = cadeia[i + 1:]  # Representa os símbolos que ainda não foram lidos
				if 'λ' in aux.ponteiros:  # Se o novo estado possui uma lambda-transição
					if self.reconhecer(subcadeia, aux):
						return True
				while conjunto_estados:  # Loop até que não existam mais estados no conjunto
					estado_alternativa = conjunto_estados.pop()
					if self.reconhecer(subcadeia, estado_alternativa):
						return True
			except KeyError:
				return False  # O estado não possui uma transição para o símbolo lido
		else:
			if aux in self.final:
				return True
			else:
				return False  # 'aux' parou em um estado não-final sem mais símbolos para ler

	def definir_linguagem(self, tam_min: int = None, tam_max: int = None):
		self.boolverificar = False

		if tam_min is None:
			tam_min = self.tam_predefinido[0]
		if tam_max is None:
			tam_max = self.tam_predefinido[1]

		for tam in range(tam_min, tam_max + 1):
			while True:
				try:
					cadeia = self.cadeias[tam].pop()
					if self.reconhecer(cadeia):
						self.linguagem.add(cadeia)
					else:
						self.cnrs.add(cadeia)
				except KeyError:  # Acabaram as cadeias de tamanho 'tam'
					break
				except IndexError:  # Ainda não foram criadas cadeias de tamanho 'tam'
					self.tam_predefinido = (self.tam_predefinido[0], tam_max)
					self.cadeias = self.fcadeias()

		self.boolverificar = True

	def mostrar_linguagem(self, *args):
		if self.final:  # Verificar se o autômato possui estado final
			if len(args) == 0:
				tam_min = self.tam_predefinido[0]
				tam_max = self.tam_predefinido[1]
			elif len(args) == 1:  # Se só um argumento for passado, o valor será usado como tamanho máximo da cadeia
				tam_min = self.tam_predefinido[0]
				tam_max = args[-1]
			elif len(args) == 2:
				tam_min = args[-2]
				tam_max = args[-1]
			else:
				raise TypeError(f"mostrar_linguagem() recebe de 0 a 2 argumentos mas {len(args)} foram passados")

			if tam_min <= 0:
				raise ValueError(f"'tam_min' tem que ser um valor positivo maior que zero")
			elif tam_max <= 0:
				raise ValueError(f"'tam_max' tem que ser um valor positivo maior que zero")

			self.definir_linguagem(tam_min, tam_max)
			if self.linguagem:  # Se foram encontradas cadeias de tamanho 'tam_max' que o autômato reconhece
				lista = sorted(self.linguagem)
				lista = sorted(lista, key=len)
				for e in lista:
					if tam_min <= len(e) <= tam_max:
						print(f"\033[32m{e}\033[0m", end=' ')
				print()
			else:
				print(f'O autômato não reconhece nenhuma cadeia de tamanho {tam_max} ou menor. Tentarei cadeias de tamanho {tam_max + 1} a {tam_max + 4}...')
				self.mostrar_linguagem(tam_max+1, tam_max+4)

		else:
			raise Exception("Não há estado final.")

	def buscar_cnr(self, qnt: int = 3):
		self.boolverificar = False
		cnr = tst = 0  # 'cnr'=quantidade de cnr encontradas, 'tst'=quantidade de cadeias testadas
		lim = 150000  # 'lim'=quantidade máxima de cadeias que podem ser testadas
		cnrs = set()  # 'qnt'=quantidade de cnr sendo buscadas 'cnrs'=conjunto local de cnrs
		while cnr != qnt and tst < lim:
			while True:
				try:
					tam = choice(tuple(self.tams))  # IndexError = acabou as cadeias do self.cadeias
					try:
						cadeia = self.cadeias[tam].pop()
						break
					except KeyError:
						self.tams.remove(tam)
				except IndexError:
					cadeia = None  # Não há mais cadeias para testar
					break
			if cadeia is not None:
				tst += 1
				if not self.reconhecer(cadeia):
					cnrs.add(cadeia)
					cnr += 1
				else:
					self.linguagem.add(cadeia)
			else:
				cnrs.add(choice(tuple(self.cnrs)))
				cnr += 1
		else:
			self.boolverificar = True
			if cnrs:
				self.cnrs.update(cnrs)  # Adicionar ao conjunto de cnrs do autômato o conjunto encontrado nessa execução da função
				print(f"{cnr} Cadeias não reconhecidas: ", end='')
				for e in cnrs:
					print(f"\033[31m'{e}'\033[0m", end=' ')
				print()
			else:
				print(f"Limite de {lim} cadeias testadas alcançado. Não foi encontrada nenhuma cadeia não reconhecida.")

	def comparar_l(self, comparado: Automato) -> bool:
		if self.linguagem and comparado.linguagem:  # Se ambos autômatos já possuem uma linguagem definida
			if self.linguagem == comparado.linguagem:
				return True
			else:
				return False
		else:
			self.definir_linguagem(self.tam_predefinido[0], self.tam_predefinido[1])
			comparado.definir_linguagem(self.tam_predefinido[0], self.tam_predefinido[1])
			return self.comparar_l(comparado)
