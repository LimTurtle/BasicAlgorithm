# BasicAlgorithm

# Python Class 주의점

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

- 위 처럼 ```__init__``` 을 생성자처럼 사용 가능하고 클래스 멤버 변수를 이곳에서 초기화
- 재귀 함수 사용 시 return 에 값을 명시해서 최신화 해주어야 함 (Search -> BST 참조)
