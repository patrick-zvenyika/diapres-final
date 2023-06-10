from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EarlyDiagnosisPatient(models.Model):
    name = models.CharField(max_length=40)
    id_number = models.CharField(max_length=19)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    age = models.IntegerField(max_length=4)
    gender = models.CharField(max_length=7)
    polyuria = models.CharField(max_length=5)
    polydipsia = models.CharField(max_length=5)
    sudden_weight_loss = models.CharField(max_length=5)
    weakness = models.CharField(max_length=5)
    polyphagia = models.CharField(max_length=5)
    genital_thrush = models.CharField(max_length=5)
    visual_blurring = models.CharField(max_length=5)
    itching = models.CharField(max_length=5)
    irritability = models.CharField(max_length=5)
    delayed_healing = models.CharField(max_length=5)
    partial_paresis = models.CharField(max_length=5)
    muscle_stiffness = models.CharField(max_length=5)
    alopecia = models.CharField(max_length=5)
    obesity = models.CharField(max_length=5)
    height = models.CharField(max_length=7)
    mass = models.CharField(max_length=7)
    status = models.CharField(max_length=10, default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class PatientData(models.Model):
    name = models.CharField(max_length=40)
    id_number = models.CharField(max_length=17, null=False)
    sex = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    pregnancies = models.IntegerField(max_length=2)
    glucose_level = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    BMI = models.FloatField()
    Diabetes_Pedigree_Function = models.FloatField()
    age = models.IntegerField(max_length=3)
    height = models.FloatField()
    mass = models.FloatField()
    status = models.CharField(max_length=10, default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class ChatMessage(models.Model):
    msg_sender = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    msg_receiver = models.ForeignKey(User, null=False, on_delete = models.CASCADE, related_name = 'receiver' )
    body = models.TextField(null=True)
    pdf = models.FileField( upload_to='media',blank=True)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.body 