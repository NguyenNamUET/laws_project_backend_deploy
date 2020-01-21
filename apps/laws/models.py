from django.db import models


# Create your models here.
class DocumentMetaDataTerm(models.Model):
    term_id = models.BigIntegerField(20, primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    last_update_time = models.DateTimeField()  # Ngày cập nhật meta văn bản (editor)


class ExtractiveDocument(models.Model):
    id = models.BigAutoField(20, primary_key=True, unique=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    description = models.TextField(blank=True, null=True)
    signer = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=225, blank=True, null=True)
    url = models.CharField(max_length=255)
    issued_date = models.DateField(blank=True, null=True) #Ngày ban hành
    expiry_date = models.DateField(blank=True, null=True) #Ngày hết hiệu lực
    effective_date = models.DateField(blank=True, null=True) #Ngày có hiệu lực
    enforced_date = models.DateField(blank=True, null=True) #Ngày đăng công báo
    last_update_time = models.DateTimeField(blank=True, null=True) #Ngày cập nhật văn bản (crawler)
    is_over_due = models.PositiveSmallIntegerField(1, blank=True, null=True)


class ExtractiveDocumentMetaData(models.Model):
    meta_id = models.BigIntegerField(20, primary_key=True, unique=True)
    term_value = models.CharField(max_length=1500)
    last_update_time = models.DateTimeField()  # Ngày cập nhật metadata của văn bản (crawler)
    extractive_document_id = models.ForeignKey(ExtractiveDocument, on_delete=models.CASCADE)
    term_id = models.ForeignKey(DocumentMetaDataTerm, on_delete=models.CASCADE)


class RelationType(models.Model):
    id = models.BigAutoField(20, primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(blank=True, null=True)  # Ngày cập nhật liên hệ của văn bản (crawler)


class ExtractiveDocumentSchema(models.Model):
    source_id = models.ForeignKey(ExtractiveDocument, on_delete=models.CASCADE, related_name="extractive_document_source")
    destination_id = models.ForeignKey(ExtractiveDocument, on_delete=models.CASCADE, related_name="extractive_document_destination")
    relation_type_id = models.ForeignKey(RelationType, on_delete=models.CASCADE)
    last_update_time = models.DateTimeField()  # Ngày cập nhật schema của văn bản (crawler)

    class Meta:
        unique_together = (("source_id", "destination_id"),)


class SelfDraftedDocument(models.Model):
    id = models.BigIntegerField(20, primary_key=True, unique=True)
    title = models.CharField(max_length=45)
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_time = models.DateTimeField() #Ngày soạn thảo văn bản
    last_update_time = models.DateTimeField()  # Ngày cập nhật văn bản (editor)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)


class SelfDraftedDocumentMetaData(models.Model):
    meta_id = models.BigIntegerField(20, primary_key=True, unique=True)
    term_value = models.CharField(max_length=1500)
    last_update_time = models.DateTimeField()  # Ngày cập nhật meta văn bản (editor)
    self_drafted_document_id = models.ForeignKey(SelfDraftedDocument, on_delete=models.CASCADE)
    term_id = models.ForeignKey(DocumentMetaDataTerm, on_delete=models.CASCADE)

