from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Jedi(models.Model):
    name = models.CharField(max_length=254)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/jedi/%i" % self.id


class Candidate(models.Model):
    name = models.CharField(max_length=254)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=1)
    email = models.EmailField(max_length=254)
    jedi = models.ForeignKey(Jedi, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/candidate/%i/test" % self.id


class Test(models.Model):
    planet = models.OneToOneField(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return '%s`s test' % self.planet


class Question(models.Model):
    text = models.TextField(max_length=10000)
    answer = models.NullBooleanField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return 'Question for %s' % self.test
