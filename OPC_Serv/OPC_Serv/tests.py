# файл tests.py
import unittest
import OPC_Serv # тестируемый модуль

class TestOPC_Serv(unittest.TestCase):
    # начинается с test_
    def test_set_open(self):
        self.assertTrue(OPC_Serv.Valve.set_open())
        #self.assertEqual(OPC_Serv.dValve.get_open(),True)
        #self.assertFalse(OPC_Serv.dValve.get_open())


    # начинается с test_
    #def test_is_positive(self):
    #    self.assertTrue(OPC_Serv.is_positive(1))


if __name__ == "__main__":
    unittest.main()



