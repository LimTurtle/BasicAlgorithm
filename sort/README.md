# Python 정렬 방식
- 기본적으로 ```list.sort()``` 또는 ```sorted(list)``` 를 사용할 수 있으며, sort() 는 list에서만 사용 가능하다는 점을 주의
- 위 정렬 함수들은 Timsort 를 사용한 것으로, 평균 $O(nlogn)$ 의 시간 복잡도를 가짐

# Bubble Sort

![Bubble Sort](https://gmlwjd9405.github.io/images/algorithm-bubble-sort/bubble-sort.png)

- 출처 : https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html
- 인접한 두 원소를 비교

# Selection Sort

![Selection Sort](https://gmlwjd9405.github.io/images/algorithm-selection-sort/selection-sort.png)

- 출처 : https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html
- 최솟값을 계속해서 앞으로 가져오기

# Insertion Sort

![Insertion Sort](https://gmlwjd9405.github.io/images/algorithm-insertion-sort/insertion-sort.png)

- 출처 : https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html
- Selection 과 비슷하게 한 번의 루프마다 리스트의 앞부분이 정렬되지만, 최솟값을 찾는게 아닌 배열의 다음 원소를 계속해서 정렬해나감

