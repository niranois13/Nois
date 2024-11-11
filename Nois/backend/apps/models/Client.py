from django.db import models
from .Address import Address
from django.contrib.auth import get_user_model
from .UserManager import User

User = get_user_model()

class Client(User):
    is_helper = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class ClientAddress(Address):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        related_name='address_of_client'
        )

    def __str__(self):
        return f"Address of {self.client.first_name} {self.client.last_name}"
