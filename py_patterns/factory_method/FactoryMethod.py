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
    
    def some_operation(self) -> str:
        """
        Creators Primary responsiblity isn't creating products. Usually, contains some core business logic
        that relieas on product objects, returned by the factory method.
        Subclasses can indrectly change that buisness loggic by overrideing the factory method
        and returning a different type of product from it.
        """

        # Call the factory to create a product object.
        product = self.factory_method()
        # Now use the product
        result = f"creator: the same code has just done {product}"
        return result
    

    





def main():
    pass


if __name__ == "__main__":
    print("running Main")
    main()
