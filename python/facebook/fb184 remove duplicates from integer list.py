
def n_largest(dic,n):
    print("dict",sorted(dic.items(), key=lambda x: -x[1])     )
    print("dict",sorted(dic.items(), key=lambda x: -x[1])[-3]     )
    print("dict",sorted(dic.keys()     )  )
    print("dict",sorted(dic.keys() , reverse=True  )  )
dic = {'cow':20 , 'squirrel':3 , 'ant':1 , 'dog':7 , 'cat':6 }
n = 3
n_largest (dic,n)