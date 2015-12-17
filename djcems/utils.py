

def rest_anonymous():
    def decorator(func):
        func.authentication_classes = ()
        func.permission_classes = ()
        return func
    return decorator
