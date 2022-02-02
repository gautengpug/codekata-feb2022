import unittest
from unittest.mock import patch

from pacman import Pacman


class TestPacman(unittest.TestCase):
    # @patch('builtins.print')
    # def test_show(self, mock_print):
    #     p = Pacman()
    #     p.show()
    #     self.assertEqual(mock_print.call_count, 3)
    #     expected = [
    #         '[".", ".", "."]',
    #         '[".", "V", "."]',
    #         '[".", ".", "."]'
    #     ]
    #     # Failing right now
    #     self.assertEqual(mock_print.mock.call_args_list, expected) 

    def test_is_coords_in_range(self):
        p = Pacman()
        self.assertEqual(p.is_coords_in_range(2,2), True)
        self.assertEqual(p.is_coords_in_range(2,3), False)
        self.assertEqual(p.is_coords_in_range(3,2), False)
        self.assertEqual(p.is_coords_in_range(-1,2), False)
