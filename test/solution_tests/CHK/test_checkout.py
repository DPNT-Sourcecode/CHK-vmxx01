from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_illegal_input(self):
        assert checkout("") == -1
        assert checkout("E") == -1
        assert checkout("a") == -1
        assert checkout("123") == -1

    def test_unit_input(self):
        assert checkout("A") == 50
        assert checkout("B") == 30
        assert checkout("C") == 20
        assert checkout("D") == 15

    def test_multiple_inputs(self):
        assert checkout("ABCD") == 115
        assert checkout("AABCD") == 165
        assert checkout("AAABCD") == 195
        assert checkout("AAABB") == 175
        assert checkout("AAABBCCDD") == 245

    def test_unordered_inputs(self):
        assert checkout("CDBADCBAA") == 245
    

