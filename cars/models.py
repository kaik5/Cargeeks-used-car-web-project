from django.db import models
from datetime import MAXYEAR, datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField


# Create your models here.
class Car(models.Model):
    state_choice  = (
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

    features_choices = (
        
        ('Navigation System', 'Navigation System'),
        ('Audio', 'Audio'),
        ('Airbags', 'Airbags'),
        ('AC', 'AC'),
        ('Heated Seats', 'Heated Seats'),
        ('Seat Massage', 'Seat Massage'),
        ('Alarm System', 'Alarm System'),
        ('Parking Assist', 'Parking Assist'),
        ('Power Steering', 'Power Steering'),
        ('Backup Camera', 'Backup Camera'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Bluetooth', 'Bluetooth'),
        ('Keyless Entry', 'Keyless Entry'),
        ('Electric Charging', 'Electric Charging'),
        ('Leather Seats', 'Leather Seats'),
        
    )
    
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    
    year_choice = [];
    for r in range (2000, (datetime.now().year + 1)):
        year_choice.append((r, r));
    
    car_title = models.CharField(max_length = 255);
    state = models.CharField(choices = state_choice, max_length= 100);
    city = models.CharField(max_length = 100);
    color = models.CharField(max_length = 100);
    model = models.CharField(max_length = 100);
    year = models.IntegerField(('year'), choices = year_choice);
    condition = models.CharField(max_length = 100);
    price = models.IntegerField();
    description = RichTextField();
    photo = models.ImageField(upload_to = "photos/%d/%m/%Y", blank = True);
    photo1 = models.ImageField(upload_to = "photos/%d/%m/%Y", blank = True);
    photo2 = models.ImageField(upload_to = "photos/%d/%m/%Y", blank = True);
    photo3 = models.ImageField(upload_to = "photos/%d/%m/%Y", blank = True);
    photo4 = models.ImageField(upload_to = "photos/%d/%m/%Y", blank = True);
    features = MultiSelectField(choices=features_choices);
    body_stlye = models.CharField(max_length = 100);
    engine = models.CharField(max_length = 100);
    transmission = models.CharField(max_length = 100);
    interior = models.CharField(max_length = 100);
    mileage = models.IntegerField();
    doors = models.CharField(choices= door_choices, max_length=10);
    vin_number = models.CharField(max_length = 50);
    fuel_type = models.CharField(max_length = 50);
    number_of_owners = models.CharField(max_length = 100);
    is_featured = models.BooleanField(default = False);
    created_date = models.DateTimeField(default=datetime.now, blank = True);
    
    
    
    
    def __str__(self):
        return self.car_title;
    
    
    

