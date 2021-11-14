from django.db import models

# Create your models here.
#car_title
# city
# state
# color
# model
# year
# condition
# price
# description
# car_photo_1
# car_photo_2
# car_photo_3
# car_photo_4
# car_photo_5
# features
# body_style
# engine
# transmission
# interior
# mileage
# fuel_type
# no_of_owners
# created_date

class Car(models.Model):
    state_choices = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    car_title = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    car_photo = models.CharField(max_length=255)
    car_photo_1 = models.CharField(max_length=255)
    car_photo_2 = models.CharField(max_length=255)
    car_photo_3 = models.CharField(max_length=255)
    car_photo_4 = models.CharField(max_length=255)
    car_photo_5 = models.CharField(max_length=255)
    features = models.CharField(max_length=255)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    mileage = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255)
    no_of_owners = models.CharField(max_length=255)
    is_feature = models.CharField(max_length=255)
    created_date = models.CharField(max_length=255)
    


