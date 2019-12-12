# from django.db import models


# STATUS_CHOICES = (
#     ("Received", "Received"),
#     ("Started", "Started"),
#     ("Abandoned", "Abandoned"),
#     ("Finished", "Finished"),
# )

# PAYMENT_CHOICES = (
#     ('C', 'CASH'),
# )


# # TODO: User field additions


# class TimeStampedModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


# class Order(TimeStampedModel):
#     transaction_id = models.CharField(max_length=100)
#     store = models.ForeignKey(Store, on_delete=models.CASCADE)
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     shipping_address = models.TextField()
#     payment_type = models.CharField(max_length=1, choices=PAYMENT_CHOICES)

#     def __str__(self):
#         # TODO: return relevant string made with store and order count
#         return self.id

#     def get_total(self):
#         # TODO: return relevant data
#         return 0


# class OrderItem(TimeStampedModel):
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     amount = models.FloatField()

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"


# class OrderStatus(TimeStampedModel):
#     status = models.CharField(choices=STATUS_CHOICES, max_length=100)

#     def __str__(self):
#         return f"{self.status}"
