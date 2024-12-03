def fibonacci(n):
    try:
        if n < 0:
            raise ValueError('n nie moze byc ujemne')
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    except ValueError as e:
        print(e)
    except Exception:
        print("nieznany blad")


print(fibonacci(10))
