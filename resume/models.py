from django.db import models

class Company(models.Model):
    """
    Model representing a company
    """
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return "%s - %s,%s" % (self.name, self.city, self.state)

class Job(models.Model):
    """
    Model representing a single work experience on a resume
    """
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    description = models.TextField(max_length=1000)
    tools = models.ManyToManyField('Tool')
    resume = models.ForeignKey('Resume')

    class Meta:
        ordering = ['-start_date', '-end_date']

    def __str__(self):
        if (self.end_date):
            return "%s at %s (%s - %s)" % (self.title, self.company.name, self.start_date.strftime("%B, %Y"), self.end_date.strftime("%B, %Y"))
        else:
            return "%s at %s (%s - Present)"  % (self.title, self.company.name, self.start_date.strftime("%B, %Y"))

    def get_dates(self):
        if (self.end_date):
            return "%s - %s" % (self.start_date.strftime("%B, %Y"), self.end_date.strftime("%B, %Y"))
        else:
            return "%s - Present"  % (self.start_date.strftime("%B, %Y"))

class Tool(models.Model):
    """
    Model representing a technical skill associated with a Job
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Person(models.Model):
    """
    Model representing a person and their contact information
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Resume(models.Model):
    """
    Model representing a person's resume
    """
    person = models.ForeignKey(Person)
    objective = models.TextField(max_length=3000,blank=True)

    def __str__(self):
        return "Resume for %s" % (self.person)

class Course(models.Model):
    """
    Model representing an academic course
    """
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Education(models.Model):
    """
    Model representing a single school
    """
    HONORS = (
        ('s', 'Summa Cum Laude'),
        ('m', 'Magna Cum Laude'),
        ('c', 'Cum Laude'),
    )

    college_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    honors = models.CharField(choices=HONORS,max_length=1,blank=True)
    gpa = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    classes = models.ManyToManyField(Course)
    resume = models.ForeignKey('Resume')

    class Meta:
        ordering = ['-start_date', '-end_date']

    def get_honors(self):
        if self.honors == "s":
            return "Summa Cum Laude"
        elif self.honors == "m":
            return "Magna Cum Laude"
        else:
            return "Cum Laude"

    def __str__(self):
        if (self.end_date):
            return "%s (%s - %s)" % (self.college_name, self.start_date.strftime("%B, %Y"), self.end_date.strftime("%B, %Y"))
        else:
            return "%s (%s - Present)"  % (self.college_name, self.start_date.strftime("%B, %Y"))
