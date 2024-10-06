# transactions/models.py
from sqladmin import ModelView

from users.models import User


class UserAdmin(ModelView, model=User):
    name = "User"
    name_plural = "Users"

    column_list = [User.id, User.user_name]
    form_columns = ['user_name']
    column_details_list = [User.id, User.user_name]

    column_labels = {
        User.id: "ID",
        User.user_name: "Username",
    }

