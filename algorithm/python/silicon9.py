# 정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.
# 예제)
# Input: [0, 5, 0, 3, -1]
# Output: [5, 3, -1, 0, 0]

# Input: [3, 0, 3]
# Output: [3, 3, 0]

def moveAllZerosToEnd(array):
    cursor = 0

    for i in range(len(array)):
        if(array[i] != 0):
            array[cursor] = array[i]
            array[i] = 0
            cursor += 1

    return array

print(moveAllZerosToEnd([0, 5, 0, 3, -1]))
