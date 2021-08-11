# [smart-room-schema]

Database schema for smart room related projects

## Prerequisitive

* Software

| Category | Version |
| --- | --- |
| docker | 18.09.7 |
| docker-compose | 1.17.1 |
| GNU Make | 4.1 |
| Python | 3.7 |
| pipenv(Python module) | 2018.11.26 |

## QuickStart

1. Initialize environment
```
make init
```

2. Start the service
```
make service_up
```

3. Migrate to current version
```
make migrate
```

4. (Optional) Shutdown the service
```
make service_down
```

* Upgrade/Downgrade migrations

```
cd migrations/ && pipenv run alembic upgrade +<number> / <sha_key>
cd migrations/ && pipenv run alembic downgrade -<number> / <sha_key>
```

* Genrate migration
```
cd migrations/ && pipenv run alembic revision --autogenerate -m "Migrate message"
cd migrations/ && pipenv run alembic upgrade head
```

## Cheatsheets

Enter database(with default config)
```
psql postgresql://postgres:password@localhost:5432/database
```

## Landmines!

Alembic will sort table creation order if it does not specified.

Sometime it will occur `NoReferencedTableError` since required table haven't created.


Add relation object ex: `foo = relationship('Tablename')` to specify this relationship

Then in the column use object to reference this relationship

Ex: `bar = Column(INT, ForeignKey('foo.property'))`

Example scenario:

`fun.boo` make a reference key to `boo` in `far` table.

```
    class Far():
        boo = Column(VARCHAR)

    class Fun():
        boo = Column(VARCHAR, ForeignKey('test.foo'))
        test = relationship('Far')
```

* Auto generate issue

Since `autogenerate` will scan through the Model table

We need to add new table in `model.model_list.py` and import `model.model_list` or it can't find the available table.
