# -*- coding: utf-8 -*-
##############################################################################

'''
'''

##############################################################################
# Imports


import unittest

from decimal import Decimal
from itertools import chain

from flightdatautilities.units import *  # flake8: noqa


##############################################################################
# Test Cases


class TestUnitsModule(unittest.TestCase):

    def test__check_definitions(self):

        values = set(available())
        constants =  set(available(values=False)[1])
        # Check we have no redefinitions of units:
        self.assertEqual(len(values), len(constants), 'Unit redefinition!')
        # Check we have a category for every unit constant:
        x = list(chain.from_iterable(UNIT_CATEGORIES.values()))
        self.assertEqual(len(x), len(set(x)), 'Unit in multiple categories!')
        self.assertItemsEqual(set(x), values)
        # Check we have a description for every unit constant:
        self.assertItemsEqual(set(UNIT_DESCRIPTIONS.keys()), values)
        # Check we only correct to (and not from) standard units:
        self.assertLessEqual(set(UNIT_CORRECTIONS.values()), values)
        self.assertEqual(set(UNIT_CORRECTIONS.keys()) & values, set())
        # Check we only convert to and from standard units:
        self.assertLessEqual(set(STANDARD_CONVERSIONS.keys()), values)
        self.assertLessEqual(set(STANDARD_CONVERSIONS.values()), values)
        for mapping in CONVERSION_MULTIPLIERS, CONVERSION_FUNCTIONS:
            for k, v in mapping.iteritems():
                self.assertIn(k, values)
                self.assertLessEqual(set(v.keys()), values)

    @unittest.skip('Test not implemented.')
    def test__normalise(self):

        pass

    @unittest.skip('Test not implemented.')
    def test__function(self):

        pass

    @unittest.skip('Test not implemented.')
    def test__multiplier(self):

        pass

    def test__convert(self):

        data = {
            # Angles:
            (1, DEGREE, RADIAN): 0.0174532925,
            (1, RADIAN, DEGREE): 57.2957795,
            # Flow (Volume):
            (1, LB_H, KG_H): 0.453592,
            (1, LB_H, TONNE_H): 0.000453592,
            (1, KG_H, LB_H): 2.20462,
            (1, KG_H, TONNE_H): 0.001,
            (1, TONNE_H, LB_H): 2204.62,
            (1, TONNE_H, KG_H): 1000,
            # Force:
            (1, LBF, KGF): 0.45359237,
            (1, LBF, DECANEWTON): 0.444822162,
            (1, LBF, NEWTON): 4.44822162,
            (1, KGF, LBF): 2.20462262,
            (1, KGF, DECANEWTON): 0.980665,
            (1, KGF, NEWTON): 9.80665,
            (1, DECANEWTON, LBF): 2.24808943,
            (1, DECANEWTON, KGF): 1.01971621,
            (1, DECANEWTON, NEWTON): 10,
            (1, NEWTON, LBF): 0.224808943,
            (1, NEWTON, KGF): 0.101971621,
            (1, NEWTON, DECANEWTON): 0.1,
            # Frequency:
            (1, KHZ, MHZ): 0.001,
            (1, KHZ, GHZ): 0.000001,
            (1, MHZ, KHZ): 1000.0,
            (1, MHZ, GHZ): 0.001,
            (1, GHZ, KHZ): 1000000.0,
            (1, GHZ, MHZ): 1000.0,
            # Length:
            (1, FT, METER): 0.3048,
            (1, FT, KM): 0.0003048,
            (1, FT, MILE): 0.000189394,
            (1, FT, NM): 0.000164579,
            (1, METER, FT): 3.28084,
            (1, METER, KM): 0.001,
            (1, METER, MILE): 0.000621371,
            (1, METER, NM): 0.000539957,
            (1, KM, FT): 3280.84,
            (1, KM, METER): 1000,
            (1, KM, MILE): 0.621371,
            (1, KM, NM): 0.539957,
            (1, MILE, FT): 5280,
            (1, MILE, METER): 1609.34,
            (1, MILE, KM): 1.60934,
            (1, MILE, NM): 0.868976,
            (1, NM, FT): 6076.12,
            (1, NM, METER): 1852,
            (1, NM, KM): 1.852,
            (1, NM, MILE): 1.15078,
            # Mass:
            (1, LB, KG): 0.453592,
            (1, LB, TONNE): 0.000453592,
            (1, KG, LB): 2.20462,
            (1, KG, TONNE): 0.001,
            (1, TONNE, LB): 2204.62,
            (1, TONNE, KG): 1000,
            # Pressure:
            (1, INHG, MILLIBAR): 33.86,
            (1, INHG, PSI): 0.4910,             # Google: 0.49109778
            (1, MILLIBAR, INHG): 0.029533,      # Google: 0.0295333727
            (1, MILLIBAR, PSI): 0.0145037738,
            (1, PSI, INHG): 2.0362,             # Google: 2.03625437
            (1, PSI, MILLIBAR): 68.94757,       # Google: 68.9475729
            # Speed:
            (1, KT, MPH): 1.15078,
            (1, KT, FPM): 101.2686,
            (1, MPH, KT): 0.868976,
            (1, MPH, FPM): 88.0002,
            (1, FPM, KT): 0.0098747300,
            (1, FPM, MPH): 0.0113636364,
            (1, FPM, FPS): 60.0,
            (1, FPS, FPM): 0.016666666666666666,
            # Temperature:
            (0, CELSIUS, FAHRENHEIT): 32,
            (0, CELSIUS, KELVIN): 273.15,
            (0, FAHRENHEIT, CELSIUS): -17.7778,
            (0, FAHRENHEIT, KELVIN): 255.372,
            (0, KELVIN, CELSIUS): -273.15,
            (0, KELVIN, FAHRENHEIT): -459.67,
            # Time:
            (1, HOUR, MINUTE): 60,
            (1, HOUR, SECOND): 3600,
            (1, MINUTE, HOUR): 0.0166667,
            (1, MINUTE, SECOND): 60,
            (1, SECOND, HOUR): 0.000277778,
            (1, SECOND, MINUTE): 0.0166667,
            # Volume:
            (1, PINT, QUART): 0.5,
            (1, QUART, PINT): 2,
            # Other:
            (1, GS_DDM, DOTS): 11.428571428571429,
            (1, LOC_DDM, DOTS): 12.903225806451614,
            (1, MILLIVOLT, DOTS): 0.01333333333333333,
            (1, MICROAMP, DOTS): 0.01333333333333333,
            (1, DOTS, GS_DDM): 0.0875,
            (1, DOTS, LOC_DDM): 0.0775,
            (1, DOTS, MILLIVOLT): 75,
            (1, DOTS, MICROAMP): 75,
        }

        for arguments, expected in data.iteritems():
            dp = max(abs(Decimal(str(expected)).as_tuple().exponent) - 1, 0)
            # Check forward conversion:
            i = arguments
            o = expected
            m = 'Invalid conversion from %s --> %s' % i[1:]
            self.assertAlmostEqual(convert(*i), o, places=dp, msg=m)
            # Check backward conversion:
            i = tuple([expected] + list(arguments)[:0:-1])
            o = arguments[0]
            m = 'Invalid reverse conversion from %s --> %s' % i[1:]
            self.assertAlmostEqual(convert(*i), o, delta=0.001, msg=m)


##############################################################################
# vim:et:ft=python:nowrap:sts=4:sw=4:ts=4
