
paths = []


def hamiltonian_path(K, current, allowed = None, length = None, path = None):
    if length == K - 1 :
        paths.append(path)
        return
    
    if allowed == None : 
        allowed = [i for i in range(K)]
        length = 1
        path = [current]
    allowed.pop(allowed.index(current[0]))
        
    i_next = current[1]
    for j_next in allowed:
        if j_next == i_next : 
            continue
        new = [i_next, j_next]
        new_length = length + 1
        new_path = path.copy()
        new_path.append(new)
        new_allowed = allowed.copy()
        hamiltonian_path(K, new, new_allowed, new_length, new_path)
  
K = 5
  
for i in range(K):
    for j in range(K):
        if i == j :
            pass
        else:
            hamiltonian_path(K, [i, j])

#hamiltonian_path(K, [0, 1])
            
for i in range(len(paths)):
    print(paths[i])

        
        
    
    
