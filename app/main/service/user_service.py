import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    """Saves a new user.

    Args:
        data: The user data.
    Returns:
        The response object.
    """
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    """Gets all the users.

    Returns: The users.
    """
    return User.query.all()


def get_a_user(public_id):
    """Gets a user.

    Args:
        public_id: The public user identifier.
    Returns:
        The user with the gicen public identifier.
    """
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    """Commits the changes to database.

    Args:
        data: The data to be commited.
    """
    db.session.add(data)
    db.session.commit()
