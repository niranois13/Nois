from django.db import models
from .BaseModel import BaseModel
from .Professional import Professional, ProfessionalAddress
from .Client import Client, ClientAddress


class AppointmentLink(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

class Appointment(BaseModel):
    APPOINTMENT_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('MOD PENDING', 'Modification pending'),
        ('CANCELED', 'Canceled'),
    )
    LOCATION_CHOICES = (
        ('DOMICILE', 'Adresse du client'),
        ('CABINET', 'Adresse du professionel'),
        ('XT', 'Extérieur'),
        #('VISIO', 'Visioconférence'),
    )
    appntmnt_link = models.OneToOneField(
        AppointmentLink,
        on_delete=models.CASCADE,
        related_name='appointment'
        )
    # Vérifier les DateTimeField + est-ce le bon fuseau horaire ?
    appntmnt_datetime_start = models.DateTimeField()
    appntmnt_datetime_end = models.DateTimeField()
    appntmnt_status = models.CharField(
        max_length=50,
        choices=APPOINTMENT_STATUS_CHOICES,
        default="PENDING",
        blank=False,
        null=False
        )
    apppntmnt_location = models.CharField(
        max_length=35,
        choices=LOCATION_CHOICES,
        default="",
        blank=False,
        null=False
        )
    custom_location = models.CharField(max_length=255, blank=True, null=True)
    client_address = models.ForeignKey(
        ClientAddress,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    professional_address = models.ForeignKey(
        ProfessionalAddress,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )

    @property
    def client(self):
        return self.appntmnt_link.client

    @property
    def professional(self):
        return self.appntmnt_link.professional

    def save(self, *args, **kwargs):
        if self.appntmnt_location == 'DOMICILE':
            self.client_address = self.client.address
            self.professional_address = None
        elif self.appntmnt_location == 'CABINET':
            self.professional_address = self.professional.address
            self.client_address = None
        elif self.appntmnt_location == 'XT':
            self.client_address = None
            self.professional_address = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Appointment of {self.appntmnt_link.client} \
            with {self.appntmnt_link.professional}, on \
                {self.appntmnt_datetime_start.strftime('%Y-%m-%d at %H:%M')}"

    class Meta:
        verbose_name="Appointment"
        verbose_name_plural="Appointments"
