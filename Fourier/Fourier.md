$$
\begin{align}
cos(a + b) &= \mathfrak{Re}(e^{ia+b}) \\
&= \mathfrak{Re}(e^{ia} \ e^{ib}) \\
&= \mathfrak{Re}((cos(a) + i\sin(a))(cos(b) + i\sin(b))) \\
&= \cos(a)\cos(b)-\sin(a)\sin(b)\\
sin(a + b) &= \mathfrak{Im}(e^{ia+b}) \\
&= \mathfrak{Im}(e^{ia} \ e^{ib}) \\
&= \mathfrak{Im}((cos(a) + i\sin(a))(cos(b) + i\sin(b))) \\
&= \sin(a)\cos(b)+\cos(a)\sin(b) 
\end{align} \\
$$

$$
\begin{align}
&\text{d'ou : } \\
\mathcal{F(f)} &= \max_{\phi}\bigg(\int f(x)\sin(wx + \phi)\bigg) \\
\mathcal{F(f)}&=\max_{\phi}\bigg(\int f(x)\Big(sin(wx)cos(\phi) + cos(wx)sin(\phi) \Big)dx \bigg) \\
&= \max_{\phi}\bigg(cos(\phi)\int f(x)sin(wx)\ dx + sin(\phi) \int f(x)cos(wx)\ dx \bigg) \\
\\
&\text{on utilise l'identité} \quad A\cos(\theta) + B\sin(\theta) = \sqrt{A^2 + B^2} \ \sin(\theta + \alpha) \\
&\max_{\theta}\big(\sin(\theta + \alpha)\big) = 1 \\
&\max_{\theta}\big(\sqrt{A^2 + B^2} \ \sin(\theta + \alpha)\big) = \sqrt{A^2 + B^2} \\
&\text{d'ou : } \\
\mathcal{F(f)} &= \sqrt{\bigg(\int f(x) \sin(wx)\bigg)^2 + \bigg(\int f(x) \cos(wx)\bigg)^2}
\end{align}
$$
