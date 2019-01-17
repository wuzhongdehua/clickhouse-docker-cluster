from clickhouse_driver import Client

for server in ['server1', 'server2', 'server3', 'server4']:
    client = Client(server)
    client.execute(
        'CREATE TABLE IF NOT EXISTS test_shared ('
            'event_date Date, '
            'id UInt32, '
            'data String '
        ') ENGINE = ReplicatedMergeTree(\'/clickhouse/tables/{id_shard}/test_shared\', \'{replica}\') '
        'PARTITION BY (event_date, id) '
        'ORDER BY (event_date, id)'
    )

    if server == 'server1':
        client.execute(
            'CREATE TABLE IF NOT EXISTS test AS test_shared '
            'ENGINE = Distributed(test_shard, default, test_shared, intHash32(id))'
        )
