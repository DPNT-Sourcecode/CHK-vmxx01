from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_illegal_input(self):
        assert checkout("") == -1
        assert checkout("E") == -1
        assert checkout("123") == -1

