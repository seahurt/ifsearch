import os
import django
pwd = os.getcwd()
os.chdir('..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'IF.settings'
django.setup()
os.chdir(pwd)
from models import If


def readif(file):
    ifset = []
    with open(file) as f:
        for line in f.readlines():
            if 'Rank' in line:
                continue
            info = line.strip().split('\t')
            ifset.append((info[1], info[3]))
    return ifset


def save2db(dbif, year):
    dbset = []
    for x in dbif:
        dbset.append(If(journal=x[0], iff=x[1], year=year))
    If.objects.bulk_create(dbset)


db2017 = readif('data/Journal Impact factor_2017.txt')
db2016 = readif('data/Journal Impact factor_2016.txt')

save2db(db2017, '2017')
save2db(db2016, '2016')
