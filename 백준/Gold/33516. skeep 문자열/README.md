# [Gold III] skeep 문자열 - 33516 

[문제 링크](https://www.acmicpc.net/problem/33516) 

### 성능 요약

메모리: 193688 KB, 시간: 312 ms

### 분류

자료 구조, 스택, 문자열

### 제출 일자

2025년 7월 7일 22:55:33

### 문제 설명

<p><code>skeep</code>은 자신의 오프라인 팬클럽을 운영 중이다. 어느덧 인기스타가 된 <code>skeep</code>의 팬클럽에는 사람들이 몰려 공간이 부족해졌다.</p>

<p>이에 <code>skeep</code>은 자신의 진정한 팬만 팬클럽에 입장시키기로 결심했다.</p>

<p><code>skeep</code>의 진정한 팬이라면 <span style="color:#e74c3c;"><code>skeep</code></span>이라는 문자열을 좋아할 것이라 믿으며, 이를 판별하기 위해 다음과 같은 문제를 준비했다.</p>

<p>길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 알파벳 소문자로 구성된 문자열이 주어진다. 이 문자열에서 다음 작업을 원하는 만큼 수행할 수 있다.</p>

<ul>
	<li>문자열에서 <span style="color:#e74c3c;"><code>skeep</code></span>이라는 연속한 부분 문자열을 찾아 <span style="color:#e74c3c;"><code>s</code></span>를 제외한 소문자 알파벳 하나로 바꾼다.</li>
</ul>

<p>이때, 수행할 수 있는 작업의 최대 횟수를 구해야 한다.</p>

<p><code>skeep</code>의 팬인 당신은 팬클럽에 들어가기 위해 이 문제를 해결해야 한다. 문자열의 길이와 문자열이 주어질 때 정답을 출력하시오.</p>

### 입력 

 <p>첫 번째 줄에 문자열의 길이에 해당하는 정수<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le N \le 1\,000\,000)$</span> </mjx-container></p>

<p>두 번째 줄에 알파벳 소문자로 구성된 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 문자열이 주어진다.</p>

### 출력 

 <p>위 작업의 최대 횟수를 출력하시오.</p>

