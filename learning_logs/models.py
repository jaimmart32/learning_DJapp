#Django utiliza un ORM (Mapeador Objeto-Relacional) para interactuar con la base de datos 
# de una manera orientada a objetos, lo que significa que puedes definir modelos como clases 
# de Python y Django se encargará de convertir esos modelos en tablas en la base de datos.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Un tema sobre el que esta aprendiendo el usuario."""

    # Cada atributo de la clase representa un campo de la tabla en la base de datos. 
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Este método es útil para proporcionar una representación legible y significativa de 
    # un objeto cuando se utiliza en contextos donde se espera una cadena de texto.
    def __str__(self):
        """Devuelve una representación del modelo como string."""
        return self.text

class Entry(models.Model):
    """Algo específico aprendido sobre un tema."""

    # clave que asocia entradas con temas en la DB, elimina en cascada las entradas si se borra el tema asociado.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        if len(self.text) <= 50:
            return self.text
        return f"{self.text[:50]}..."