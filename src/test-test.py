# -*- coding: utf-8 -*-
__author__ = 'soroosh'

import random
import unittest
import xml.etree.cElementTree as ET
from  xml.dom.minidom import *
import sys

# class MyWriter:
#     def __init__(self):
#         self._result = ''
#     def write(self,txt):
#
#

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        print 'test setup'
        self.doc = ET.Element('numbers')

    def test_should_add_one_number(self):
        # make sure the shuffled sequence does not lose any elements

        sub_element = ET.SubElement(self.doc, 'number')
        sub_element.set('user','soroosh')
        sub_element.text = '09122502092'

        xml.dom.minido
        ET.ElementTree(self.doc).write(sys.stdout)
        self.assertEqual(self.doc, self.doc)

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)
    #
    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)


if __name__ == '__main__':
    unittest.main()