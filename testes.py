# Guilherme Azambuja - 149 429

from main import *

# Linguagem = ? Exemplo dos slides
teste1 = Automato(nome='teste1', alfabeto={'0', '1'})
teste1.inserir(estado='q0', final=False, transicoes={'0': 'q0', '1': 'q1'})
teste1.inserir(estado='q1', final=True, transicoes={'0': 'q0', '1': 'q2'})
teste1.inserir(estado='q2', final=False, transicoes={'0': 'q2', '1': 'q1'})
# teste1.mostrar_linguagem()

# Linguagem = {a^n b / n >= 0}
teste2 = Automato(nome='teste2', alfabeto={'a', 'b'})
teste2.inserir(estado='q0', final=False, transicoes={'a': 'q0', 'b': 'q1'})
teste2.inserir(estado='q1', final=True, transicoes={'a': 'q2', 'b': 'q2'})
teste2.inserir(estado='q2', final=False, transicoes={'a': 'q2', 'b': 'q2'})
# teste2.mostrar_linguagem()

# Linguagem = {a b w / w ∈ {a, b}*}
teste3 = Automato(nome='teste3', alfabeto={'a', 'b'})
teste3.inserir(estado='q0', final=False, transicoes={'a': 'q1', 'b': 'q3'})
teste3.inserir(estado='q1', final=False, transicoes={'a': 'q3', 'b': 'q2'})
teste3.inserir(estado='q2', final=True, transicoes={'a': 'q2', 'b': 'q2'})
teste3.inserir(estado='q3', final=False, transicoes={'a': 'q3', 'b': 'q3'})
# teste3.mostrar_linguagem()

# Linguagem = Todas as cadeias do alfabeto exceto as que contem a subcadeia '001'
teste4 = Automato(nome='teste4', alfabeto={'0', '1'})
teste4.inserir(estado='q0', final=True, transicoes={'0': 'q1', '1': 'q0'})
teste4.inserir(estado='q1', final=True, transicoes={'0': 'q2', '1': 'q0'})
teste4.inserir(estado='q2', final=True, transicoes={'0': 'q2', '1': 'q3'})
teste4.inserir(estado='q3', final=False, transicoes={'0': 'q3', '1': 'q3'})
# teste4.mostrar_linguagem()

# Linguagem = Todas as cadeias do alfabeto com uma quantidade par de 'a' e 'b'
teste5 = Automato(nome='teste5', alfabeto={'a', 'b'})
teste5.inserir(estado='q0', final=True, transicoes={'a': 'q1', 'b': 'q3'})
teste5.inserir(estado='q1', final=False, transicoes={'a': 'q0', 'b': 'q2'})
teste5.inserir(estado='q2', final=False, transicoes={'a': 'q3', 'b': 'q1'})
teste5.inserir(estado='q3', final=False, transicoes={'a': 'q2', 'b': 'q0'})
# teste5.mostrar_linguagem()

# Linguagem = {a w a / w ∈ {a, b}*}
teste6 = Automato(nome='teste6', alfabeto={'a', 'b'})
teste6.inserir(estado='q0', final=False, transicoes={'a': 'q2', 'b': 'q1'})
teste6.inserir(estado='q1', final=False, transicoes={'a': 'q1', 'b': 'q1'})
teste6.inserir(estado='q2', final=False, transicoes={'a': 'q3', 'b': 'q2'})
teste6.inserir(estado='q3', final=True, transicoes={'a': 'q3', 'b': 'q2'})
# teste6.mostrar_linguagem()

# Linguagem = {a w1 a a w2 a / w1, w2 ∈ {a, b}*}
teste7 = Automato(nome='teste7', alfabeto={'a', 'b'})
teste7.inserir(estado='q0', final=False, transicoes={'a': 'q2', 'b': 'q1'})
teste7.inserir(estado='q1', final=False, transicoes={'a': 'q1', 'b': 'q1'})
teste7.inserir(estado='q2', final=False, transicoes={'a': 'q3', 'b': 'q2'})
teste7.inserir(estado='q3', final=False, transicoes={'a': 'q4', 'b': 'q2'})
teste7.inserir(estado='q4', final=False, transicoes={'a': 'q5', 'b': 'q4'})
teste7.inserir(estado='q5', final=True, transicoes={'a': 'q5', 'b': 'q4'})
# teste7.mostrar_linguagem()

# Linguagem = Todas as cadeias do alfabeto exceto as que contem a subcadeia '001'
teste8 = Automato(nome='teste8', alfabeto={'0', '1'})
teste8.inserir(estado='q0', final=False, transicoes={'0': 'q0', '1': 'q1'})
teste8.inserir(estado='q1', final=True, transicoes={'0': 'q0', '1': 'q2'})
teste8.inserir(estado='q2', final=False, transicoes={'0': 'q2', '1': 'q1'})
# teste8.mostrar_linguagem()

# Linguagem = Todas as cadeias que contêm somente um 'a'
teste9 = Automato(nome='teste9', alfabeto={'a', 'b'})
teste9.inserir(estado='q0', final=False, transicoes={'a': 'q1', 'b': 'q0'})
teste9.inserir(estado='q1', final=True, transicoes={'a': 'q2', 'b': 'q1'})
teste9.inserir(estado='q2', final=False, transicoes={'a': 'q2', 'b': 'q2'})
# teste9.mostrar_linguagem()

# NÃO FINALIZADO Linguagem = Todas as cadeias do alfabeto com uma quantidade ímpar de 'a' e 'b'
teste10 = Automato(nome='teste10', alfabeto={'a', 'b'})
teste10.inserir(estado='q0', final=False, transicoes={'a': 'q3', 'b': 'q3'})
teste10.inserir(estado='q1', final=False, transicoes={'a': 'q0', 'b': 'q2'})
teste10.inserir(estado='q2', final=False, transicoes={'a': 'q3', 'b': 'q1'})
teste10.inserir(estado='q3', final=True, transicoes={'a': 'q2', 'b': 'q1'})
teste10.mostrar_linguagem()

