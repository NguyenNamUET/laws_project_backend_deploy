# Generated by Django 3.0.2 on 2020-02-04 15:10
import json
from datetime import datetime
from django.db import migrations

FILE_PATH = 'localdata/documents.json'


def populateExtractiveDocument(apps, schema_editor):
    with open(FILE_PATH, "r") as file:
        extracted_documents = json.load(file)
        ExtractiveDocument = apps.get_model('laws', 'ExtractiveDocument')
        for document in extracted_documents:
            id = document['id']
            url = document['url']
            content = document.get('Toàn văn')
            description = document['Thuộc tính']['Mô tả']
            official_number = document['Thuộc tính']['Số hiệu:']
            signer = document['Thuộc tính']['Người ký:']
            type = document['Thuộc tính']['Loại văn bản:']
            title = document['Thuộc tính']['Loại văn bản:'] + ' ' + document['Thuộc tính']['Số hiệu:']
            organization = document['Thuộc tính']['Nơi ban hành:']
            try:
                issued_date = datetime.strptime(document['Thuộc tính']['Ngày ban hành:'], '%d/%m/%Y').strftime(
                    "%Y-%m-%d")
            except:
                issued_date = None

            expiry_date = None

            try:
                effective_date = datetime.strptime(document['Thuộc tính']['Ngày hiệu lực:'], '%d/%m/%Y').strftime(
                    "%Y-%m-%d")
            except:
                effective_date = None

            try:
                enforced_date = datetime.strptime(document['Thuộc tính']['Ngày công báo:'], '%d/%m/%Y').strftime(
                    "%Y-%m-%d")
            except:
                enforced_date = None

            last_update_time = datetime.now()
            is_over_due = 1

            saved_document = ExtractiveDocument.objects.get_or_create(  id=id,
                                                                        official_number=official_number,
                                                                        title=title,
                                                                        description=description,
                                                                        content=content,
                                                                        signer=signer,
                                                                        type=type,
                                                                        organization=organization,
                                                                        url=url,
                                                                        issued_date=issued_date,
                                                                        expiry_date=expiry_date,
                                                                        effective_date=effective_date,
                                                                        enforced_date=enforced_date,
                                                                        last_update_time=last_update_time,
                                                                        is_over_due=is_over_due)  # return tuple (object, created) created is Boolean
            saved_document[0].save()


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populateExtractiveDocument)
    ]
