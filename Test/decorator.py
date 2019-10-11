def logger(func):
    def wrapper():
        print('Logging Started')
        func()
        print('Logging completed')
    return wrapper

@logger
def test_logging():
    print('Function execution')

test_logging()