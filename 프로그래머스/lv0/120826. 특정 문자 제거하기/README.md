# [level 0] 특정 문자 제거하기 - 120826 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120826) 

### 성능 요약

메모리: 77.2 MB, 시간: 0.06 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>문자열 <code>my_string</code>과 문자 <code>letter</code>이 매개변수로 주어집니다. <code>my_string</code>에서 <code>letter</code>를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>letter</code>은 길이가 1인 영문자입니다.</li>
<li><code>my_string</code>과 <code>letter</code>은 알파벳 대소문자로 이루어져 있습니다.</li>
<li>대문자와 소문자를 구분합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>letter</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"abcdef"</td>
<td>"f"</td>
<td>"abcde"</td>
</tr>
<tr>
<td>"BCBdbe"</td>
<td>"B"</td>
<td>"Cdbe"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"abcdef" 에서 "f"를 제거한 "abcde"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"BCBdbe" 에서 "B"를 모두 제거한 "Cdbe"를 return합니다.</li>
</ul>

#### 타인이 푼 조금 더 완벽한 코드
```
class Solution {
    public String solution(String my_string, String letter) {
        String answer = ""; //answer값 초기화

        answer = my_string.replace(letter, ""); //letter값을 ""로 바꾼 후 answer에 저장

        return answer; //결과값 출력
    }
}
```


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
