# Guilherme Azambuja - 149 429

from main import *

# Linguagem = {a^n b / n >= 0}
# teste2 = Automato(nome='teste2', alfabeto={'a', 'b'})
# teste2.inserir(estado='q0', final=False, transicoes={'a': 'q0', 'b': 'q1'})
# teste2.inserir(estado='q1', final=True, transicoes={'a': 'q2', 'b': 'q2'})
# teste2.inserir(estado='q2', final=False, transicoes={'a': 'q2', 'b': 'q2'})
# teste2.mostrar_linguagem()

# Linguagem = {a b w / w ∈ {a, b}*}
# teste3 = Automato(nome='teste3', alfabeto={'a', 'b'})
# teste3.inserir(estado='q0', final=False, transicoes={'a': 'q1', 'b': 'q3'})
# teste3.inserir(estado='q1', final=False, transicoes={'a': 'q3', 'b': 'q2'})
# teste3.inserir(estado='q2', final=True, transicoes={'a': 'q2', 'b': 'q2'})
# teste3.inserir(estado='q3', final=False, transicoes={'a': 'q3', 'b': 'q3'})
# teste3.mostrar_linguagem()

# Linguagem = Todas as cadeias do alfabeto exceto as que contem a subcadeia '001'
# teste4 = Automato(nome='teste4', alfabeto={'0', '1'})
# teste4.inserir(estado='q0', final=True, transicoes={'0': 'q1', '1': 'q0'})
# teste4.inserir(estado='q1', final=True, transicoes={'0': 'q2', '1': 'q0'})
# teste4.inserir(estado='q2', final=True, transicoes={'0': 'q2', '1': 'q3'})
# teste4.inserir(estado='q3', final=False, transicoes={'0': 'q3', '1': 'q3'})
# teste4.mostrar_linguagem()

# Linguagem = Todas as cadeias do alfabeto com uma quantidade par de 'a' e 'b'
# teste5 = Automato(nome='teste5', alfabeto={'a', 'b'})
# teste5.inserir(estado='q0', final=True, transicoes={'a': 'q1', 'b': 'q3'})
# teste5.inserir(estado='q1', final=False, transicoes={'a': 'q0', 'b': 'q2'})
# teste5.inserir(estado='q2', final=False, transicoes={'a': 'q3', 'b': 'q1'})
# teste5.inserir(estado='q3', final=False, transicoes={'a': 'q2', 'b': 'q0'})
# teste5.mostrar_linguagem()

# Linguagem = {a w a / w ∈ {a, b}*}
# teste6 = Automato(nome='teste6', alfabeto={'a', 'b'})
# teste6.inserir(estado='q0', final=False, transicoes={'a': 'q2', 'b': 'q1'})
# teste6.inserir(estado='q1', final=False, transicoes={'a': 'q1', 'b': 'q1'})
# teste6.inserir(estado='q2', final=False, transicoes={'a': 'q3', 'b': 'q2'})
# teste6.inserir(estado='q3', final=True, transicoes={'a': 'q3', 'b': 'q2'})
# teste6.mostrar_linguagem()

# Linguagem = {a w1 a a w2 a / w1, w2 ∈ {a, b}*}
# teste7 = Automato(nome='teste7', alfabeto={'a', 'b'})
# teste7.inserir(estado='q0', final=False, transicoes={'a': 'q2', 'b': 'q1'})
# teste7.inserir(estado='q1', final=False, transicoes={'a': 'q1', 'b': 'q1'})
# teste7.inserir(estado='q2', final=False, transicoes={'a': 'q3', 'b': 'q2'})
# teste7.inserir(estado='q3', final=False, transicoes={'a': 'q4', 'b': 'q2'})
# teste7.inserir(estado='q4', final=False, transicoes={'a': 'q5', 'b': 'q4'})
# teste7.inserir(estado='q5', final=True, transicoes={'a': 'q5', 'b': 'q4'})
# teste7.mostrar_linguagem()

# Linguagem = Todas as cadeias do alfabeto exceto as que contem a subcadeia '001'
# teste8 = Automato(nome='teste8', alfabeto={'0', '1'})
# teste8.inserir(estado='q0', final=False, transicoes={'0': 'q0', '1': 'q1'})
# teste8.inserir(estado='q1', final=True, transicoes={'0': 'q0', '1': 'q2'})
# teste8.inserir(estado='q2', final=False, transicoes={'0': 'q2', '1': 'q1'})
# teste8.mostrar_linguagem()

# Linguagem = Todas as cadeias que contêm somente um 'a'
# teste9 = Automato(nome='teste9', alfabeto={'a', 'b'})
# teste9.inserir(estado='q0', final=False, transicoes={'a': 'q1', 'b': 'q0'})
# teste9.inserir(estado='q1', final=True, transicoes={'a': 'q2', 'b': 'q1'})
# teste9.inserir(estado='q2', final=False, transicoes={'a': 'q2', 'b': 'q2'})
# teste9.mostrar_linguagem()

# Linguagem = Cadeias do alfabeto com uma quantidade ímpar de 'a' e 'b'
# teste10 = Automato(nome='teste10', alfabeto={'a', 'b'})
# teste10.inserir(estado='q0', final=False, transicoes={'a': 'q1', 'b': 'q3'})
# teste10.inserir(estado='q1', final=False, transicoes={'a': 'q0', 'b': 'q2'})
# teste10.inserir(estado='q2', final=True, transicoes={'a': 'q3', 'b': 'q1'})
# teste10.inserir(estado='q3', final=False, transicoes={'a': 'q2', 'b': 'q0'})
# teste10.mostrar_linguagem()

# Linguagem = Cadeias de 'a' de tamanho par e a cadeia 'aab' * Autômato Finito Não-Determinístico
# teste11 = Automato(nome='teste11', alfabeto={'a', 'b'})
# teste11.inserir(estado='q0', final=False, transicoes={'a': {'q1', 'q4'}})
# teste11.inserir(estado='q1', final=False, transicoes={'a': 'q2'})
# teste11.inserir(estado='q2', final=False, transicoes={'b': 'q3'})
# teste11.inserir(estado='q3', final=True)
# teste11.inserir(estado='q4', final=False, transicoes={'a': 'q5'})
# teste11.inserir(estado='q5', final=True, transicoes={'a': 'q4'})
# teste11.mostrar_linguagem(8)

# Linguagem = Cadeias do tipo {0n 1m 2p / n, m, p >= 0} * Autômato Finito Não-Determinístico
# teste12 = Automato(nome='teste12', alfabeto={'0', '1', '2'})
# teste12.inserir(estado='q0', final=False, transicoes={'0': 'q0', 'lambda': 'q1'})
# teste12.inserir(estado='q1', final=False, transicoes={'1': 'q1', 'lambda': 'q2'})
# teste12.inserir(estado='q2', final=True, transicoes={'2': 'q2'})
# print(teste12.reconhecer('2'))
# teste12.mostrar_linguagem(3)

# Linguagem = Figura 2.9 Equivalente ao AFN14 * Autômato Finito Não-Determinístico
# teste13 = Automato(nome='AFN13', alfabeto={'0', '1'})
# teste13.inserir(estado='q0', final=False, transicoes={'0': {'q0', 'q1'}})
# teste13.inserir(estado='q1', final=True, transicoes={'1': 'q2'})
# teste13.inserir(estado='q2', final=False, transicoes={'0': 'q1'})
# teste13.mostrar_linguagem(6)

# Linguagem = Figura 2.15 Equivalente ao AFN13 * Autômato Finito Não-Determinístico
# teste14 = Automato(nome='AFN14', alfabeto={'0', '1'})
# teste14.inserir(estado='q0', final=False, transicoes={'0': 'q0', 'lambda': 'q1'})
# teste14.inserir(estado='q1', final=False, transicoes={'0': 'q2'})
# teste14.inserir(estado='q2', final=True, transicoes={'1': 'q1'})
# teste14.mostrar_linguagem(7)

# Linguagem = Figura 2.16 AFD Equivalente ao AFN14
# teste15 = Automato(nome='AFD15', alfabeto={'0', '1'})
# teste15.inserir(estado='q0', final=False, transicoes={'0': 'q1', '1': 'q4'})
# teste15.inserir(estado='q1', final=True, transicoes={'0': 'q1', '1': 'q2'})
# teste15.inserir(estado='q2', final=False, transicoes={'0': 'q3', '1': 'q4'})
# teste15.inserir(estado='q3', final=True, transicoes={'0': 'q4', '1': 'q2'})
# teste15.inserir(estado='q4', final=False, transicoes={'0': 'q4', '1': 'q4'})
# teste15.mostrar_linguagem(7)

# Linguagem = Exercício 2 Cap. 2
# teste16 = Automato(nome='AFD16', alfabeto={'0', '1'})
# teste16.inserir(estado='q0', final=False, transicoes={'0': 'q0', '1': 'q1'})
# teste16.inserir(estado='q1', final=False, transicoes={'0': 'q0', '1': 'q2'})
# teste16.inserir(estado='q2', final=False, transicoes={'0': 'q3', '1': 'q2'})
# teste16.inserir(estado='q3', final=True, transicoes={'0': 'q3', '1': 'q1'})
# print(f'0001 {teste16.reconhecer("0001")}')
# print(f'01001 {teste16.reconhecer("010011")}')
# print(f'0000110 {teste16.reconhecer("0000110")}')

# Linguagem = {w 1 ∈ {0, 1}* / w = (001)n , n >= 0} (Exercício 3 Cap. 2)
# teste17 = Automato(nome='AFD17', alfabeto={'0', '1'})
# teste17.inserir(estado='q0', final=False, transicoes={'0': 'q2', '1': 'q1'})
# teste17.inserir(estado='q1', final=True, transicoes={'0': 'qm', '1': 'qm'})
# teste17.inserir(estado='q2', final=False, transicoes={'0': 'q3', '1': 'qm'})
# teste17.inserir(estado='q3', final=False, transicoes={'0': 'qm', '1': 'q4'})
# teste17.inserir(estado='q4', final=False, transicoes={'0': 'q2', '1': 'q1'})
# teste17.inserir(estado='qm', final=False, transicoes={'0': 'qm', '1': 'qm'})
# print(f'1 {teste17.reconhecer("1")}')
# print(f'0011 {teste17.reconhecer("0011")}')
# print(f'0010011 {teste17.reconhecer("0010011")}')
# print(f'0010010011 {teste17.reconhecer("0010010011")}')
# teste17.mostrar_linguagem(13)

# Linguagem = Exercícios 4(a, b) Cap. 2
# AFD4a = Automato(nome='AFD4a', alfabeto={'a', 'b', 'c', 'd'})
# AFD4b = Automato(nome='AFD4b', alfabeto={'a', 'b', 'c', 'd'})

# Qualquer cadeia consistindo somente de 'a'
# AFD4a.inserir('q0', final=False, transicoes={'a': 'q1', 'b': 'q2', 'c': 'q2', 'd': 'q2'})
# AFD4a.inserir('q1', final=True, transicoes={'a': 'q1', 'b': 'q2', 'c': 'q2', 'd': 'q2'})
# AFD4a.inserir('q2', final=False, transicoes={'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q2'})
# AFD4a.mostrar_linguagem()

# Qualquer cadeia terminando com um 'a'
# AFD4b.inserir('q0', final=False, transicoes={'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0'})
# AFD4b.inserir('q1', final=True, transicoes={'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0'})
# AFD4b.mostrar_linguagem(3)

# Exercício 20 Cap. 2
# AFN2_23 = Automato(nome='AFN2_23', alfabeto={'0', '1'})
# AFN2_23.inserir('q0', final=False, transicoes={'0': 'q0', '1': {'q0', 'q1'}})
# AFN2_23.inserir('q1', final=False, transicoes={'1': 'q2'})
# AFN2_23.inserir('q2', final=False, transicoes={'1': 'q3'})
# AFN2_23.inserir('q3', final=True, transicoes={'0': 'q3'})
# print(f'00 {AFN2_23.reconhecer("00")}')
# print(f'0100010 {AFN2_23.reconhecer("0100010")}')
# print(f'10010 {AFN2_23.reconhecer("10010")}')
# print(f'000 {AFN2_23.reconhecer("000")}')
# print(f'0000 {AFN2_23.reconhecer("0000")}')
# AFN2_23.mostrar_linguagem()

# AFN2_24 = Automato(nome='AFN2_24', alfabeto={'0', '1'})
# AFN2_24.inserir('q0', final=False, transicoes={'1': 'q1'})
# AFN2_24.inserir('q1', final=True, transicoes={'0': {'q0', 'q2'}, '1': {'q1', 'q2'}, 'lambda': 'q0'})
# AFN2_24.inserir('q2', final=False, transicoes={'0': 'q2', '1': 'q1'})
# AFN2_24.mostrar_linguagem(4)

# AFN2_25 = Automato(nome='AFN2_25', alfabeto={'a', 'b'})
# AFN2_25.inserir('q0', final=False, transicoes={'a': 'q2', 'lambda': 'q1'})
# AFN2_25.inserir('q1', final=False, transicoes={'b': 'q2'})
# AFN2_25.inserir('q2', final=False, transicoes={'a': {'q2', 'q3'}})
# AFN2_25.inserir('q3', final=True, transicoes={'b': {'q0', 'q3'}})
# AFN2_25.mostrar_linguagem(4)
# AFN2_25.buscar_cnr(3)

# AFN2_26 = Automato(nome='AFN2_26', alfabeto={'a', 'b'})
# AFN2_26.inserir('q0', final=False, transicoes={'a': 'q2', 'b': 'q3', 'lambda': 'q1'})
# AFN2_26.inserir('q1', final=False, transicoes={'lambda': {'q2', 'q3'}})
# AFN2_26.inserir('q2', final=True, transicoes={'a': 'q2', 'b': 'q4'})
# AFN2_26.inserir('q3', final=True, transicoes={'a': 'q4', 'b': 'q3'})
# AFN2_26.inserir('q4', final=False, transicoes={'a': {'q1', 'q5'}, 'b': {'q1', 'q5'}})
# AFN2_26.inserir('q5', final=False, transicoes={'a': 'q2', 'b': 'q3'})
# AFN2_26.mostrar_linguagem(4)
# AFN2_26.buscar_cnr()

# AFN2_27 = Automato(nome='AFN2_27', alfabeto={'a', 'b'})
# AFN2_27.inserir('q0', final=False, transicoes={'a': 'q1', 'b': 'q3'})
# AFN2_27.inserir('q1', final=False, transicoes={'lambda': {'q2', 'q3'}})
# AFN2_27.inserir('q2', final=True, transicoes={'a': {'q0', 'q2'}, 'b': 'q4'})
# AFN2_27.inserir('q3', final=True, transicoes={'a': 'q4', 'b': 'q3'})
# AFN2_27.inserir('q4', final=False, transicoes={'a': 'q4', 'b': 'q4', 'lambda': 'q1'})
# AFN2_27.mostrar_linguagem(4)
# AFN2_27.buscar_cnr()

# AFD não mínimo que reconhece os números em binário múltiplos de 6
# AFD2_30 = Automato(nome='AFD2_30', alfabeto={'0', '1'})
# AFD2_30.inserir('q0', final=True, transicoes={'0': 'q0', '1': 'q1'})
# AFD2_30.inserir('q1', final=False, transicoes={'0': 'q2', '1': 'q3'})
# AFD2_30.inserir('q2', final=False, transicoes={'0': 'q4', '1': 'q5'})
# AFD2_30.inserir('q3', final=False, transicoes={'0': 'q0', '1': 'q1'})
# AFD2_30.inserir('q4', final=False, transicoes={'0': 'q2', '1': 'q3'})
# AFD2_30.inserir('q5', final=False, transicoes={'0': 'q4', '1': 'q5'})
# AFD2_30.mostrar_linguagem(4)
# AFD2_30.buscar_cnr(5)

AFD3_13 = Automato(nome='AFD3_13', alfabeto={'a', 'b'})
AFD3_13.inserir('S', final=False, transicoes={'a': 'q1'})
AFD3_13.inserir('q1', final=False, transicoes={'b': 'A'})
AFD3_13.inserir('A', final=False, transicoes={'b': 'q2'})
AFD3_13.inserir('q2', final=False, transicoes={'a': 'B'})
AFD3_13.inserir('B', final=False, transicoes={'a': 'A', 'b': 'q3'})
AFD3_13.inserir('q3', final=False, transicoes={'b': 'q4'})
AFD3_13.inserir('q4', final=True)
AFD3_13.mostrar_linguagem(10)
AFD3_13.mostrar_linguagem(7, 13)
