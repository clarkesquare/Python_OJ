# [Silver V] Judging Troubles - 10527 

[문제 링크](https://www.acmicpc.net/problem/10527) 

### 성능 요약

메모리: 130896 KB, 시간: 240 ms

### 분류

구현, 자료 구조, 정렬, 집합과 맵, 해시를 사용한 집합과 맵

### 제출 일자

2025년 11월 6일 10:45:12

### 문제 설명

<p>The NWERC organisers have decided that they want to improve the automatic grading of the submissions for the contest, so they now use two systems: DOMjudge and Kattis. Each submission is judged by both systems and the grading results are compared to make sure that the systems agree. However, something went wrong in setting up the connection between the systems, and now the jury only knows all results of both systems, but not which result belongs to which submission! You are therefore asked to help them figure out how many results could have been consistent.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with one integer n (1 ≤ n ≤ 10<sup>5</sup>), the number of submissions;</li>
	<li>n lines, each with a result of the judging by DOMjudge, in arbitrary order;</li>
	<li>n lines, each with a result of the judging by Kattis, in arbitrary order.</li>
</ul>

<p>Each result is a string of length between 5 and 15 characters (inclusive) consisting of lowercase letters.</p>

### 출력 

 <p>Output one line with the maximum number of judging results that could have been the same for both systems.</p>

