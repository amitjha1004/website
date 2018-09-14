# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models

class invoice(models.Model):

    pkey=models.IntegerField
    date=models.IntegerField
    invoice_number=models.IntegerField
    total_quantity = models.IntegerField
    total_amount = models.IntegerField
    total_tax = models.IntegerField
    # emp_id = models.IntegerField(primary_key=True)


    def __str__(self):
        return self.pkey


