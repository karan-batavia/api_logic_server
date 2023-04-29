from project import db
from project.models import User
from project.model2 import Specie


# insert data
db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("mike", "mike@herman.com", "tell"))

Specie.query.all()

Specie.query.add_columns()

# commit the changes
db.session.commit()
