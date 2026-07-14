from app.database.session import engine
from app.models.base import Base

# Import all models so Base knows about them
import app.models.user
import app.models.submission
import app.models.streak

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created.")
