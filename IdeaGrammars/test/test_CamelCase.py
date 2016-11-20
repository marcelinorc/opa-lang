import unittest

from CamelCase import CamelCase

class TestCamelCase(unittest.TestCase):

    def test_parse(self):
        """
        Smoke test for the execute method
        """
        iden = CamelCase("%(identifier)s ")
        iden.execute({"identifier":"transformation count"})

if __name__ == '__main__':
    unittest.main()