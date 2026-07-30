"""
CONSTRUCTION TENSEUR RECURSIF POUR GRAPH DE TRANSITIONS
"""

import copy

def parse(string):
    array = []
    temp = ""
    for char in string:
        if char == "-":
            array.append(int(temp))
            temp = ""
        else : 
            temp += char
    array.append(int(temp))
    return array

def convert(K, array):
    if K > 26 : 
        raise ValueError("on ne peut pas convertir pour des K > 26")
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    B = []
    for i in range(len(A)):
        B.append(A[i])
       
    converted = ""
    for i in range(len(array)):
        s_i = array[i] // K
        s_j = array[i] % K
        
        if i == 0 : converted += A[s_i] + A[s_j]
        else : converted += " " + A[s_i] + A[s_j]
    return converted

def convert_matrix(matrix):
    K = len(matrix)
    out = [[None for j in range(K)] for i in range(K)]
    for i in range(K):
        for j in range(K):
            out[i][j] = convert(K, parse(matrix[i][j]))
    return out
            
def print_matrix(matrix, convert = False):
    if convert : 
        matrix = convert_matrix(matrix)
    for i in range(len(matrix)):
        print(matrix[i])
    print("")
        
def print_tensor(tensor):
    if type(tensor) == list:
        if type(tensor[0]) == list:
            if type(tensor[0][0]) != list:
                print_matrix(tensor, True)
            else : 
                for i in range(len(tensor)):
                    print_tensor(tensor[i])
        else : 
            print("/!\ mauvais format ?")
            print(tensor)
    else :
        print("/!\ mauvais format ?")
        print(tensor)
      
class Tensor():
    def __init__(self, K, N):
        
        #tensor construction
        self.K = K
        self.N = N
        self.tensor = self.recursive_tensor_generator()
        
        #tensor analysis
        self.C_V = None
        
        self.nb_elements = None
        self.nb_doublons = None
        self.doublons_counting = None
        self.nb_singletons = None
         
    def recursive_add(self, tensor, index = None):
        if index == None:
            index = []
            
        if type(tensor) == list:
            for i in range(self.K):
                new_index = index + [i]
                tensor[i] = self.recursive_add(tensor[i], new_index)
                  
        else : 
            tensor = str(self.K * index[0] + index[1]) + "-" + tensor
            
        return tensor
    
    def recursive_tensor_generator(self, current_lvl = None, tensor = None):
        if tensor == None :
            current_lvl = 2
            tensor = [[str((self.K * i) + j) for j in range(self.K)] for i in range(self.K)]
            
        if current_lvl == self.N : 
            return tensor
        
        else : 
            new_tensor = [None for i in range(self.K)]
            
            for i in range(self.K):
                new_tensor[i] = copy.deepcopy(tensor)
                
            self.recursive_add(new_tensor)
            current_lvl += 1
            
            return self.recursive_tensor_generator(current_lvl, new_tensor)
        
    def display(self):
        print_tensor(self.tensor)
        
    def counting_vectors(self, tensor = None, index = None):
        #vecteurs de comptage, nombre, indexs
        #nombre de doublons 
        #nombre de singletons
        
        if tensor == None : 
            tensor = self.tensor
            self.C_V = []
        if index == None : index = []
        
        if type(tensor) == list:
            if type(tensor[0]) == list:
                if type(tensor[0][0]) != list:
                    
                    for i in range(self.K):
                        for j in range(self.K):
                            new_index = index + [i, j]
                            c_v = [0 for i in range(self.K ** 2)]
                            array = parse(tensor[i][j])
                            for k in array:
                                c_v[k] += 1
                            if self.C_V == []:
                                self.C_V.append([c_v, [new_index], 1])
                            else : 
                                found = False
                                for l in range(len(self.C_V)):
                                    if c_v == self.C_V[l][0]:
                                        self.C_V[l][1].append(new_index)
                                        self.C_V[l][2] += 1
                                        found = True
                                        break
                                    
                                if not found : 
                                    self.C_V.append([c_v, [new_index], 1])
                                
                else : 
                    for i in range(len(tensor)):
                        new_index = index + [i]
                        self.counting_vectors(tensor[i], new_index)
                        
    def analysis(self, disp_vect = False):
        self.counting_vectors()
        
        self.nb_doublons = 0
        self.doublons_counting = []
        self.nb_singletons = 0
        self.nb_elements = self.K ** self.N
        
        for v in self.C_V:
            if v[2] == 1 : self.nb_singletons += 1
            else : 
                self.nb_doublons += 1
                if self.doublons_counting == [] : 
                    self.doublons_counting.append([v[2], 1])
                else : 
                    found = False
                    for d in self.doublons_counting : 
                        if v[2] == d[0] : 
                            d[1] += 1
                            found = True
                            break
                    if not found : 
                        self.doublons_counting.append([v[2], 1])
                        
        print(f"\n==== ANALYSE K = {self.K}, N =  {self.N} ====\n\n")
            
        print("nb elements total = ", self.K ** self.N)        
        print("nb doublons differents = ", self.nb_doublons)
        print("nb doublons total = ", self.K ** self.N - self.nb_singletons)
        print("nb singletons = ", self.nb_singletons)
        
        
        print("")
        
        self.doublons_counting.sort(key = lambda x : x[0])
        
        for  i in range(len(self.doublons_counting)):
            a = self.doublons_counting[i][0]
            b = self.doublons_counting[i][1]
            print("nb doublons à", a, ":", b, "total : ", a * b)
                    
        print("")
        
        if disp_vect:
            for i in range(len(self.C_V)):
                print(self.C_V[i])
                print("")
                
def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
    
def inclusion_exclusion(K, N):
    tensors = []
    for i in range(K):
        tensors.append(Tensor(i + 1, N))
        tensors[i].analysis()
    tensors.reverse()
    
    #formule d'inclusion exclusion : 
    #le nombre de séquences avec exactement K sommets : 
    #f(K, N) = K^N - [\sum_{k = 1}^{K - 1} C(K - 1, k) * f(k, N)]
    #ou bien \sum_{k = 1}^{K} (-1)^k C(K, k) * (K - k)^N
    nb_total = 0
    nb_doublons_differents = 0
    nb_singletons = 0
    
    doublons_counting_total = []
    
    
    
    for i in range(len(tensors)):
        nb_total += (-1)**i * binom(K, i) * tensors[i].nb_elements
        nb_doublons_differents += (-1)**i * binom(K, i) * tensors[i].nb_doublons
        nb_singletons += (-1)**i * binom(K, i) * tensors[i].nb_singletons
        for j in range(len(tensors[i].doublons_counting)):
            key = tensors[i].doublons_counting[j][0]
            total = (-1)**i * binom(K, i) * tensors[i].doublons_counting[j][1]
            
            if doublons_counting_total == []:
                doublons_counting_total.append([key, total])
            else :
                found = False
                for k in range(len(doublons_counting_total)):
                    if doublons_counting_total[k][0] == key : 
                        doublons_counting_total[k][1] += total  
                        found = True
                        break
                if not found : 
                    doublons_counting_total.append([key, total])
                    
    print(f"\n==== ANALYSE EXACTEMENT K = {K}, N =  {N} ====\n\n")
        
    print("nb elements total = ", nb_total) 
    print("nb doublons differents= ", nb_doublons_differents)  
    print("nb doublons = ", nb_total - nb_singletons)  
    print("nb singletons = ", nb_singletons)  
    print("")
    
    for  i in range(len(doublons_counting_total)):
        a = doublons_counting_total[i][0]
        b = doublons_counting_total[i][1]
        print("nb doublons à", a, ":", b, "total : ", a * b)
                
    print("")
    
    
        
    
        
    
    
        
        
    
    

            
inclusion_exclusion(6, 7)
            
        
    
#T = Tensor(2, 6)

#T.analysis()


        

    
    



            
        
            
        
            
            

    
    
    


