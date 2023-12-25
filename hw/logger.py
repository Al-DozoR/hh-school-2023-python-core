import time


def Logger(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            attr = getattr(self.wrapped, name)
            if callable(attr):
                return self.decorator(attr)
            return attr

        def decorator(self, func):
            def wrapped_func(*args, **kwargs):
                start_time = time.time()
                print(f"Выполнение метода {func.__name__} началось в {time.strftime('%H:%M:%S')}.")
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                print(
                    f"Метод {func.__name__} завершен в {time.strftime('%H:%M:%S')}. Заняло {execution_time:.6f} секунд.\n")
                return result

            return wrapped_func

    return Wrapper
