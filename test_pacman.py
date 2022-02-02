import unittest
from unittest.mock import patch

from pacman import Pacman


class TestPacman(unittest.TestCase):
    @patch('builtins.print')
    def test_show(self, mock_print):
        p = Pacman()
        p.show()
        self.assertEqual(mock_print.call_count, 3)
        expected = [
            '[".", ".", "."]',
            '[".", "V", "."]',
            '[".", ".", "."]'
        ]
        # Failing right now
        self.assertEqual(mock_print.mock.call_args_list, expected) 
