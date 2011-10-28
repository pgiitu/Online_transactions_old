from transactions.models import Transaction
from transactions.models import Connected_Accounts
from transactions.models import Bank
from transactions.models import State
from transactions.models import Branch
from django.contrib import admin

admin.site.register(Transaction)
admin.site.register(Connected_Accounts)
admin.site.register(Bank)
admin.site.register(State)
admin.site.register(Branch)
