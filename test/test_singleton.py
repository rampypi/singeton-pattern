import unittest

from app.singleton import SingletonPattern


class TestSingletonClass(unittest.TestCase):
    
    
    def test_single_instance_of_sigleton_class(self):
        singleton_class = SingletonPattern()
        self.assertEqual(isinstance(singleton_class, SingletonPattern), True)
        

    def test_multiple_instance_of_sigleton_class(self):
        singleton_class = SingletonPattern()
        self.assertEqual(isinstance(singleton_class, SingletonPattern), True)
        singleton_class_second_instance = SingletonPattern()
        self.assertIs(singleton_class_second_instance, singleton_class, "They are not same")
        
    def test_multiple_instance_of_sigleton_class_tread_safe(self):
        import threading
        def create_instance():
            SingletonPattern()
            
        threads = [threading.Thread(target=create_instance) for _ in range(100)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
            
        instance = SingletonPattern()
        self.assertTrue(all(SingletonPattern() is instance for _ in range(100)), "Singleton is not thread safe")