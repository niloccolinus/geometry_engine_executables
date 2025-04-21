# Tests for verifying proper Vector functionality

from vector import Vector

class TestVector:
    def add_1(self):
    	# Standard case
    	v = Vector([3, 4])
    	v2 = Vector([4, 2])
        r = v.add(v2) # The "Add" method needs to return its end result
        assert r == [7, 6]

    def add_2(self):
    	# Zeros case
    	v = Vector([3, 4])
    	v2 = Vector([0, 0])
        r = v.add(v2)
        assert r == v.vector

    def mul_1(self):
        # Multiplication by int
        v = Vector([3, 4])
        f = 2
        r = v.multiply_by(f) # Same as above
        assert r == [6, 8]
    
    def mul_2(self):
        # Multiplication by zero
        v = Vector([3, 4])
        f = 0
        r = v.multiply_by(f)
        assert r == [0, 0]
    
    def mul_3(self):
        # Multiplication by negative number
        v = Vector([3, 4])
        f = -2
        r = v.multiply_by(f)
        assert r == [-6, -8]
    
    def mul_4(self):
        # Multiplication by float
        v = Vector([3, 4])
        f = 2.5
        r = v.multiply_by(f)
        assert r == [7.5, 10.0]

    def mul_5(self):
        # Multiplication by negative float
        v = Vector([3, 4])
        f = -2.5
        r = v.multiply_by(f)
        assert r == [-7.5, -10.0]

    def mul_6(self):
        # Multiplication by vector
        v = Vector([3, 4])
        v2 = Vector([4, 2])
        r = v.multiply(v2)
        assert r == [12, 8]