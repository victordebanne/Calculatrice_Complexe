$$
\begin{align}
&\text{soit une chaîne de Markov} \ M \ \text{de taille} \ N \ \text{sur un alphabet} \ A\text{.} \\
\\
&\text{notons} \ \sigma \ \text{une séquence de}\ n \ \text{observations} \ 
\left\{ x_1, x_2, \dots, x_n  \right\} \\
\
&\text{la probabilité d'un evenement} \ x_n \ \text{ dans une séquence} \ \sigma \ \text{est donnée par la table de Markov}\\
&P(x_n|x_{n-1})\\
&\text{d'ou la probabilité d'une séquence}\ x_{n - k} \ \text{à} \ x_n = \\
&P(x_{n - k}|x_{n- k - 1}) \times P(x_{n - k + 1}|x_{n- k}) \times \cdots P(x_n|x_{n-1}) \\
=&\prod_{i=n-k}^{n}P(x_i|x_{i-1})\\
&\text{la probabilité d'obtenir une séquence} \ \sigma \ \text{est donc :}\\
P(\sigma) &= \pi_M(x_1)\prod_{i=2}^{n}P(x_i|x_{i-1}) \quad \text{avec} \ \pi_M(x) \ \text{la mesure stationnaire de l'évènement} \ x\\
&\text{ou : } \\
P(\sigma) &= \prod_{i=2}^{n}P(x_i|x_{i-1}) \quad \text{si chaque évenement} \ x \ \text{est equiprobable au début de la séquence.}\\
\\
&\text{on en déduit alors} \ \mathcal{L}(M;\sigma) \ \text{ la vraissemblance de la séquence} \ \sigma \ \text{sur la chaîne} \ M\text{.}\\ 
\mathcal{L}(M;\sigma) &= \prod_{i=2}^{n}P(x_i|x_{i-1}, M) \\ \\
&\text{ma proposition d'interpolation entre chaînes de Markov repose sur des transitions}\\
&\text{basées sur des séquences pivot entre deux chaînes proches.}\\ \\
&\text{soient} \ M_1 \ \text{et} \ M_2 \ \text{deux chaînes de même taille, sur le même alphabet.} \\
&M_1 \ \text{produit des séquences de taille} \ n \\ \\
&\text{soit une séquence} \ k \ \text{produite par} \ M_1\ : \sigma_{k, M1}\\
&\text{si} \quad \mathcal{L}(M_2;\sigma_{k,M_1})>\mathcal{L}(M_1;\sigma_{k,M_1}) \\
&\text{alors} \quad \sigma_{k, M_1} \ \text{est une séquence pivot produite par} \ M_1 \ \text{mais plus plus vraissemblablement produite par} \ M_2
\end{align}
$$
