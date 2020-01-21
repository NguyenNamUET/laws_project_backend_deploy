# Generated by Django 3.0.2 on 2020-01-17 04:21

# Generated by Django 3.0.2 on 2020-01-17 02:49

import pandas as pd
from django.db import migrations
import ast
from os import listdir
from os.path import isfile, join
from datetime import datetime


CSV_FILE_PATH = "localdata/data.csv"
RAW_TEXT_DIRECTORY_PATH = "localdata/data/"
RAW_TEXT_PATH_LIST = [f for f in listdir(RAW_TEXT_DIRECTORY_PATH) if isfile(join(RAW_TEXT_DIRECTORY_PATH, f))]



def str_to_dict(str):
    try:
        dict = ast.literal_eval(str)
        return dict
    except:
        return None


df = pd.read_csv(CSV_FILE_PATH)
url_list = [field for field in df['url'].tolist()]
tenvb_list = [field for field in df['Tên VB'].tolist()]
toanvan_list = [field for field in df['Toàn văn'].tolist()]
luocdo_list = [str_to_dict(field) for field in df["Lược đồ"].tolist()]
thuoctinh_list = [str_to_dict(field) for field in df["Thuộc tính"].tolist()]


def populate_extractive_document(apps, schema_editor):
    ExtractiveDocument = apps.get_model('laws', 'ExtractiveDocument')

    for index, file in enumerate(df["Toàn văn"].tolist()):
        if file in RAW_TEXT_PATH_LIST:
            title = tenvb_list[index]
            url = url_list[index]
            content = open(RAW_TEXT_DIRECTORY_PATH + toanvan_list[index], 'r').read()
            if thuoctinh_list[index] is not None:
                description = thuoctinh_list[index]['Thông tin'][0]
                law_type = thuoctinh_list[index]['Loại văn bản'][0]
                if len(thuoctinh_list[index]['Cơ quan ban hành/ Chức danh / Người ký']) == 3:
                    organization = thuoctinh_list[index]['Cơ quan ban hành/ Chức danh / Người ký'][0]
                else:
                    organization = None

                try:
                    enforced_date = datetime.strptime(thuoctinh_list[index]['Ngày đăng công báo'][0],'%d/%m/%Y').strftime("%Y-%m-%d")
                except:
                    enforced_date = None

                try:
                    expiry_date = datetime.strptime(thuoctinh_list[index]['Ngày hết hiệu lực'][0],'%d/%m/%Y').strftime("%Y-%m-%d")
                except:
                    expiry_date = None

                try:
                    effective_date = datetime.strptime(thuoctinh_list[index]['Ngày có hiệu lực'][0],'%d/%m/%Y').strftime("%Y-%m-%d")
                except:
                    effective_date = None

                try:
                    issued_date = datetime.strptime(thuoctinh_list[index]['Ngày ban hành'][0],'%d/%m/%Y').strftime("%Y-%m-%d")
                except:
                    issued_date = None

                if len(thuoctinh_list[index]['Cơ quan ban hành/ Chức danh / Người ký']) == 3:
                    signer = thuoctinh_list[index]['Cơ quan ban hành/ Chức danh / Người ký'][-1]
                else:
                    signer = None

                if thuoctinh_list[index]['Thông tin'][1].lower().find("còn") > 0:
                    is_over_due = 0
                else:
                    is_over_due = 1

                document = ExtractiveDocument.objects.get_or_create(title=title,
                                                                    description=description,
                                                                    content=content,
                                                                    signer=signer,
                                                                    type=law_type,
                                                                    organization=organization,
                                                                    url=url,
                                                                    issued_date=issued_date,
                                                                    expiry_date=expiry_date,
                                                                    effective_date=effective_date,
                                                                    enforced_date=enforced_date,
                                                                    is_over_due=is_over_due) #return tuple (object, created) created is Boolean
                document[0].save()

            else:
                document = ExtractiveDocument.objects.get_or_create(title=title, url=url, content=content)
                document[0].save()


def populate_relation_type(apps, schema_editor):
    RelationType = apps.get_model('laws', 'RelationType')
    luocdo_field_list = [ld for ld in luocdo_list[0].keys() if ld is not None]
    for field in luocdo_field_list:
        relation = RelationType.objects.get_or_create(name=field)
        relation[0].save()


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_extractive_document),
    ]

