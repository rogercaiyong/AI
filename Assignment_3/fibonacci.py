def fibonacci(n):
    list = [1, 1]
    for i in range(n-2):
        list.append(list[i]+list[i+1])
    print(list)

fibonacci(20)
