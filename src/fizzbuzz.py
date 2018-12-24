def fizzbuzz(n):
    array = []
    for m in range(0, n):
        if m%15 == 0:
            array.append("fizzbuzz")
        elif m%3 == 0:
            array.append("fizz")
        elif m%5 == 0:
            array.append("buzz")
        else:
            array.append(m)
    return array
