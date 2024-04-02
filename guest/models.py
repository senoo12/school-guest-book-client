from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings

key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Create your models here.
class Guest(models.Model):
    K = 'Kepala Sekolah'
    G = 'Guru'
    T = 'TU'
    S = 'Siswa'

    kategori_dituju = (
        (K, K),
        (G, G),
        (T, T),
        (S, S),
    )

    P = 'Pria'
    W = 'Wanita'

    jenis_kelamin = (
        (P, P),
        (W, W),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=10, choices=jenis_kelamin, default=P) 
    kategori_dituju = models.CharField(max_length= 20, choices=kategori_dituju, default=S)
    pihak_dituju = models.CharField(max_length=100)
    keperluan = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=34)
    foto = models.ImageField(max_length=100, null=True, default=False, upload_to='media/%Y/%m/%d/')

    def save(self, *args, **kwargs):
        self.no_hp = cipher_suite.encrypt(self.no_hp.encode()).decode()
        super().save(*args, **kwargs)

    def decrypted_data(self):
        return cipher_suite.decrypt(self.no_hp.encode()).decode()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "guest"