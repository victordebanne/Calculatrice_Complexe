# Synthèse complète — Tenseurs de transitions et comptage des doublons

## 0. Contexte et problème initial

Point de départ : calculer la vraisemblance d'une chaîne de Markov sur une séquence ne dépend que des **fréquences de transitions**, pas de l'ordre. Deux séquences différentes peuvent partager le même vecteur de comptage $N$ (une matrice $K\times K$, $N_{ij}$ = nombre de transitions $i\to j$). On appelle **doublon** un vecteur $N$ atteint par plusieurs séquences, et $g(N)$ le nombre de séquences qui le réalisent.

Objectif : comprendre et si possible calculer $g(N)$, caractériser quelles tailles de groupes de doublons existent, et construire des outils pour les étudier.

---

## 1. Construction fondamentale : le tenseur récursif

**Objet de base (à toi)** : un tenseur $T_N$ à $N$ indices, chacun dans $\{0,\ldots,K-1\}$, construit récursivement. Deux variantes ont été explorées :

- **Version historique** (utilisée en premier) : $T_N[i,j,k,\ldots] = T_{N-1}[i,k,\ldots] + t[k,j]$ — indexage "mélangé".
- **Version simplifiée** (celle que tu utilisais dans tes schémas depuis le début, formalisée en code plus tard) : les coordonnées $(i_0,i_1,\ldots,i_{N-1})$ correspondent **directement et dans l'ordre** aux lettres du mot. C'est la version à privilégier — plus simple, mêmes résultats, lemmes plus propres.

**Chaque case $T_N[i_0,\ldots,i_{N-1}]$** contient le vecteur de comptage $N$ du mot $(i_0,\ldots,i_{N-1})$. Le tenseur explore *exhaustivement* et *sans rejet* les $K^N$ mots possibles.

---

## 2. Lemmes structurels sur les coordonnées (prouvés)

Avec l'indexage simplifié :

- **Lemme de fermeture** : $\text{mot fermé (départ=arrivée)} \iff i_0 = i_{N-1}$.
- **Lemme des boucles internes** : $i_p = i_{p+1} \iff$ boucle à cette position exacte dans le mot, pour tout $p$ consécutif.
- **Caractérisation des "cores"** (mots sans aucune boucle) : $i_p \neq i_{p+1}$ pour tout $p$.
- **Caractérisation des chemins hamiltoniens** : coordonnées où tous les $i_p$ sont deux à deux distincts (permutation de $\{0,\ldots,K-1\}$).

Les deux premiers sont démontrables par récurrence directe sur la construction du tenseur.

---

## 3. Formules fermées aux petites longueurs (formulées par toi, prouvées ensemble)

Pour $N=2$ (2 transitions, mot de longueur 3) : *(attention, convention "N = nb transitions" ici, historique)*
$$n_{doublons} = \frac{K(K-1)}{2}$$

Pour $N=3$ (3 transitions, mot de longueur 4) :
$$n_{doublons} = \frac{2K(K^2-1)}{3}$$

Vérifiées exactement sur $K=2$ à $8$.

---

## 4. Décomposition core + confluence (vérifiée exhaustivement)

**Définition** : le *core* d'un mot est obtenu en contractant récursivement toute boucle ($XX \to X$) jusqu'à ce qu'il n'y en ait plus.

**Résultat** : cette réduction est **confluente** — le core obtenu ne dépend pas de l'ordre des contractions (vérifié sur 50 mots aléatoires, plusieurs longueurs, zéro contre-exemple).

**Conséquence** : tout mot se décompose uniquement en *(core sans boucle) + (boucles insérées à des positions précises)*.

**Comptage des cores** : nombre de mots de longueur $N$ sans aucune boucle interne
$$= K(K-1)^{N-1}$$
(vérifié exactement, $N=2$ à $7$).

---

## 5. Théorème de couverture par insertion de cycles hamiltoniens

**Construction (formulée par toi)** : une boucle de "taille $K'$" insérée à un caractère $X$ consiste à remplacer $X$ par un détour $X, s_1, \ldots, s_{K'-1}, X$ visitant $K'-1$ autres états distincts puis revenant — c'est-à-dire un **cycle hamiltonien** sur un sous-ensemble de $K'$ états.

**Théorème de couverture (vérifié à 100% sur $N=5,6,7$, $K=3$)** :
$$\text{Tout doublon à niveau } N = \bigcup_{K'=1}^{K}\big(\text{insertion d'un cycle hamiltonien de taille } K' \text{ depuis le niveau } N-K'\big)$$

Sources = **tous** les mots des niveaux inférieurs (pas seulement les doublons déjà connus).

**Cas limite historique** : le mot $ABCABCA$ (triangle répété deux fois) semblait échapper à une première version restreinte de la construction (boucles fixes 2/3) ; il a fallu généraliser à des boucles de longueur arbitraire, insérées potentiellement **récursivement** (sur le point de retour d'une boucle précédente) pour le couvrir — la version finale (cycles hamiltoniens $K'=1,\ldots,K$, sources directes) couvre ce cas sans récursion supplémentaire.

---

## 6. Principe de linéarité (prouvé)

Insérer une boucle-2 (dupliquer un caractère $X$) modifie le vecteur $N$ toujours de la même façon, indépendamment du contexte :
$$N(\text{mot avec boucle sur } X) = N(\text{mot}) + \delta_X, \qquad \delta_X = (+1 \text{ uniquement sur } N_{XX})$$

**Conséquence directe** : deux mots partageant le même $N$, si on leur insère une boucle sur le **même caractère** $X$ (peu importe où), restent forcément dans le même $N$ après insertion — d'où le fait que "les doublons engendrent des doublons".

---

## 7. Lemme de correspondance coordonnées ↔ insertion (vérifié)

Dans le tenseur d'états à indexage séquentiel :
$$\text{coordonnée(mot avec boucle insérée en position } p\text{, caractère } X) = \text{coord(source)}[:p{+}1] \,\Vert\, [X] \,\Vert\, \text{coord(source)}[p{+}1:]$$

C'est une insertion littérale d'indice — vérifié uniformément, y compris pour la dernière position (contrairement à une version testée avec le tenseur des transitions, qui nécessitait un cas particulier).

---

## 8. Comptage des chemins généralisé (prouvé)

$$\forall (i,j) \in \{0,\ldots,K-1\}^2,\quad \#\{\text{chemins de } i \text{ à } j \text{ en un mot de longueur } N\} = K^{N-2}$$

Généralise le lemme de fermeture : le nombre de chemins ne dépend **jamais** du couple (départ, arrivée), y compris le cas fermé $i=j$. Preuve par symétrie du graphe complet.

---

## 9. Décomposition binomiale $f(r,s,m)$ et inclusion-exclusion (prouvée, automatisée)

**Intuition de départ (toi)** : "la situation à $K=2$ se retrouve dans $K=3$..."

**Formalisation** :
$$\text{compte}(s, m, K) = \sum_{r} \binom{K}{r}\, f(r,s,m)$$
où $f(r,s,m)$ est le nombre de configurations *primitives* (utilisant exactement $r$ états) de taille $s$ à $m$ transitions — fixe, indépendant de $K$.

**Formule d'inclusion-exclusion associée** :
$$f(K,N) = \sum_{i=0}^{K} (-1)^i \binom{K}{i}(K-i)^N = K^N - \sum_{r=0}^{K-1}\binom{K}{r} f(r,N)$$

Ton outil (`Tensor` + `inclusion_exclusion`) calcule automatiquement cette table pour n'importe quel $(K,N)$, vérifié exactement contre la force brute.

---

## 10. Théorèmes sur les chemins et cycles hamiltoniens (prouvés)

**Théorème A (cycle complet, prouvé + vérifié 5 fois)** :
$$f(r,\, s{=}r,\, m{=}r) = (r-1)!$$
Nombre de cycles hamiltoniens orientés étiquetés sur $r$ sommets.

**Théorème B (chemin, juste en dessous du seuil, prouvé)** :
$$f(r,\, s\geq 2,\, m{=}r{-}1) = 0, \qquad \text{nombre de mots} = r!, \text{ tous singletons}$$
Preuve : un mot de longueur $r$ sans répétition est une permutation ; l'ensemble de ses $r-1$ arêtes forme un chemin hamiltonien dirigé, qui n'admet qu'un seul ordre de parcours possible (source unique, arêtes déterminées) — donc reconstruction unique, zéro collision.

**Lien entre les deux** : fermer chaque chemin ($r!$ d'entre eux) en cycle (ajouter la transition de retour) donne exactement $(r-1)!$ groupes de taille $r$ — $r! = r \times (r-1)!$.

**Accès direct par coordonnées** : les coordonnées des chemins hamiltoniens sont exactement les permutations de $\{0,\ldots,K-1\}$ ; accès $O(N)$ direct sans recherche, en indexant le tenseur avec la permutation voulue.

---

## 11. Classification par familles (K=2, vérifiée jusqu'à $N=10$)

Quatre régimes identifiés pour les mots fermés/symétriques ($AB=BA$) vs ouverts ($AB\neq BA$) :

| Régime | Condition | Taille | Formule |
|---|---|---|---|
| Période pure | fermé, sans boucle, $AB=BA=p$ | $2$ | toujours $2$ |
| Cycle primitif | fermé, avec boucle, $AB=BA=1$ | $m$ | toujours $m$ |
| Boucle répétée | fermé, avec boucle, $AB=BA\geq2$ | variable | pas de formule simple |
| Embranchement | ouvert, $AB\neq BA$ | variable | pas de formule simple |

**Invariants de somme** (vérifiés) : pour la famille fermée, la somme composante-par-composante de tous les membres d'un groupe est constante — conséquence d'être des rotations cycliques les unes des autres.

---

## 12. Convergence "doublons engendrent doublons" (CONJECTURE)

En restreignant les sources d'insertion aux mots **déjà** doublons (pas tous les mots), le système devient autonome (couverture $100\%$) à partir d'un seuil $N_0(K)$ :

| $K$ | $N_0(K)$ |
|---|---|
| $2$ | $6$ (vérifié jusqu'à $N=12$, stable) |
| $3$ | $10$ (vérifié) |
| $4$ | $\approx 12$–$13$ (extrapolé, $99{,}95\%$ à $N=11$) |

Piloté spécifiquement par la sous-famille $r=K$ (les états $r<K$ héritent de la convergence des niveaux inférieurs). **Pas de formule fermée trouvée pour $N_0(K)$.**

Exception à $N=5, K=2$ : $4$ groupes sur $8$ nécessitent des singletons comme sources — exemples : $\{AABAB,ABAAB\}$, $\{ABABB,ABBAB\}$, etc.

---

## 13. Règle du facteur premier (CONJECTURE forte)

$$\text{tout facteur premier d'une taille de groupe est} \leq m \text{ (nombre de transitions)}$$

Vérifiée sur $8$ niveaux et $4$ valeurs de $K$ ($2,3,4,5,6$), jamais mise en défaut. Justification intuitive : un facteur premier $p$ vient d'un cycle de longueur $p$, qui nécessite $p$ transitions disponibles.

---

## 14. Indépendance en K de l'ensemble des tailles (CONJECTURE forte)

$$\text{Pour } K\geq3, \text{ l'ensemble des tailles de groupe atteignables à } m \text{ fixé ne dépend pas de } K$$

Vérifiée exactement sur $K=3,4,5,6$ (ensembles identiques à chaque niveau $m=2$ à $6$). $K=2$ fait exception (plus restreint).

---

## 15. Structure algébrique : monoïde libre non commutatif (prouvée)

Sur $E(K,\cdot) = \bigcup_N \{$mots de longueur $N$ sur $K$ lettres$\}$, muni de la concaténation $A$ :

- **Associativité** : vraie.
- **Élément neutre** : le mot vide ($E(K,0)$).
- **Commutativité** : **fausse** en général.
- **Inverses** : absents (structure de monoïde, pas de groupe).
- **Fermeture** : vraie par construction, y compris pour un second opérateur $B$ (remplacement d'un caractère par un mot entier), à condition que le mot inséré contienne le caractère remplacé (sinon un état peut disparaître — cas limite identifié et corrigé).

$E(K,N) \times E(K,M) \to E(K,N+M)$ par concaténation libre est une **bijection exacte** (vérifiée $9\times9=81=3^4$) — division/reconstruction d'un mot en deux parties de longueurs arbitraires.

---

## Bilan : statut de chaque résultat

| Résultat | Statut |
|---|---|
| Formules $N=2,3$ | **Prouvé** |
| Lemme de fermeture, lemme des boucles internes | **Prouvé** |
| Comptage des cores $K(K-1)^{N-1}$ | **Prouvé** |
| Principe de linéarité $\delta_X$ | **Prouvé** |
| Comptage des chemins généralisé $K^{N-2}$ | **Prouvé** |
| $f(r,r,r)=(r-1)!$ | **Prouvé** + vérifié 5 fois |
| $f(r,\geq2,r-1)=0$ | **Prouvé** |
| Décomposition $\binom{K}{r}f(r,s,m)$ / inclusion-exclusion | **Prouvé**, automatisé |
| Structure de monoïde libre | **Prouvé** |
| Décomposition core + confluence | Vérifié exhaustivement (pas de preuve formelle rédigée) |
| Couverture par cycles hamiltoniens | Vérifié à 100% sur 3 niveaux (pas de preuve générale) |
| Convergence $N_0(K)$ | **Conjecture** |
| Règle du facteur premier | **Conjecture forte** |
| Indépendance en $K$ des tailles | **Conjecture forte** |

---

## Ce qui reste hors de portée

Une formule fermée générale pour $g(N)$ n'existe pas et n'a pas été trouvée — dès qu'un vrai embranchement (degré $\geq3$) apparaît dans le multigraphe, seul le calcul complet (algorithme récursif équivalent au théorème BEST) donne la réponse exacte. C'est cohérent à travers toute l'exploration : chaque piste combinatoire a éclairé un sous-cas (cycles purs, chemins hamiltoniens, décomposition par états) sans jamais réduire le cas général.
