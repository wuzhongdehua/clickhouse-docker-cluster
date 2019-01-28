import argparse
from clickhouse_driver import Client

parser = argparse.ArgumentParser(description='Deleting tables on one of ClickHouse shards')
parser.add_argument('shard', choices=['1', '2'], help='ClickHouse shard')

args = parser.parse_args()

if args.shard == '1':
    server = 'server1'
else:
    server = 'server2'

client = Client(server)
partition = client.execute('SELECT partition FROM system.parts LIMIT 1')[0][0]
client.execute('ALTER TABLE test_shared DROP PARTITION ' + partition)
