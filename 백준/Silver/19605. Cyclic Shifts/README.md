# [Silver IV] Cyclic Shifts - 19605 

[문제 링크](https://www.acmicpc.net/problem/19605) 

### 성능 요약

메모리: 31380 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘, 문자열

### 제출 일자

2024년 9월 24일 13:10:14

### 문제 설명

<p>Thuc likes finding cyclic shifts of strings. A <em>cyclic shift</em> of a string is obtained by moving characters from the beginning of the string to the end of the string. We also consider a string to be a cyclic shift of itself. For example, the cyclic shifts of <code>ABCDE</code> are:</p>

<p style="text-align: center;"><code>ABCDE</code>, <code>BCDEA</code>, <code>CDEAB</code>, <code>DEABC</code>, and <code>EABCD</code>.</p>

<p>Given some text, T, and a string, S, determine if T contains a cyclic shift of S.</p>

### 입력 

 <p>The input will consist of exactly two lines containing only uppercase letters. The first line will be the text T, and the second line will be the string S. Each line will contain at most 1000 characters.</p>

### 출력 

 <p>Output <code>yes</code> if the text, T, contains a cyclic shift of the string, S. Otherwise, output <code>no</code>.</p>

