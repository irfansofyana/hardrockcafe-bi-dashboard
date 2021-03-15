from scripts.schema.tables import Base, Customer, Cafe, Product, Promo, Time, Guest

def load_cafes_table(session, cafes):
    for cafe in cafes:
        row = Cafe (
            name        =cafe['name'],
            capacity    =cafe['capacity'],
            address     =cafe['address'],
            city        =cafe['city'],
            state       =cafe['state'],
            zip_code    =cafe['zip_code'],
            country     =cafe['country']
        )
        session.add(row)

    session.commit()
