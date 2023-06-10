from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Testing the methods and relationships
    # Retrieve a dev from the database by its attributes
    dev = session.query(Dev).filter_by(name='John Doe').first()
    print(f"Dev: {dev.name}")

    # View the companies that the dev has collected freebies from
    for company in dev.companies:
        print(f"Company: {company.name}")

    # Retrieve a company from the database by its attributes
    company = session.query(Company).filter_by(name='Example Corp').first()
    print(f"Company: {company.name}")

    # View the freebies for the company
    for freebie in company.collected_freebies:
        print(f"Freebie: {freebie.item_name}")

    # View the devs who collected freebies from the company
    for dev in company.devs:
        print(f"Dev: {dev.name}")

    # Create a new freebie
    new_freebie = Freebie(item_name='New Item', value=5, dev=dev, company=company)
    session.add(new_freebie)
    session.commit()

    # View the freebies that the dev has collected
    for freebie in dev.collected_freebies:
        print(f"Freebie: {freebie.item_name}")

    # View the companies that the dev has collected freebies from
    for company in dev.companies:
        print(f"Company: {company.name}")

    # Close the session
    session.close()
