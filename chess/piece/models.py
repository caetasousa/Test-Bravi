from django.db import models


class Piece(models.Model):
    color = (
            ('black', 'Black'),
            ('white', 'White'),
        )

    name = models.CharField(max_length=250)
    color = models.CharField(max_length=10, choices=color)

    def __str__(self):
            return self.name
