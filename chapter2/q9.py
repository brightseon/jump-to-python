def dic():
    a = dict()
    a['name'] = 'python'
    a[('a',)] = 'python'
    # 리스트 자료형은 값이 변하기 때문에 key로 사용하기 적당하지 않다.
    # a[[1]] = 'python' error!
    a[250] = 'python'
    return

dic()