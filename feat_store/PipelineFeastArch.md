###### Feast Arch

```
project: feature_demo
# By default, the registry is a file (but can be turned into a more scalable SQL-backed registry)
registry: data/registry.db
# The provider primarily specifies default offline / online stores & storing the registry in a given cloud
provider: local
online_store:
    type: sqlite
    path: data/online_store.db
entity_key_serialization_version: 3
# By default, no_auth for authentication and authorization, other possible values kubernetes and oidc. Refer the documentation for more details.
auth:
    type: no_auth

```


###### Online store options
- Redis, Dragonfly, Valkey
- cloud managed NoSQL 
    - aws Dynamodb, azure cosmodb/bigtable, google cloud datastore
- SQL Stores
    - postGresSQL, Mysql, Singlestore
- Vector abd specialized bs
    - milvus, qdrant, Elastisearch, cassandra