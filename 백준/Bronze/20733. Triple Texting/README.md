# [Bronze II] Triple Texting - 20733 

[문제 링크](https://www.acmicpc.net/problem/20733) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

문자열

### 제출 일자

2024년 5월 22일 08:33:41

### 문제 설명

<p>Julia enjoys talking to her grandma, playing with legos, and inventing two-player card games where she has a winning strategy. Recently however, she has not been able to talk to her grandma in person because of some kind of "pandemonium". Instead, they have resorted to texting, which is a very slow process since grandma types very slowly and often mistypes letters. To make matters worse, grandma has started to write every word three times so that Julia can correct her mistypes. For example, if grandma wants to write the word "hello", she will instead write "hellohellohello". If she mistypes one of those letters, it might instead be sent as "hellohrllohello'.'</p>

<p>Your task is to write a program that given a message sent by grandma, where possibly one letter has been changed to some other letter, finds the original word.</p>

### 입력 

 <p>The input consists of one string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> containing lower case English letters (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>s</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><mn>99</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3 \leq |s| \leq 99$</span></mjx-container>). This is the message sent by grandma. It is guaranteed that this string is the result of a word being written three times, where possibly one letter was changed to some other letter.</p>

### 출력 

 <p>Output one string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$t$</span></mjx-container>, the original word.</p>

