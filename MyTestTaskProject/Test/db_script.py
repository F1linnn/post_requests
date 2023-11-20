from tinydb import TinyDB, Query

db = TinyDB('db.json')
db.default_table_name = "Form templates"
form_template_1 = {
    "FormName": "MyForm_1_NEPD",
    "f_name": "TYPE_TEXT",
    "f_email": "TYPE_EMAIL",
    "f_phone": "TYPE_PHONE",
    "f_date": "TYPE_DATE"
    
}

form_template_2 = {
    "FormName": "MyForm_2_NEP",
    "f_name": "TYPE_TEXT",
    "f_email": "TYPE_EMAIL",
    "f_phone": "TYPE_PHONE"
}

form_template_3 = {
    "FormName": "MyForm_3_NE",
    "f_name": "TYPE_TEXT",
    "f_email": "TYPE_EMAIL",    
}

form_template_4 = {
    "FormName": "MyForm_4_N",
    "f_name": "TYPE_TEXT",    
}

# Запись шаблона в базу данных
db.insert(form_template_1)
db.insert(form_template_2)
db.insert(form_template_3)
db.insert(form_template_4)





