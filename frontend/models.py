from django.db import models


class Sex(models.TextChoices):
    MALE = "male"
    FEMALE = "female"


class Person(models.Model):
    name = models.CharField(max_length=80)
    sex = models.TextField(choices=Sex.choices)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if hasattr(other, "id"):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.name) * hash(self.sex) + self.pk * hash("random")



class Male(Person):
    def save(self, *args, **kwargs):
        self.sex = Sex.MALE
        super(Male, self).save(*args, **kwargs)


class Female(Person):
    def save(self, *args, **kwargs):
        self.sex = Sex.FEMALE
        super(Female, self).save(*args, **kwargs)


class MatchState(models.TextChoices):
    UNKNOWN = "unknown"
    NO_MATCH = "no match"
    PERFECT_MATCH = "perfect match"


class BaseMatch(models.Model):
    male = models.ForeignKey(to=Male, on_delete=models.PROTECT)
    female = models.ForeignKey(to=Female, on_delete=models.PROTECT)
    match_state = models.TextField(choices=MatchState.choices)


class PerfectMatch(BaseMatch):
    def save(self, *args, **kwargs):
        self.match_state = MatchState.PERFECT_MATCH
        super(PerfectMatch, self).save(*args, **kwargs)


class NoMatch(BaseMatch):
    def save(self, *args, **kwargs):
        self.match_state = MatchState.NO_MATCH
        super(NoMatch, self).save(*args, **kwargs)
