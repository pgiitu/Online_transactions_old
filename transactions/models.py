from django.db import models


class Transaction(models.Model):
    t_transaction_id = models.CharField(max_length=20)  #transaction ID
    t_sender_acc_no = models.CharField(max_length=10)
    t_receiver_acc_no = models.CharField(max_length=10)  
    t_start_date = models.DateTimeField('Start Date')  #date on which the transactions was requested
    t_end_date = models.DateTimeField('End Date')    #date on which the transactions was completed
    t_status=models.IntegerField()                  # we can define the various staus code for the successful and unsuccessful transactions
    t_transaction_type = models.IntegerField()     # 0 for funds transfer   1 for Third party  2 for Inter bank
    def __unicode__(self):
        return self.t_transaction_id

class Connected_Accounts(models.Model):
    ca_host_acc_no = models.CharField(max_length=10)
    ca_connected_acc_no = models.CharField(max_length=10)
    ca_addition_date = models.DateTimeField('Date Of Addition')   
    ca_transfer_limit=models.IntegerField()   #transfer limit for the connected account
    ca_ifsc_code=models.IntegerField()        #IFSC Code for the branch
    ca_acc_type=models.IntegerField()    # 1 for Third party  2 for Inter bank
    def __unicode__(self):
        return self.ca_host_acc-no

class Bank(models.Model):
    bank_name = models.CharField(max_length=10)
    def __unicode__(self):
        return self.bank_name

class State(models.Model):			# i have used the state instead of State as proposed by us in the class diagram
    bank = models.ForeignKey(Bank)
    state_name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.state_name


class Branch(models.Model):
    branch = models.ForeignKey(State)
    branch_name = models.CharField(max_length=10)
    ifsc_code = models.CharField(max_length=10)  # i have put it a char if needed we can change it to integer
    def __unicode__(self):
        return self.branch_name


    

# Create your models here.
