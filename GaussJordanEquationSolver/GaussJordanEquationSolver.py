#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EQUATION SOLVER
"""

def solver(M, V):
    size = len(M)
    M_out = [[M[i][j] for j in range(size)] for i in range(size)]
    V_out = [V[i] for i in range(size)] 
    
    #n compte les pivots utilisé
    n = 0

    #pour chaque variables : 
    for i in range(size):
        pivot = None
        #les pivots utilisés sont rangés du début vers la fin
        #on itère seulement sur les pivots non utilisés
        for j in range(n, size):
            if M_out[j][i] != 0 :
                pivot = j
                #on élimine sur toutes les lignes de la matrice
                #sauf le pivot
                for k in range(j + 1, size + j):
                    m_k = k % size
                    K = M_out[m_k][i]/M_out[j][i]
                    #on fait l'élimination sur toutes les variables non annulées précédemment
                    for l in range(i, size):
                        M_out[m_k][l] -= M_out[j][l] * K
                    V_out[m_k] -= V_out[j] * K
                break
        #on échange la ligne pivot utilisée 
        #de sort a obtenir une matrice diagonale
        #   X 0 0 
        #   0 Y 0 
        #   0 0 Z 
        if pivot != None:
            M_out[pivot], M_out[n] = M_out[n], M_out[pivot]
            V_out[pivot], V_out[n] = V_out[n], V_out[pivot]
            
            n += 1
            
    #une fois la matrice devenue diagonale, on divise V par la digonale
    for i in range(size):
        if M_out[i][i] != 0 : 
           V_out[i] /= M_out[i][i]
        else : 
            V_out[i] = 'f'
            
    return V_out
                  
import random as r
def eq_gen():
    m_i = r.randint(2, 10)
    M = [[r.randint(0, 10) for i in range(m_i)]for i in range(m_i)]
    V = [r.randint(0, 10) for i in range(m_i)]
    return M, V

def verifier(M, V, R):
    m_i = len(M)
    for i in range(m_i):
        total = 0
        for j in range(m_i):
            total += M[i][j] * R[j]
        print(round(total - V[i], 12))
            
#print(linear_equation_solver(M, V))

for i in range(100):
    E = eq_gen()
    M = E[0]
    V = E[1]
    R = solver(M, V)
    verifier(M, V, R)
        
