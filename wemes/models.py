from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_num = models.PositiveBigIntegerField()
    last_four = models.IntegerField()
    email = models.CharField(max_length=200, blank=True)
    admin = models.BooleanField(default=False)
    code = models.ImageField(blank=True, upload_to="code")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(f'http://127.0.0.1:8000/users/{self.id}/')
        qr_offset = Image.new('RGB', (350,350), 'white')
        qr_offset.paste(qr_image)
        file_name = f'{self.last_four}-{self.first_name}_{self.last_name}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_num = models.PositiveBigIntegerField()
    last_four = models.IntegerField()
    email = models.CharField(max_length=200, blank=True)
    code = models.ImageField(blank=True, upload_to="code")
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(f'http://127.0.0.1:8000/users/{self.last_four}/')
        qr_offset = Image.new('RGB', (350,350), 'white')
        qr_offset.paste(qr_image)
        file_name = f'{self.last_four}-{self.first_name}_{self.last_name}_qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

class Transaction(models.Model):
    drop_off = models.DateField(blank=True)
    admin = models.ForeignKey(User, related_name='user_admin', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="transactions")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.admin} helped {self.customer}"

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class QRCode(models.Model):
    number = models.IntegerField()
    code = models.ImageField(blank=True, upload_to="code")

    def __str__(self):
        return f"{self.number}"

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(f'http://127.0.0.1:8000/users/{self.number}/')
        qr_offset = Image.new('RGB', (350,350), 'white')
        qr_offset.paste(qr_image)
        file_name = f'item_{self.number}_qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

class Item(models.Model):
    drop_off = models.DateField(blank=True)
    due_date = models.DateField(blank=True)
    is_shoe = models.BooleanField(default=True)
    follow_up = models.BooleanField(default=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, related_name="items")
    qr_code = models.ForeignKey(QRCode, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.drop_off}"