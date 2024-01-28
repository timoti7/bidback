from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Kategori Adı"))

    class Meta:
        verbose_name = _("Kategori")
        verbose_name_plural = _("Kategoriler")

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name=_("Üst Kategori"))
    name = models.CharField(max_length=100, verbose_name=_("Alt Kategori Adı"))

    class Meta:
        verbose_name = _("Alt Kategori")
        verbose_name_plural = _("Alt Kategoriler")

    def __str__(self):
        return self.name

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', verbose_name=_("Alt Kategori"))
    name = models.CharField(max_length=100, verbose_name=_("Ürün Adı"))
    start_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Başlangıç Fiyatı"))
    start_time = models.DateTimeField(verbose_name=_("Başlangıç Zamanı"))
    end_time = models.DateTimeField(verbose_name=_("Bitiş Zamanı"))

    class Meta:
        verbose_name = _("Ürün")
        verbose_name_plural = _("Ürünler")

    def __str__(self):
        return self.name

class RealEstate(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='real_estate', verbose_name=_("Ürün"))
    location = models.CharField(max_length=255, verbose_name=_("Konum"))

    class Meta:
        verbose_name = _("Emlak")
        verbose_name_plural = _("Emlaklar")

    def __str__(self):
        return self.product.name

class Vehicle(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='automobile', verbose_name=_("Ürün"))
    make = models.CharField(max_length=100, verbose_name=_("Marka"))
    model = models.CharField(max_length=100, verbose_name=_("Model"))

    class Meta:
        verbose_name = _("Araç")
        verbose_name_plural = _("Araçlar")

    def __str__(self):
        return self.product.name

class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Ürün"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Kullanıcı"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Teklif Miktarı"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Teklif Zamanı"))

    class Meta:
        verbose_name = _("Teklif")
        verbose_name_plural = _("Teklifler")

    def __str__(self):
        return f"{self.product.name} - {self.amount}"
