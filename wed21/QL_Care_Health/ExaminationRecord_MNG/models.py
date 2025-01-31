from django.db import models
from Veterinarian_MNG.models import Veterinarian
from Pet_MNG.models import Pet
# Create your models here.
class ExaminationRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    date = models.DateTimeField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    stay_required = models.BooleanField(default=False)

    # Thêm trường đánh giá
    rating = models.IntegerField(null=True, blank=True)  # Đánh giá sao từ 1 đến 5
    comment = models.TextField(null=True, blank=True)  # Bình luận từ khách hàng

    def __str__(self):
        return f"{self.pet.name} - {self.veterinarian.name} - {self.date}"