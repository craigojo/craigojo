import fahrenheit_to_celcius

epsilon = 0.001

def test_correct():
    assert abs(temp.fahrenheit_to_celcius(68) -20) <epsilon


def test_absolute_zero():
    try:
        temp.fahrenheit_to_celcius(-500)
    except AssertionError:
        pass
    else:
        assert False, "Absololute zero not handled"
def test_absolute_zero():
    try:
        temp.fahrenheit_to_celcius(-500)
    except AssertionError():
        pass
    else:
        assert False, "Absolute zero not handled"

test_correct()
test_absolute_zero()
print("All tests completed successfully")








# assert fahrenheit_to_celcius(68) == 20