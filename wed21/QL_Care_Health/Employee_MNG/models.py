from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()  # Lưu ý: Bạn có thể muốn dùng ForeignKey tới bảng User nếu có
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"Employee {self.employee_id}: Specialization - {self.specialization}"

