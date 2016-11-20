import unittest
from Identifier import Identifier


class TestIdentifier(unittest.TestCase):


    def test_parse(self):
        """
        Smoke test for the execute method
        """
        iden = Identifier("%(identifier)s ")
        iden.execute({"identifier":"transformation count"})

if __name__ == '__main__':
    unittest.main()