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
    
    def another_operation(self) -> None:

        print("Another method")
    

    
# Concreate creators override the factory method inorder to change thre resulting product

class ConcreteCreator1(Creator):
    """
    The signiature of the method still uses the abstract product type,
    even though the concrete product is acutally returned from the method. THis 
    way the creator can stay independent of concreate product classes.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The p0roduct interface declares the operations that all concreate products must implement
    """

    def operation(self) -> str:
        raise NotImplementedError(f"This method is not implemented{operation.__name__}")


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, through its vase interface
    As long as the client keeps working with the creator via the base interface, you can pass
    it any creator's subclass.

    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")
    print("\n")
    creator.another_operation()

def main():
    print("App: Launched with the ConcreteCreator1.")
    t = client_code(ConcreteCreator1())
    print("\n")
    print("App: Launched with the ConcreteCreator2.")
    a = client_code(ConcreteCreator2())
    


if __name__ == "__main__":
    print("running Main")
    main()
