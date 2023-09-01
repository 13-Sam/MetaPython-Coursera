def d():
    
    animal = "elephant"
    def e():
        # nonlocal animal
        animal = "girafee"
        print("inside from nested function: "+animal)
    
    print("This is before calling function: "+animal)
    e()
    print("After nested funcion: "+animal)
    
animal = "camel"
d()
print("Global Animal: "+animal)