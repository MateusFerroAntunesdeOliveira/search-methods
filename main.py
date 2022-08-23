# Imports
import sys
import csv
from math import sqrt, pow

# Given a Matrix and a value, find the coords (i,j).
def findPosition(matriz, m, n, valor):
    # Empty List posicoes
    posicoes = []
    
    for i in range(0, m):
        for j in range(0, n):
            if matriz[i][j] == valor:
                # Add the respective position to the posicoes list
                posicoes.append((i, j))
    return posicoes


# Given a Matrix and the current position by coords (i,j), find successor states with 1 step from (i,j)
def findStates(matriz, m, n, posicao_atual):
    # Set positions and Initialize sucessorStates list
    i = posicao_atual[0]
    j = posicao_atual[1]
    estados_sucessores = []
    
    # Move UP
    if i > 0 and matriz[i-1][j] != "2":
        estados_sucessores.append((i-1, j))
    # Move Down
    if i+1 < m and matriz[i+1][j] != "2":
        estados_sucessores.append((i+1, j))
	# Move Left
    if j > 0 and matriz[i][j-1] != "2":
        estados_sucessores.append((i, j-1))
    # Move Right
    if j+1 < n and matriz[i][j+1] != "2":
        estados_sucessores.append((i, j+1))
    # Move to TopLeft
    if j > 0 and i > 0 and matriz[i-1][j-1] != "2":
        estados_sucessores.append((i-1, j-1))
    # Move to BottomLeft
    if j > 0 and i+1 < m and matriz[i+1][j-1] != "2":
        estados_sucessores.append((i+1, j-1))
    # Move to TopRight
    if j+1 < n and i > 0 and matriz[i-1][j+1] != "2":
        estados_sucessores.append((i-1, j+1))
    # Move to BottomRight
    if j+1 < n and i+1 < m and matriz[i+1][j+1] != "2":
        estados_sucessores.append((i+1, j+1))
    return estados_sucessores


# Shows in which iteration the solution was found and how to start from the initial state 
# and reach the final state from the partial solution stored in predecessors.
def showSolution(estado, predecessores, iteracao):
	caminho = []
	caminho.append(estado)
	print("Solucao encontrada na iteracao " + str(iteracao) + ":")
	while predecessores[estado] != None:
		caminho.append(predecessores[estado])
		estado = predecessores[estado]
	caminho = caminho[::-1]
	print(caminho)


# Given any state and a set of end states, calculate the distance from any state to the nearest end state.
def targetDistance(estado, estados_finais):
	x = estado[0]
	y = estado[1]
	distancia_minima = 1000000000

	for estado_final in estados_finais:
		x_estado_final = estado_final[0]
		y_estado_final = estado_final[1]
		diff1 = x_estado_final - x
		diff2 = y_estado_final - y
		somaDiffs = pow(diff1, 2) + pow(diff2, 2)
		distancia_atual = sqrt(somaDiffs)
		if distancia_atual < distancia_minima:
			distancia_minima = distancia_atual
	return distancia_minima


# Given a fringe and a heuristic function, finds the state with the lowest value in that fringe.
def promisingState(franja, heuristica_estados):
	valor_mais_promissor = 1000000000
	estado_mais_promissor = None
	indice_mais_promissor = 0
	indice = 0
	for estado in franja:
		if heuristica_estados[estado] < valor_mais_promissor:
			estado_mais_promissor = estado
			valor_mais_promissor = heuristica_estados[estado]
			indice_mais_promissor = indice
		indice = indice + 1
	return indice_mais_promissor


# Given a queue with some states, shows each one of them.
def showStates(fila):
	print("===================================")
	print("Estados para analisar")
	for estado in fila:
		print(str(estado))
	print("===================================")


# Given a fringe with some states, shows the heuristic value of each one of them.
def showValues(franja, heuristica):
	print("===================================")
	print("Valores da franja")
	for estado in franja:
		print("V_" + str(estado) + " = " + str(heuristica[estado]))
	print("===================================")


# TODO - Impelements Breadth-First Search


# TODO - Implements A*


# Main flow - Use python main.py content/duende.csv
if len(sys.argv) == 2:
	problema = open(sys.argv[1])
	leitor_problema = csv.reader (problema)
	entrada = list(leitor_problema)
	m = int(entrada[0][0]) # Row number
	n = int(entrada[0][1]) # Column number
	matriz = entrada[1:] # Map

	estado_inicial = findPosition(matriz, m, n, "3")
	estados_finais = findPosition(matriz, m, n, "0")
	print ("Matriz (mapa): ")
	print (str(matriz))
	print ("Estado Inicial: " + str(estado_inicial))
	print ("Estado Final: " + str(estados_finais))
 
	# TODO - Call the functions
else:
    print("Provides a CSV file for the search algorithms")
