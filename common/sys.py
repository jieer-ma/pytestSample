#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/25
# desc：该文件中存放全局使用的系统函数，如：移动时间，获取时间等


import datetime
import time

class DateTime(object):
    def __init__(self):
        self.now = datetime.datetime.now()

    def shiftDays(self, days):
        shift_days = datetime.timedelta(days=days)
        new_time = self.now + shift_days

        return new_time

    def shiftHours(self, hours):
        shift_hours = datetime.timedelta(hours=hours)
        new_time = self.now + shift_hours

        return new_time

    def shiftMinutes(self, minutes):
        shift_minutes = datetime.timedelta(minutes=minutes)
        new_time = self.now + shift_minutes

        return new_time

    def shiftSeconds(self, seconds):
        shift_seconds = datetime.timedelta(seconds=seconds)
        new_time = self.now + shift_seconds

        return new_time


date_time = DateTime()
