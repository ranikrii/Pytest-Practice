def add(a,b):
    return a + b

def divide(a, b):
    if b == 0 :
        raise ValueError("can't divide by zero")
    return a/b
#def test_get_weather():
    #assert get_weather(21) == "hot"