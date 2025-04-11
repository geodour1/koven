from db.connector import DBConnector
from models.user import User
from helpers.logger import Logger

from flask import Request, flash, render_template, redirect


class UserController:
    def __init__(self, db_connector: DBConnector):
        self.db_connector = db_connector

    def get_users(self, request: Request):
        users = self.db_connector.user_all()
        return render_template(
            'users.html',
            users=users
        )

    def add_user(self, request: Request):
        if request.method == 'GET':
            return render_template(
                'user_add.html'
            )
        try:
            if user_name := request.form.get("name"):
                Logger.print(user_name)
                user = User(name=user_name)
                user = self.db_connector.user_insert_one(user)
                flash(f'User added successfully!\n id: {user.id}', 'success')

        except Exception as e:
            flash(f'Failed to add user.', 'error')
            Logger.log_error(e.__str__())

        return redirect(
            '/users'
        )