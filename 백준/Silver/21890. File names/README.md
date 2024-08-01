# [Silver V] File names - 21890 

[문제 링크](https://www.acmicpc.net/problem/21890) 

### 성능 요약

메모리: 31120 KB, 시간: 48 ms

### 분류

많은 조건 분기, 구현, 문자열

### 제출 일자

2024년 8월 1일 14:37:27

### 문제 설명

<p>Petya and Vasya love to develop their own operating systems, so Petya uses PetOS operating system on his computer, and Vasya uses VasOS on his computer.</p>

<p>One day Petya wanted to send Vasya some files from his computer, but it turned out that it was not so easy to do. The problem is that in PetOS the name of file can be any string consisting of Latin letters and dots, with length in range from 1 to 20, and VasOS only supports the names of the form <code><filename>.<extension></code>, where <code><filename></code> and <code><extension></code> are non-empty strings of Latin letters, with the length of <code><filename></code> not greater than 8, and the length of <code><extension></code> not greater than 3.</p>

<p>Help Petya to calculate how many files from his list can be transferred to Vasya without changing their name.</p>

### 입력 

 <p>The first line contains the number <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>, the number of files Petya wants to transfer (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 100$</span></mjx-container>). The following <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines contain file names. All names have a length of 1 to 20 characters and contain only lowercase Latin letters and dots.</p>

### 출력 

 <p>Output the number of files that Petya can transfer to Vasya without renaming.</p>

