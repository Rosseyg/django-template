from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# create member model with user as foreign key
class Stylist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add additional fields
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add additional fields
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # add list of past donations
    def past_donations(self):
        return self.donations.filter(donation_date__lte=timezone.now()).order_by('donation_date')
    def __str__(self):
        return self.user.username

#create a donation model with 3 types of donations
class Donation(models.Model):
    # add additional fields
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='donations')
    donation_amount = models.IntegerField(default=0)
    donation_date = models.DateTimeField(auto_now_add=True)
    donation_type = models.CharField(max_length=30, blank=True)
    
    # publish donation
    def publish(self):
        self.donation_date = timezone.now()
        self.save()
    
    # return title of donation
    def __str__(self):
        return self.donation_type
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return str(self.name)
    
class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()
    status = models.CharField(max_length=50, choices=(
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ))
    class Meta:
        verbose_name_plural = 'Appointments'

    def __str__(self):
            return f"{self.member}'s {self.service} appointment with {self.stylist}"

# create post model with member as foreign key
class Post(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    # add additional fields
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    # publish post
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    # return title of post
    def __str__(self):
        return self.title
