## Реализовано для конвератции файлов конвертации файлов .xslx в xml

##### Для установки клонируйте репозиторий комадой
```
git clone git@github.com:WayBro-54/convert_xml.git
```
##### Саздайте виртуальное окружение и установите зависимости
```
python -m venv venv
pip install -r requirements.txt
```

##### Описание констант: 
* BASE_TAG -> КорневойSUBBASE_TAG тег, в который заключаются данные.
* SUBBASE_TAG -> второй по значимости тег. Является родительским тегом для данных
* TEMP_XML -> Шаблон, где связываются поля выгрузки из .xlsx файла с тегом .xml <br/>
TEMP_XML состоит из 3 вложенных словарей 
```
{  в первом словаре в качестве ключа передается поле из файла БД например: REG_TYPE_CODE
    { во втором словаре в  качестве ключа передается ТЕГ из шаблона xml  например: att_attachType_id
        { в третьем словаре передаются атрибуты  тегов  }
    }
}
```

Пример TMP_XML <br/>
```
TEMP_XML = {
    'ID': {
        'att_client_id':{DATA_TYPE: INT, NULABLE: N}
    },
    'REG_TYPE_CODE': {
        'att_attachType_id':{DATA_TYPE: INT, NULABLE: N}
    },
    'REG_TYPE_NAME': {
        'att_attachType_Title':{DATA_TYPE: VARCHAR255, NULABLE: N}
    },
    'LPU_REG': {
        'att_LPU_CODE':{DATA_TYPE: INT, NULABLE: INT}
    },
    'DIVISION': {
        'att_orgStructure_Title':{DATA_TYPE: VARCHAR255, NULABLE: Y}
    },
    'DIV_CODE': {
        'att_orgStructure_CODE':{DATA_TYPE: INT, NULABLE: Y}
    },
    'BEGIN_DATE': {
        'att_begDate':{DATA_TYPE: DATE, NULABLE: N}
    },
    'END_DATE': {
        'att_endDate':{DATA_TYPE: DATE, NULABLE: Y}
    },
    'LPU_REG_ALLNAME': {
        'att_LPU_Title':{DATA_TYPE: VARCHAR255, NULABLE: Y}
    },
}
```

