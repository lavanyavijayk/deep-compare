import unittest

from datetime import datetime, date

from deep_compare import CompareVariables


class test_schedule_data_ingress_job(unittest.TestCase):

    def test_compare(self):
        self.assertEqual(CompareVariables.deep_compare('',None),True)

    def test_compare_1(self):
        self.assertEqual(CompareVariables.deep_compare(0,None),True)

    def test_number_compare(self):
        self.assertEqual(CompareVariables.deep_compare('3 ',3),True)

    def test_number_compare_1(self):
        self.assertEqual(CompareVariables.deep_compare(0,-0.00),True)

    def test_complex_number_compare(self):
        self.assertEqual(CompareVariables.deep_compare('3 + 4j',3 + 4j),True)

    def test_array_compare(self):
        self.assertEqual(CompareVariables.deep_compare('["5"," 0","6"]',[5,6,0]),True)
    
    def test_set_compare(self):
        self.assertEqual(CompareVariables.deep_compare('{"5","6"," 0"}',{5,6,0}),True)

    def test_tuple_compare(self):
        self.assertEqual(CompareVariables.deep_compare('("5","6"," 0")',(5,6,0)),True)

    def test_dict_compare(self):
        self.assertEqual(CompareVariables.deep_compare('{"5":"6","4":" 0"}',{5:6,4:0}),True)

    def test_dict_compare_1(self):
        self.assertEqual(CompareVariables.deep_compare('{"4":" 0","5":"6"}',{5:6,4:0}),True)

    def test_date_compare(self):
        self.assertEqual(CompareVariables.deep_compare(date(2020,5,2),'2020-05-02'),True)

    def test_date_compare_1(self):
        self.assertEqual(CompareVariables.deep_compare(date(2020,5,2),'2020-05-02 12:48'),True)

    def test_date_compare_2(self):
        self.assertEqual(CompareVariables.deep_compare('2020-05-02 12:48','2020-05-02',date_only = True),True)    

    def test_date_compare_3(self):
        self.assertEqual(CompareVariables.deep_compare(datetime(2020,5,2,12,48),datetime(2020,5,2,10,18),date_only = True),True)    

    def test_datetime_compare(self):
        self.assertEqual(CompareVariables.deep_compare(datetime(2020,5,2,12,48),'2020-05-02 12:48'),True)
        

if __name__ == '__main__':
   unittest.main()

