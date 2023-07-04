from django.db import models


# Create your models here.
# class Language(models.Model):
#     language_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.language_id

class Translation(models.Model):
    translation_id = models.AutoField(primary_key=True)
    # source_lang = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='source_translations')
    # target_lang = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='target_translations')
    source_lang = models.CharField(max_length=10)
    target_lang = models.CharField(max_length=10)
    translation_model = models.CharField(max_length=100)
    translation_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"Translation ID: {self.translation_id}"
