import pytest
from Fixture.db import Database
 
@pytest.fixture
# fixtures provide a fresh instace of the database class and cleanup after the test. 
def db():
   database = Database()
   yield database      # provide the fixture instance 
   database.data.clear()   # cleanup step (not needed for in memory. but usefull for real db)


def test_add_user(db):
    db.add_user(1, "Rani")

def test_add_dupicate_user_db(db):
    db.add_user(1, "Rani")
    with pytest.raises(ValueError, match="user already exist"):
        db.add_user(1, "Bob")

def test_delete_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert 2 not in db.data