# Listed error types in Python

class BaseError(Exception):
    """Base error class for all errors"""
    def __init__(self, message, errno=None, winerror=None,strerror=None,filename=None,filename2=None ):
        self.message = message
        self.errno = errno
        self.winerror = winerror
        self.strerror = strerror
        self.filename = filename
        self.filename2 = filename2

class DivisionError(BaseError):
    pass
class AssertionError(BaseError):
    pass
class AttributeError(BaseError):
    pass
class EOFError(BaseError):
    pass
class FloatingPointError(BaseError):
    pass
class GeneratorExit(BaseError):
    pass
class ImportError(BaseError):
    pass
class ModuleNotFoundError(BaseError):
    pass
class IndexError(BaseError):
    pass
class KeyError(BaseError):
    pass
class KeyboardInterrupt(BaseError):
    pass
class MemoryError(BaseError):
    pass
class NameError(BaseError):
    pass
class NotImplementedError(BaseError):
    pass
class OSError(BaseError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
