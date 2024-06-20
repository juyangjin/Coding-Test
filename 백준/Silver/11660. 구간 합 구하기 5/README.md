# [Silver I] 구간 합 구하기 5 - 11660 

[문제 링크](https://www.acmicpc.net/problem/11660) 

### 성능 요약

메모리: 128084 KB, 시간: 1356 ms

### 분류

다이나믹 프로그래밍, 누적 합

### 제출 일자

2024년 6월 20일 12:17:09

### 문제 설명

<p>N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.</p>

<p>예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.</p>

<table class="table table-bordered" style="line-height:20.8px; width:158px">
	<tbody>
		<tr>
			<td style="text-align:center">1</td>
			<td style="text-align:center">2</td>
			<td style="text-align:center">3</td>
			<td style="text-align:center">4</td>
		</tr>
		<tr>
			<td style="text-align:center">2</td>
			<td style="text-align:center">3</td>
			<td style="text-align:center">4</td>
			<td style="text-align:center">5</td>
		</tr>
		<tr>
			<td style="text-align:center">3</td>
			<td style="text-align:center">4</td>
			<td style="text-align:center">5</td>
			<td style="text-align:center">6</td>
		</tr>
		<tr>
			<td style="text-align:center">4</td>
			<td style="text-align:center">5</td>
			<td style="text-align:center">6</td>
			<td style="text-align:center">7</td>
		</tr>
	</tbody>
</table>

<p>여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.</p>

<p>표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)</p>

### 출력 

 <p>총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.</p>

### 풀이설명 및 참고자료 

개인적으로는 어제 풀었던 예제보다 더 어려웠다. 어제랑 마찬가지로 구간 합 구하기를 해보았는데 일단 속도 개선을 위한 BufferedReader, StringTokenizer를 사용해야 했고, throws IOException로 예외 상황을 모두 없애버려야 에러없이 돌아가는 문제였다.

오늘 문제는 2차원 전체배열을 받아 A에 저장하고 D라는 새로운 배열을 선언하여 구간의 값을 합치는 작업을 먼저 진행했다.
<자리 예시>
```
1 2 3
4 5 6
7 8 9
```
5번 저장 시 2, 4, 5가 저장되고 6번 저장 시 3, 5, 6이 저장된다.
이처럼 ㄴ을 좌우반전한 모양으로 구간의 값이 저장되는데 저장할 때 저장되는 위치의 배열은 A에서 값을 가져오고 나머지 좌우의 부분은 D의 값을 그대로 사용하여 저장한다.
따라서 1번 값이 1, 2번 값이 3, 4번 값이 5 일 때 5번을 저장한다면 2,4번에 있는 값을 더하여 3+5가 되고, 저장되는 위치는 다른 배열이 있다 치고  5를 저장후 좌측 상단의 1을 빼면 총 12가 되어 1+2+4+5와 동일한 값을 가지게 된다. 

따라서 호출된 구간에 대한 배열은 D배열에 저장된 값에서 가로 새로에 저장된 값들을 빼고 마지막으로 중첩되게 뺐던 좌측 상단의 값을 더하는 것으로 구할 수 있게 된다. 
출처 DO it! 알고리즘 코딩테스트 자바 편(김종관 저) 전자책 50-51Page

오늘은 중첩 저장되는 부분에 대하여 이해할 때까지 생각보다 시간이 걸려서 반복문에 대한 공부가 부족하다는 것을 실감하였다.
