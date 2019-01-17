# ClickHouse Docker Cluster

A ClickHouse cluster in a Docker containers.

The project shows an example of a serial connection of cluster instances.

## Getting started

### Prerequisites

`docker 18.06.0+`

`docker-compose`

### Installing

`git clone https://github.com/Gorynychdo/clickhouse-docker-cluster.git`

`cd clickhouse-docker-cluster`

`docker-compose up`

### Steps

* At first there is one instance of cluster.

* Creating tables:

    `docker-compose exec app python app/create.py`

    This command creates replicated tables 'test_shared' with custom
    composite partition key on all clickHouse servers.
    Also it creates distributed table 'test' on server1

* Connect the second shard:

    `rm -f configs/server1.xml && ln -s server1/distributed.xml configs/server1.xml`

    `docker-compose restart server1`

* Connect replicas to shards:

    `rm -f configs/server1.xml && ln -s server1/replicated.xml configs/server1.xml`

    `docker-compose restart server1`

* Reset state at last:

    `rm -f configs/server1.xml && ln -s server1/mono.xml configs/server1.xml`

    `docker-compose restart server1`

## Authors

* **Igor Sannikov** - [Gorynychdo](https://github.com/Gorynychdo)

## License

This project is licensed under the MIT License
