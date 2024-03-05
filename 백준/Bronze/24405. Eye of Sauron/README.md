# [Bronze II] Eye of Sauron - 24405 

[문제 링크](https://www.acmicpc.net/problem/24405) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현, 문자열

### 제출 일자

2024년 3월 5일 09:28:00

### 문제 설명

<p>Little Elrond is obsessed with the Lord of the Rings series. Between lectures he likes to doodle the central tower of the great fortress Baraddûr in the margins of his notebook. Afterward, he always double checks his drawings to ensure they are accurate: with the Eye of Sauron located in the very center of the tower. If any are incorrect, he makes sure to fix them.</p>

<p>You are to write a program that reads a representation of his tower, and ensures that the drawing is correct, with a properly centered eye.</p>

### 입력 

 <p>Input consists of a single string of length <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>, where <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4 ≤ n ≤ 100$</span></mjx-container>. Input strings will consist only of three types of characters: vertical bars, open parentheses, and closing parentheses. Input strings contain one or more vertical bars followed by a set of matching parentheses (the “eye”), followed by one or more vertical bars. For a drawing to be “correct”, the number of vertical bars on either side of the “eye” must match. Input will always contain a pair of correctly matched parentheses, with no characters between them. No other characters will appear in the string.</p>

### 출력 

 <p>On a single line print the word “correct” if the drawing is accurate or the word “fix” if there is an error that needs addressing.</p>

