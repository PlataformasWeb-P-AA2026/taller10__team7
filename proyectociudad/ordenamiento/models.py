from django.db import models

# Create your models here.


class Parroquia(models.Model):
    """ """

    nombre = models.CharField("Nombre de la parroquia", max_length=100)
    ubicacion = models.CharField("Ubicación", max_length=50)  # norte, sur, este, oeste
    tipo = models.CharField("Tipo de parroquia", max_length=50)  # urbana, rural

    def __str__(self):
        return "Parroquia: %s - Ubicación: %s - Tipo: %s" % (
            self.nombre,
            self.ubicacion,
            self.tipo,
        )


class Barrio(models.Model):
    """ """

    nombre = models.CharField("Nombre del barrio", max_length=100)
    num_viviendas = models.IntegerField("Número de viviendas")
    num_parques = models.IntegerField(
        "Número de parques"
    )  # Valores esperados: 1, 2, 3, 4, 5, 6
    num_edificios_residenciales = models.IntegerField(
        "Número de edificios residenciales"
    )

    # Relación: Un barrio pertenece a una parroquia
    parroquia = models.ForeignKey(
        Parroquia, related_name="mis_barrios", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            "Barrio: %s - Viviendas: %d - Parques: %d - Edificios Residenciales: %d"
            % (
                self.nombre,
                self.num_viviendas,
                self.num_parques,
                self.num_edificios_residenciales,
            )
        )


class PresidenteBarrio(models.Model):
    """ """

    cedula = models.CharField("Cédula de identidad", max_length=30, unique=True)
    nickname = models.CharField("Nickname", max_length=50)
    edad = models.IntegerField("Edad")
    profesion = models.CharField("Profesión", max_length=100)

    # Relación: Un presidente lidera un barrio
    barrio = models.ForeignKey(
        Barrio, related_name="mis_presidentes", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Presidente: %s (%s) - Profesión: %s" % (
            self.nickname,
            self.cedula,
            self.profesion,
        )
