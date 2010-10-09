#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test defs element
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import Group, Defs, parameter

from svgwrite.interface import ITransform

class TestDefs(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        defs = Defs()
        self.assertTrue(isinstance(defs, ITransform))
        self.assertTrue(isinstance(defs, Group))
        self.assertEqual(defs.tostring(), "<defs />")

    def test_add_subelement(self):
        defs = Defs(id='defs')
        group = Group(id='group')
        defs.add(group)
        self.assertEqual(defs.tostring(), '<defs id="defs"><g id="group" /></defs>')

    def test_add_group(self):
        defs = Defs(id='defs')
        group = defs.group(id='group') # implicit call of add
        self.assertEqual(defs.tostring(), '<defs id="defs"><g id="group" /></defs>')


if __name__=='__main__':
    unittest.main()