import random
import hashlib
from datetime import date
from clickhouse_driver import Client

client = Client('server1')
rowId = random.randrange(4294967295)
dataSet = []

for i in range(1000):
    dataSet.append([date.today(), rowId, hashlib.md5(bytes(i)).hexdigest()])

client = Client('server1')
client.execute(
    'INSERT INTO test VALUES ',
    dataSet
)
