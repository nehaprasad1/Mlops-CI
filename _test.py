import pytest


#fn to check square
def square(n) : 
    return n ** 2
#fn to check cube
def cube(n):
    return n**3
#fn to check fifth power"
def fifth_pow(n):
    return n**5

#testing the square function
def test_sq():
    assert square(2)==4, "Test Failed : square of 2 should be 4"
    assert square(4)==16, "Test Failed : square of 4 should be 16"
    
def test_cb():
    assert cube(1) == 1 , "Test failed: cube of 1 should be 1"
    assert cube(2)== 8, "Test failed for cube of 2"
    
def test_ft():
    assert fifth_pow(2)==32 , "Test failed for fifth power of 2"
    assert fifth_pow(3)==243,"test failed : fifth powerr of 3 hould be 243"
    
#test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")