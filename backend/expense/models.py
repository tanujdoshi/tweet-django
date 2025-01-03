from django.db import models

class Transactions(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('credit', 'Credit'), ('debit', 'Debit')])
    
    def save(self, *args, **kwargs):
        if self.transaction_type == 'debit':
            self.amount = self.amount * -1
        return super().save()

