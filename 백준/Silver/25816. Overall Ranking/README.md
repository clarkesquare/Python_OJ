# [Silver III] Overall Ranking - 25816 

[문제 링크](https://www.acmicpc.net/problem/25816) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 정렬

### 제출 일자

2024년 8월 21일 01:11:27

### 문제 설명

<p>The Regional Competitions of ICPC (International Collegiate Programming Contest) allow universities to enter more than one team in the contest. The scoresheet for the contest will list the ranking for each team. For example, if UCF has three teams, GT two teams, and Auburn four teams, the final team ranking may look like:</p>

<ol>
	<li>Auburn</li>
	<li>GT</li>
	<li>UCF</li>
	<li>UCF</li>
	<li>UCF</li>
	<li>Auburn</li>
	<li>Auburn</li>
	<li>GT</li>
	<li>Auburn</li>
</ol>

<p>The regional contest does not show the “overall performance” of each university which is the average of the team rankings for the university. For the above scoresheet, Auburn has the overall performance of “(1 + 6 + 7 + 9) / 4 = 5.75”; UCF has the overall performance of “(3 + 4 + 5) / 3 = 4.0”; and GT has the overall performance of “(2 + 8) / 2 = 5.0”. So, the overall ranking of the universities will be:</p>

<ol>
	<li>UCF</li>
	<li>GT</li>
	<li>Auburn</li>
</ol>

<p>Note that lower average indicates better performance, hence higher university ranking.</p>

<p>Assume that the universities will not have the same overall performance, i.e., no need for tiebreaker.</p>

<p>Given the scoresheet for a contest with each university having one or more teams, find the university ranking based on the overall performances.</p>

### 입력 

 <p>The first input line contains an integer, n (2 ≤ n ≤ 100), indicating the number of teams in the regional contest. The teams are listed on the following n input lines, one per line, in the order of team ranking at the regional. Each team name will be 1 to 20 letters (uppercase and/or lowercase). Assume there will be at least two universities in the input.</p>

### 출력 

 <p>Print the universities, one per line, in the order of overall performance.</p>

