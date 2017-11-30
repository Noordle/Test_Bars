from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=254)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.DateField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/candidate/%i" % self.id


class Jedi(models.Model):
    name = models.CharField(max_length=254)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/jedi/%i" % self.id


class Questions(models.Model):
    text = models.TextField(max_length=255)
    answer = models.BooleanField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)



class Test(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)


