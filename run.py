from app.views import app
from app import db


@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)