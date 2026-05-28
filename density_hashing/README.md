# partionnement de l'espace par densité à priori et recherche d'esperance $\mathcal{O}(1)$

Le but ici est de trouver un partionnement de l'espace optimal pour une recherche du plus proche voisin lorsque la distribution des points n'est pas uniforme. 

l'optimum est d'avoir une case par point. chaque case a un cout de recherche $\mathcal{O}(1)$ et le point par case a un cout de recherche $\mathcal{O}(n)$

il suffit alors de partionner l'espace de sorte a ce que l'esperance de la case de contenir un point soit égale à $\frac{\int_{a}^{b}f(x)dx}{N}$ avec $f(x)$ la focntion de densité

et $a$ et $b$ le domaine de définition de l'échantillonnage de $f$ et $N$, le nombre d'échantillons. 

prenons l'exemple d'une gaussienne 1D

le partitionnement de cette gaussienne se fait de la manière suivante. 

$$
\begin{align}
E(X \in [A, B]|N) = 1 &= \Big(b\ \text{tq} \ \int_{A}^{b} f(x)dx = \frac{\int_{A}^{B} f(x)dx}{N}\Big) - A\\
intervalle &= B - A\\
\text{nombre de cellules} &= \bigg\lfloor\frac{intervalle}{E(X \in [A, B]) = 1} \bigg\rfloor \\
\text{taille de la cellule} &=  \frac{intervalle}{\text{nombre de cellules}}
\end{align}
$$

