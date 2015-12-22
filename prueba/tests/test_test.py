from unittest import TestCase

import prueba

class TestTest(TestCase):
    def test_is_string(self):
        s = prueba.test()
        self.assertTrue(isinstance(s, basestring))
