import threading

class SingletonPattern:
    
    _instance = None
    _lock = threading.Lock()
        
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(SingletonPattern, cls).__new__(cls, *args, **kwargs)
        return cls._instance