# Psuedo code for abstract factory

define factory interface

class IFactory:
    
    create_product_a implements IProductA:
        pass

    create_product_b implements IProductB:
        pass

Note: this is only an interface for the factories.

Class ConcreteFactory1 implement IFactory:
    
    create_product_a implements IProductA:
        return Concrete_Product_a1()

    create_product_b implements IProductB:
        return Concrete_Product_b1()
   
Class ConcreteFactory2 implement IFactory:
    
    create_product_a implements IProductA:
        return Concrete_Product_a2()

    create_product_b implements IProductB:
        return Concrete_Product_b2()
 

Note: the 2 classes implement Ifactory

