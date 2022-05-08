from django.test import TestCase

# Create your tests here.
import datetime

time = datetime.datetime.strptime("1992-12-12", '%Y-%m-%d')
print(time)

lis = ["思修", "篮球"]

res = ",".join(["思修", "篮球"])
print(res)
