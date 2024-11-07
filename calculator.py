class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b > 0:
            for i in range(b):
                result = self.add(result, a)
            return result
        else:
            for i in range(a):
                result = self.add(result, b)
            return result
    

        

    def divide(self, a, b):
        result = 0
        c = False
        if b == 0:
            return "undefined"
        
        if a < 0 or b < 0:
            c = True
            a = abs(a)
            b = abs(b)

        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        if c ==  True:
            result = -result
        return result
            
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, -3))
    print("Example: division: ", calc.divide(10,10))
    print("Example: modulo: ", calc.modulo(10, 3))