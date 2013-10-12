#!/usr/bin/python
#
# Copyright (C) 2013 Martin Owens
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""
Test simple 'every' api.
"""

import os
import sys

sys.path.insert(0, '../')

import unittest
from crontab import CronTab, py3
try:
    from test import test_support
except ImportError:
    from test import support as test_support

if py3:
    unicode = str

class EveryTestCase(unittest.TestCase):
    """Test basic functionality of crontab."""
    def setUp(self):
        self.crontab = CronTab(tabfile='data/test.tab')

    def test_00_minutes(self):
        """Every Minutes"""
        for job in self.crontab:
            job.every(3).minutes()
            self.assertEqual(job.render_time(), '*/3 * * * *')

    def test_01_hours(self):
        """Every Hours"""
        for job in self.crontab:
            job.every(3).hours()
            self.assertEqual(job.render_time(), '0 */3 * * *')

    def test_02_dom(self):
        """Every Day of the Month"""
        for job in self.crontab:
            job.every(3).dom()
            self.assertEqual(job.render_time(), '0 0 */3 * *')

    def test_03_single(self):
        """Every Single Hour"""
        for job in self.crontab:
            job.every().hour()
            self.assertEqual(job.render_time(), '0 * * * *')

    def test_04_month(self):
        """Every Month"""
        for job in self.crontab:
            job.every(3).months()
            self.assertEqual(job.render_time(), '0 0 1 */3 *')

    def test_05_dow(self):
        """Every Day of the Week"""
        for job in self.crontab:
            job.every(3).dow()
            self.assertEqual(job.render_time(), '0 0 * * */3')

    def test_06_year(self):
        """Every Year"""
        for job in self.crontab:
            job.every().year()
            self.assertEqual(job.render_schedule(), '@yearly')
            self.assertEqual(job.render_time(), '* * * * *')
            self.assertRaises(ValueError, job.every(2).year)

    def test_07_reboot(self):
        """Every Reboot"""
        for job in self.crontab:
            job.every_reboot()
            self.assertEqual(job.render_schedule(), '@reboot')
            self.assertEqual(job.render_time(), '* * * * *')

if __name__ == '__main__':
    test_support.run_unittest(
       EveryTestCase,
    )
