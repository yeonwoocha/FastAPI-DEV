'''
def find_squared_largest(arr):
    largest = arr[0]
    print("largest : ", largest)
    for i in arr:
        # 제일큰수 [0]으로 잡았을때, 다음에 들어오는 수가 largest보다 크면 실행
        if i > largest:
            print("before i: ", i, "largest: ", largest)
            largest = i
            print("after i: ", i, "largest: ", largest)
    return largest**2

array = [10, 5, 8, 20, 3, 9, 6, 32, 26]
largest_squared_number = find_squared_largest(array)
print(f"The largest squared number in the list is {largest_squared_number}")
'''

'''
class MyIterator():
    def __init__(self, data):
        self.data = data
        self.position = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    for item in i:
        print(item)
'''
        
'''
def is_prime(n):
    if n<2:
        return False 
    for i in range(2,n):  #time complexity is O(n)
        if n%i==0:
            return False
    return True   #if one is True then no need to check for the other so terminates the loop
n=int(input('enter a number:'))
if is_prime(n):
    print(f'given number {n} is prime')
else:
    print(f'given number {n} is not prime')
'''

def simple_generator(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# 제너레이터 객체 생성
gen = simple_generator(5)

# 제너레이터의 값 순회
for value in gen:
    print(value)




