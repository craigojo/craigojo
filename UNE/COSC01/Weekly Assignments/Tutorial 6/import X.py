import x
assert 3 == x.add(1, 2)
assert 1 == x.sub(3, 2)
assert -1 == x.sub(2, 3)
assert 6 == x.mul(2, 3)
assert 3.5 == x.div(7, 2)
assert 6 == x.calculate_strange_value(1, 2)
assert 2.0 == x.calculate_strange_value(2, 1)
assert 1 == x.calculate_strange_value(2, 2)
assert x.is_valid_positive_integer_input(1)
assert not x.is_valid_positive_integer_input(0)
assert not x.is_valid_positive_integer_input(-1)
assert not x.is_valid_positive_integer_input(1.5)
assert not x.is_valid_positive_integer_input("hello")