

# !!!!!!!!!!!!!!!!!!!!!!   ПЕРЕД ЗАПУСКОМ УСТАНОВИТЕ ЗАВИСИМОСТИ ИЗ ФАЙЛА requirements.txt
# !!!!!!!!!!!!!!!!!!!!!!   КОМАНДА ДЛЯ УСТАНОВКИ pip install -r requirements.txt

# --------------------------- НЕ ИЗМЕНЯТЬ ------------------------------------------------------
UTF8 = 'UTF-8'                                                                                #-
# --------------------------- НЕ ИЗМЕНЯТЬ ------------------------------------------------------

FILENAME = '21694.xlsx' # указываем имя файла выгруженного с расширением 
OUT_FILENAME_XML = '21694.xml' # указываем желаемое имя файла  в формате XML 


# ENCODING Принамает значение UTF8 или None
ENCODING = UTF8

# Атрибуты тегов можно
DATA_TYPE = 'data_type'
INT = 'int'
N = 'n'
Y = 'y'
VARCHAR255 = 'varchar(255)'
NULABLE = 'nullable'
DATE = 'date'

# Базовый ТЕГ
BASE_TAG = 'root'
# вспомогательный тег, в котором заключены данные
SUBBASE_TAG ='row'


# Шаблон, основан на словарях тройной вложенности.
#{  в первом словаре в качестве ключа передается поле из файла БД например: REG_TYPE_CODE
#    { во втором словаре в  качестве ключа передается ТЕГ из шаблона xml  например: att_attachType_id
#        { в третьем словаре передаются атрибуты  тегов  }
#    }
#}
# Можно сделать несколько шаблонов в одном файле, для использования необходимого шаблона
# установите ему имя TEMP_XML остальные можете закоментировать выделив их и нажав на ctrl+ /
# Запуск программы осуществялется командой python main.py \

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
