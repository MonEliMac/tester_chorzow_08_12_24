from kod import fizzbuss

def test_fizzbuss_number():
    assert fizzbuss(1) == 1
    assert fizzbuss(2) == 2

def test_fizzbuss_fizz():
    assert fizzbuss(3) == "Fizz"
    assert fizzbuss(6) == "Fizz"
    assert fizzbuss(9) == "Fizz"

def test_fizzbuss_buss():
    assert fizzbuss(5) == "Buss"
    assert fizzbuss(10) == "Buss"
    assert fizzbuss(35) == "Buss"

def test_fizzbuss_fizzbuss():
    assert fizzbuss(15) == "FizzBuss"
    assert fizzbuss(45) == "FizzBuss"
    assert fizzbuss(150) == "FizzBuss"

def test_fizzbuss_string():
    assert fizzbuss("Mama") == None

def test_fizzbuss_float():
    assert fizzbuss("Mama") == None


def test_fizzbuss_negative():
    assert fizzbuss(-3) == None

