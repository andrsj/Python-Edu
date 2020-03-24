from typing import List, Optional, Tuple, overload, final


# Tuple -> Tuple[str, str], ...
# List -> List[Any], List[int], ...
# Any
# Callable
# Dict -> Dict[Any, int], ...
# Union -> Union[int, float], ... # using and int, and float
# Optional -> like Union[str, None] but Optional[str]

value: int = 10

def func(a: int = 10, b:str = 'Sample') -> str:
    return b * a

class User:
    def __init__(self, first: str = 'Andrew', last: str = 'Derkach'):
        self.first = first
        self.last = last

user: User = User()

def function(a: List[str] = []) -> None:
    for i in a:
        print(i)

def foo(arg: Optional[int] = None) -> None:
    pass



@overload
def process(response: None) -> None:
    pass

@overload
def process(response: int) -> Tuple[int, str]:
    pass

@overload
def process(response: bytes) -> str:
    pass

def process(response):
    pass # <actual implementation>




class Base:
    @final
    def done(self) -> None:
        pass

class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        pass

@final
class Leaf:
    pass

class Other(Leaf):  # Error reported by type checker
    pass