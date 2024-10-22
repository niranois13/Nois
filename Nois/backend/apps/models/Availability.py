from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from .BaseModel import BaseModel
from .Professional import Professional

class Availability(BaseModel):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='availabilities'
        )
    availability_start_datetime = models.DateTimeField()
    availability_end_datetime = models.DateTimeField()
    availability_title = models.CharField(
        max_length=25
    )
    minimum_duration = models.DurationField(default=timedelta(hours=1))
    maximum_duration = models.DurationField(null=True, blank=True)

    def clean(self):
        if self.availability_start_datetime >= self.availability_end_datetime:
            raise ValidationError("End time must be after start time")
        if self.maximum_duration and \
            self.maximum_duration < self.minimum_duration:
            raise ValidationError(
                "Maximum duration must be greater than minimum duration"
                )

    def __str__(self):
        return f"Availability of \
            {self.professional} \
                on {self.start_time.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name="Availability"
        verbose_name_plural="Availabilities"
