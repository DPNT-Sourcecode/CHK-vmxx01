from lib.solutions.CHK.checkout_solution import checkout
from lib.solutions.CHK.price_table import PRICE_TABLE


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
        assert checkout("F") == 10
        assert checkout("G") == 20
        assert checkout("H") == 10
        assert checkout("I") == 35
        assert checkout("J") == 60
        assert checkout("K") == 70
        assert checkout("L") == 90
        assert checkout("M") == 15
        assert checkout("N") == 40
        assert checkout("O") == 10
        assert checkout("P") == 50
        assert checkout("Q") == 30
        assert checkout("R") == 50
        assert checkout("S") == 20
        assert checkout("T") == 20
        assert checkout("U") == 40
        assert checkout("V") == 50
        assert checkout("W") == 20
        assert checkout("X") == 17
        assert checkout("Y") == 20
        assert checkout("Z") == 21

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
        assert checkout("FF") == 20
        assert checkout("FFF") == 20
        assert checkout("FFFF") == 30
        assert checkout("FFFFF") == 40
        assert checkout("FFFFFF") == 40
        assert checkout("FAAAAAFFFFF") == 240
        assert checkout("HHHHH") == 45
        assert checkout("HHHHHHHHHH") == 80
        assert checkout("KK") == 120
        assert checkout("PPPPP") == 200
        assert checkout("QQQ") == 80
        assert checkout("UUUU") == 120
        assert checkout("VV") == 90
        assert checkout("VVV") == 130

    def test_unordered_inputs(self):
        assert checkout("CDBADCBAA") == 245

    def test_cross_offers(self):
        assert checkout("EE") == 80
        assert checkout("EEB") == 80
        assert checkout("EEBB") == 110
        assert checkout("EEBBB") == 125
        assert checkout("EEEEBB") == 160
        assert checkout("ABCDEABCDE") == 280
        assert checkout("CCADDEEBBA") == 280
        assert checkout("ABCDECBAABCABBAAAEEAA") == 665
        assert checkout("NNNM") == 120
        assert checkout("NNNMM") == 135
        assert checkout("RRRQ") == 150
        assert checkout("RRRQQ") == 180

    def test_group_offers(self):
        for combo in ['STX', 'STY', 'STZ', 'SXT', 'SXY', 'SXZ', 'SYT', 'SYX', 'SYZ', 'SZT', 'SZX', 'SZY', 'TSX', 'TSY', 'TSZ', 'TXS', 'TXY', 'TXZ', 'TYS', 'TYX', 'TYZ', 'TZS', 'TZX', 'TZY', 'XST', 'XSY', 'XSZ', 'XTS', 'XTY', 'XTZ', 'XYS', 'XYT', 'XYZ', 'XZS', 'XZT', 'XZY', 'YST', 'YSX', 'YSZ', 'YTS', 'YTX', 'YTZ', 'YXS', 'YXT', 'YXZ', 'YZS', 'YZT', 'YZX', 'ZST', 'ZSX', 'ZSY', 'ZTS', 'ZTX', 'ZTY', 'ZXS', 'ZXT', 'ZXY', 'ZYS', 'ZYT', 'ZYX']:
            assert checkout(combo) == 45
            for letter in ['S', 'T', 'X', 'Y', 'Z']:
                assert checkout(combo + letter) == 45 + PRICE_TABLE[letter]['price']
        
        assert checkout("SSSSS") == 85
        assert checkout("SSSSSS") == 90
        assert checkout("TTTTTT") == 90