###Fill in the body of the methods of the Fraction class below.
###Some of them are filled in already for you so you don't have to do it.
###
###Name:
###Date:

class Fraction(object):
    def __init__(self, str_fraction):
        '''
        Initializes a Fraction object
                
        Parameter:
        str_fraction is a string in the format of "num/denom". Assume it is properly formatted.
        for example, if the string "-3/12" it will split the string by the slash, and then the
        num(erator) is "-3" and the denom(inator) will be "12".
        
        a Fraction object has two attributes:
            self.num (integer, the "top part" of the string)
            self.denom (integer, the "bottom part" of the string)
            Assume the numerator and denominators are properly formatted and the denominator is not zero.
        '''        
        pass 
    
    def __str__(self):
        '''
        Returns a string format of the Fraction object in the form of "num/denom".
        Does not reduce it - simply returns astring with its current num and denom values.
        '''
        return str(self.get_num()) + "/" + str(self.get_denom())
    
    def __float__(self):
        '''
        Returns the floating point decimal equivalent of the fraction object.
        For example:
        my_frac = Fraction(1/4)
        float(my_frac) will return 0.25
        '''
        ###The pass statement below causes the program to crash.
        ###You need to return a floating point value.
        pass
        

    def get_num(self):
        '''
        Returns the numerator of the fraction object.
        '''
        pass
        
    def get_denom(self):
        '''
        Returns the denominator of the fraction object.
        '''
        pass
    
    def set_num(self, num):
        '''
        Sets self.num to num. Assume that num being passed in is an integer.
        Returns nothing. Method finished for you already.
        '''
        self.num = num
        
    def set_denom(self, denom):
        '''
        Sets self.denom to denom. Assume that num being passed in is an integer.
        Returns nothing. Method finished for you already.
        '''
        self.denom = denom

    def reduce(self):
        '''
        Reduces the attributes of the fraction to lowest terms, using the helper function find_gcf(a, b).
        Returns a new fraction that is in reduced form.
        '''
        pass

    
    def find_gcf(self, a, b):
        '''
        Finds the greatest common factor between integers a and b. 

        Parameters:
        a,b - are both integers.

        Returns:
        The integer GCF of a and b.
        '''
        pass


    def get_reciprocal(self):
        '''
        Returns the reciprocal of the fraction as a new fraction object.
        '''
        pass
    
    #### Arithmetic operators ####
    def __add__(self, f2):
        '''
        The implementation of adding two fractions together - "self + f2"
        Parameters:
        f2 - the other fraction you wish to add to "self".

        Returns:
        A new fraction where "self" and "f2" have been added together properly.
        The result is in lowest terms.
        '''

        ###REMEMBER! To add fractions DO NOT add the numerators and denominators together.
        ###To add or subtract fractions, they must have a common denominator.
        ###HINT! You don't need to find the lowest common denominator.
        ###Use any appropriate common denominator to do the calculation, then reduce it before returning it.

        #todo:implement the actual addition of the Fraction data and return
        #a new Fraction where we've added self and f2 together.
        pass

    def __sub__(self, f2):
       '''
       The implementation of subtracting two fractions together - "self - f2"
       Parameters:
       f2 - the other fraction you wish to subtract from "self".
       Returns:
       A new fraction where "self" and "f2" have been subtracted together properly.
       The result is in lowest terms.
       '''

       ###REMEMBER! To subtract fractions DO NOT subtract the numerators and denominators.
       ###To add or subtract fractions, they must have a common denominator.
       ###HINT! You don't need to find the lowest common denominator.
       ###Use any appropriate common denominator to do the calculation, then reduce it before returning it.

       #todo: do the subtraction!!!

       pass
    
    def __mul__(self, f2):
        '''
        The implementation of multiplying two fractions together - "self * f2"
        Parameters:
        f2 - the other fraction you wish to multiply by "self".

        Returns:
        A new fraction where "self" and "f2" have been multiplied together properly.
        The result is in lowest terms.
        '''

        ###REMEMBER! To multiply fractions together you multiply the numerators and the denominators.
        ###Make sure your resulting fraction is in lowest terms before returning it.
        pass
    
    def __truediv__(self, f2):
        '''
        The implementation of multiplying two fractions together - "self / f2"
        Parameters:
        f2 - the other fraction you wish to divide by.

        Returns:
        A new fraction where "self" and "f2" have been divided together properly.
        The result is in lowest terms.
        '''

        ###REMEMBER! To divide fractions together you multiply by the reciprocal!
        ###Make sure your resulting fraction is in lowest terms before returning it.

        pass
    
    #### Make all of the other comparison operators:
    #### ==, >, <, >=, <= 

###DO NOT CHANGE ANYTHING BELOW HERE###    
if __name__ == '__main__':
    frac1 = Fraction("50/100")
    frac2 = Fraction("2/16")

    print("Printing frac1. Expected output should be\n50/100")
    print("Actual Result:")
    print(frac1)

    print("Printing call to float(frac2). Expected output should be\n0.125")
    print('Actual Result:')
    print(float(frac2))

    print("Printing call to frac1.get_num(). Expected output should be\n50")
    print("Actual Result:")
    print(frac1.get_num())

    print("Printing call to frac2.get_denom(). Expected output should be\n16")
    print("Actual Result:")
    print(frac2.get_denom())

    print("Testing call to frac1.reduce(). Expected output should be:\n1/2")

    r = frac1.reduce()
    print("Actual Result:")
    print(r)

    print("Testing frac1 + frac2. Expected output should be:\n5/8")
    fsum = frac1 + frac2
    print("Actual Result:")
    print(fsum)

    print("Testing frac2 - frac1. Expected output should be:\n-3/8")
    fsub = frac2 - frac1
    print("actual Result:")
    print(fsub)

    print("New Fractions - fracA is -14/-27 and fracB is 3/7")
    (fracA, fracB) = (Fraction("-14/-27"), Fraction("3/7"))
    print("Testing fracA * fracB. Expected output should be:\n2/9")
    mult = fracA * fracB
    print("Actual Result:")
    print(mult)

    print("Testing (-3/7)/(3/-4). Expected output should be:\n4/7")
    div = Fraction("-3/7") / Fraction("3/-4")
    print("Actual Result:")
    print(div)
    print("######\nCheck the results, fix where necessary\n#####")
    
    #### Create test cases for the comparison operators.