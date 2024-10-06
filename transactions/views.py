from datetime import datetime
from sqladmin import ModelView
from transactions.models import UserTransaction

class TransactionAdmin(ModelView, model=UserTransaction):
    name = "Transaction"
    name_plural = "Transactions"
    list_template = "list_statistic.html"

    page_size = 5

    form_columns = [
        UserTransaction.user,
        UserTransaction.type,
        UserTransaction.amount,
    ]

    column_list = [
        UserTransaction.id,
        'user.user_name',  # Используем user.user_name для списка
        UserTransaction.type,
        UserTransaction.amount,
        UserTransaction.create_at
    ]

    column_labels = {
        'user.user_name': 'User Name',
        UserTransaction.type: 'Type',
        UserTransaction.amount: 'Amount',
        UserTransaction.create_at: 'Created At'
    }

    column_details_list = ["user.user_name", UserTransaction.type, UserTransaction.amount, UserTransaction.create_at]

    @staticmethod
    def datetime_format(value):
        return value.strftime("%d.%m.%Y %H:%M")

    column_type_formatters = {
        **ModelView.column_type_formatters,
        datetime: datetime_format
    }
