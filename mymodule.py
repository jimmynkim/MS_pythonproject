def my_add(a, b):
    return a+b

def my_sub(a, b):
    return a-b

# 지금 현재 모듈안에 무슨 값이 할당되어 있는지 확인
print(f'mymodule 안에서의 __name__: {__name__}')

# 이 모듈에서만 실행
if __name__ == "__main__":
    print(my_add(1, 2))
    print(my_sub(3, 4))