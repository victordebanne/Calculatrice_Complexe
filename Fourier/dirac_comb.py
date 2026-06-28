import matplotlib.pyplot as plt
import random as r


def dirac_comb(size, nb_dirac):
  array = [0 for i in range(size)]
  for i in range(nb_dirac):
    index = r.randint(0, size - 1)
    array[index] = 1
  return array

def periodic_dirac(x, epsilon = 0.01):
  out = 0
  mod = x % 1
  if - epsilon <= mod <= epsilon:
    out = 1
  return out

def analysis(comb):
  size = len(comb)
  nb_frequencies = int(size - size/2)
  max_phases = int(1/(2 * (size/2)))
  #la sortie est une matrice des fréquences et des phases
  out = [[0 for i in range(nb_frequencies)]for j in range(max_phases)]

  #pour chaque fréquence possible
  for f in range(size/2, size + 1):
    nb_phases = int(1/(2 * f))
    #pour chaque phase possible
    for phi in range(nb_phases):
      #pour chaque valeur de x
      total = 0
      for i in range(size):
        total += 1 / ((comb[i] - periodic_dirac(f * i + phi)) ** 2 + 0.01)

    out[f - (size/2)][phi] = total

  return out

X = dirac_comb(100, 20)
plt.plot(list(range(len(X))), X)
plt.show()
