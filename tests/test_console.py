#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsile(unittest.TestCase):
    """This test the console"""

    @classmethod
    def setUpClass(cls):
        """setup the test"""
        cls.consol = HBNBCommand()

    def test_create_command(self):
        """test create command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="amira@.com" password="123456"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
        with patch('builtins.input', return_value="create User name='amira' age=25") as mock_input:
            self.console.onecmd("create User name='amira' age=25")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())


if __name__ == '__main__':
    unittest.main()
