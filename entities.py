from pony.orm import *

db = Database()


class Posao(db.Entity):
    id = PrimaryKey(int, auto=True)

    adresa = Required(str)
    datum = Required(str)
    vrijeme = Required(str)

    klima = Required(str)
    radnik = Required(str)

    cijena = Required(float)

    obavljeno = Required(bool, default=False)


db.bind(
    provider='sqlite',
    filename='raspored.sqlite',
    create_db=True
)

db.generate_mapping(create_tables=True)