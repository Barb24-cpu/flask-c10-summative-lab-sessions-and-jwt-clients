from config import app, db, api
from models import User, Note

if __name__ == "__main__":
    app.run(port=5555, debug=True)