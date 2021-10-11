from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_illegal_input(self):
        assert checkout("a") == -1
        assert checkout("123") == -1

    def test_unit_input(self):
        assert checkout("") == 0 # Apparently people checkout empty baskets
        assert checkout("A") == 50
        assert checkout("B") == 30
        assert checkout("C") == 20
        assert checkout("D") == 15
        assert checkout("E") == 40

    def test_multiple_inputs(self):
        assert checkout("ABCD") == 115
        assert checkout("AABCD") == 165
        assert checkout("AAABCD") == 195
        assert checkout("AAABB") == 175
        assert checkout("AAAAAABBBB") == 340
        assert checkout("AAABBCCDD") == 245
        assert checkout("AAAAAAAA") == 330
        assert checkout("AAAAAAAAA") == 380
        assert checkout("AAAAAAAAAA") == 400

    def test_unordered_inputs(self):
        assert checkout("CDBADCBAA") == 245

    def test_cross_offers(self):
        assert checkout("EE") == 80
        assert checkout("EEB") == 80
        assert checkout("EEBB") == 95
        assert checkout("EEBBB") == 125
        assert checkout("EEEEBB") == 160

