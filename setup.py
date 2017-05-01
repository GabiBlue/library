from app import db
import models


def create_database():
    print("Create database ...")
    db.create_all()


if __name__ == '__main__':
    create_database()
    print("READY")