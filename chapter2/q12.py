def same_ref():
    a = b = [1, 2, 3]
    a[1] = 4
    # a와 b는 같은 주소를 바라보고 있기 때문에
    # a의 값이 변경되면 영향을 받는다.
    print(b)

same_ref()