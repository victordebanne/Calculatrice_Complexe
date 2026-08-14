"""
Pliage
"""
import random as r

def create_comb(nb, a = 0, b = 10, precision = 1):
    size = (b - a) * 10 ** precision
    array = [0 for i in range(size)] 
    
    for i in range(nb):
        x = r.randint(0, size - 1)
        y = 1
        array[x] = y
        
    return array

def fold(array, p):
    folded = [0 for i in range(p)]
    for i in range(len(array)):
        if (i // p) % 2 == 0:
            folded[i % p] += array[i]
        else :
            folded[p - 1 - (i % p)] += array[i]
            
    return folded

def periodic_dirac(p, phi, x):
    phi = phi % p
    #p la période
    #phi la phase, quand phi = 0, p_d(0) = 1
    
    if (x - phi) % p == 0:
        return 1
    else :
        return 0
    
def error_compute(u, v):
    total = 0
    for i in range(len(u)):
        total += abs(u[i] - v[i])
    
    return total

def sub(u, v):
    out = []
    for i in range(len(u)):
        out.append(u[i] - v[i])
    
    return out

import matplotlib.pyplot as plt

def analysis(array, out, a, p, phi):
    error = error_compute(array, out)
    plt.title(f"error = {error}, a = {a}, p = {p}, phi = {phi}")
    for i in range(len(array)):
        plt.scatter(i, array[i] + 3, color = "blue")
        plt.scatter(i , out[i] , color = "red")
    plt.show()
    
def display_comb(comb):
    for i in range(len(comb)):
        plt.scatter(i, comb[i], color = "blue")
    plt.show()

def comb_transform(array, f_min = 2, a = 0, b = 10, precision = 1, epsilon = 0.5):
    coefficient = [] #les coefficients sont des tuples (a, p, phi)
    #amplitude(signe), période, phase
    
    size = (b - a) * 10 ** precision
    
    out = [0 for i in range(size)] 
    #out est la liste sur laquelle l'algorithme itère
    
    
    while True:
        error = error_compute(array, out)
        
        diff = sub(array, out)
        
        best_error = float("inf")
        best_p = None
        best_phi = None
        best_a = None
        
        for p in range(1, size // f_min):
            folded = fold(diff, p)
            max_folded = max(folded)
            min_folded = min(folded)
            
            phi = None
            a = None
            
            if abs(min_folded) > max_folded:    
                phi = folded.index(min_folded)
                a = - 1
            else : 
                phi = folded.index(max_folded)
                a = 1
        
            new_error = 0 
            for i in range(len(out)):
                new_error += abs(array[i] - (out[i] + a * periodic_dirac(p, phi, i)))
                    
            if new_error < best_error:
                best_error = new_error
                best_p = p
                best_phi = phi
                best_a = a
                    
        if best_error >= error : 
            break
            
                        
        for i in range(len(out)):
            out[i] += best_a * periodic_dirac(best_p, best_phi, i)
            
        coefficient.append([best_a, best_p, best_phi])
        
        #analise (pas algo)
        analysis(array, out, best_a, best_p, best_phi)
        
    return coefficient

def inverse_comb_transform(coefficient, a = 0, b = 10, precision = 1):
    size = (b - a) * 10 ** precision
    out = [0 for i in range(size)] 
    
    for i in range(len(coefficient)):
        a = coefficient[i][0]
        p = coefficient[i][1]
        phi = coefficient[i][2]
        
        for j in range(len(out)):
            out[j] += a * periodic_dirac(p, phi, j)
            
    return out

comb = create_comb(10, b = 10)

coeffs = comb_transform(comb, b = 10,f_min = 1)

new_comb = inverse_comb_transform(coeffs)

display_comb(new_comb)
                
                
            
            
            
            
        
        
