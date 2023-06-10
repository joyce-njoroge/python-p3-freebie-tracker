#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create a dev instance
dev = Dev(name='John Doe')
session.add(dev)
session.commit()

# Create a company instance
company = Company(name='Example Corp', founding_year=2000)
session.add(company)
session.commit()

# Create a freebie instance and associate it with dev and company
freebie = Freebie(item_name='Free Item', value=10, dev=dev, company=company)
session.add(freebie)
session.commit()

# Test your code by querying the relationships
freebies = session.query(Freebie).all()
for freebie in freebies:
    print(f"Freebie: {freebie.item_name}")
    print(f"Dev: {freebie.dev.name}")
    print(f"Company: {freebie.company.name}")
    print()
