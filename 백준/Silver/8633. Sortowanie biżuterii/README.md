# [Silver V] Sortowanie biżuterii - 8633 

[문제 링크](https://www.acmicpc.net/problem/8633) 

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

정렬, 문자열

### 제출 일자

2024년 7월 6일 22:39:56

### 문제 설명

<p>Małgosia odziedziczyła po wujku kolekcję drogocennej biżuterii. Zastała w skarbcu artystyczny nieład i postanowiła go uporządkować. Wskład biżuterii wchodzą kolie składające się z cennych i rzadkich kamieni szlachetnych. Żadne dwa z nich nie są jednakowe. Pomóż Małgosi uporządkować drogocenny zbiór.</p>

<p>Opracuj program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia opisy biżuterii,</li>
	<li>uporządkuje je według rosnącej długości, a te, które są równej długości uporządkuje leksykograficznie,</li>
	<li>posortowane łańcuchy wypisze na standardowe wyjście.</li>
</ul>

<p>Łańcuchy o równej długości powinny być uporządkowane leksykograficznie-spośród dwóch różnych łańcuchów równej długości mniejszy jest ten, który ma mniejszy znak na pierwszej różniącej się pozycji.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się liczba łańcuchów do analizy <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>≤</mo><mn>150</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \le 150$</span></mjx-container>), a w kolejnych <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> wierszach znajdują się opisy poszczególnych elementów biżuterii. Opis każdego z nich składa się z niepustego łańcucha małych liter alfabetu łacińskiego ('a'..'z') odpowiadających użytym kamieniom, o długości nie przekraczającej <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$200$</span></mjx-container> znaków.</p>

### 출력 

 <p>W kolejnych wierszach wypisz kolejno uporządkowane rosnąco łańcuchy, po jednym w każdym wierszu.</p>

