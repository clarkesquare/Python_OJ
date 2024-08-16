# [Silver V] Recount - 24776 

[문제 링크](https://www.acmicpc.net/problem/24776) 

### 성능 요약

메모리: 49988 KB, 시간: 104 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 문자열

### 제출 일자

2024년 8월 16일 09:58:58

### 문제 설명

<p><img alt="" src="" style="width: 150px; height: 135px; float: right;">The recent schoolboard elections were hotly contested: a proposal to swap school start times for elementary and high school students, a controversial new dress code proposal that bans athletic clothes in school, and a proposal to raise real-estate taxes to pay for a new football practice facility, and the list goes on and on. It is now hours after the polls have closed and a winner has yet to emerge! </p>

<p>In their desperation, the election officials turn to you and ask you to write a program to count the vote!</p>

### 입력 

 <p>The input consists of a single test case, which is a list of votes cast. Each line in the input contains the name of a candidate for whom a vote was cast.  A name may consist of multiple words, separated by spaces. Words contain letters or hyphens, but no other punctuation characters.  There will be at least 2 votes on the list. The list of votes ends with a single line containing the characters <code>***</code>. This line should not be counted.  There can be up to <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>,</mo><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100,000$</span></mjx-container> valid votes.</p>

### 출력 

 <p>If a candidate obtained a simple or absolute majority of all votes cast (that is, more than any other candidate), output the name of this candidate! If no candidate obtained a simple majority, output: "<code>Runoff!</code>" (don't forget to include the exclamation mark!)</p>

