from __future__ import annotations
from abc import ABC, abstractmethod 


class Creator(ABC):
    """
    Creator Class declares the factory method that is supposed to return an object
    of the product class. Creator's subclasses provide the implementation of of this
    method
    """

    @abstractmethod
    def factory_method(self):
        """
        Creator may provide some default
        """
        raise NotImplementedError(f"This method is not implemented{factory_method.__name__}")




def main():
    pass


if __name__ == "__main__":
    print("running Main")
    main()
