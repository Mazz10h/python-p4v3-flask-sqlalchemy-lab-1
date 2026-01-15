import pytest
from app import app
from models import db, Earthquake


@pytest.fixture(scope='function')
def client():
    with app.app_context():
        # Create all database tables
        db.create_all()
        
        # Seed the database with test data
        Earthquake.query.delete()
        db.session.add(Earthquake(magnitude=9.5, location="Chile", year=1960))
        db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964))
        db.session.add(Earthquake(magnitude=8.6, location="Alaska", year=1946))
        db.session.add(Earthquake(magnitude=8.5, location="Banda Sea", year=1934))
        db.session.add(Earthquake(magnitude=8.4, location="Chile", year=1922))
        db.session.commit()
        
        yield app.test_client()
        
        # Clean up after tests
        db.session.remove()
        db.drop_all()

