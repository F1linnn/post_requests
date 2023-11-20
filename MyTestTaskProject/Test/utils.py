import re

def find_matching_template(form_data, form_templates):
    print(form_data)
    for template in form_templates:
        template_fields = list(template.keys())[1:]

        if all(field in form_data.keys() for field in template_fields):
            for field in template_fields:
                if template[field] != validate_value(form_data[field]):
                    return None
            return template
    return None

#curl -X POST -d "f_name=John&f_email=john@example.com&f_phone=%2B71234567890&f_date=24.07.2023&sometext=TEXTFORTEXT" http://localhost:8000/get_form/
def validate_value(field_value):
    date_pattern_1 = re.compile(r'^(?:(?:31(\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')
    date_pattern_2 = re.compile(r'(((19|20)([2468][048]|[13579][26]|0[48])|2000)[-]02[-]29|((19|20)[0-9]{2}[-](0[4678]|1[02])[-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[-](0[1359]|11)[-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[-]02[-](0[1-9]|1[0-9]|2[0-8])))')
    phone_pattern = re.compile(r'^\+7\d{10}$')
    email_pattern = re.compile(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$')
    if date_pattern_1.match(field_value) or date_pattern_2.match(field_value):
        return "TYPE_DATE"
    elif phone_pattern.match(field_value):
        return "TYPE_PHONE"
    elif email_pattern.match(field_value):
        return "TYPE_EMAIL"
    else:
        return "TYPE_TEXT"


def get_types_form(user_form):
    for key in user_form.keys():
        user_form[key] = validate_value(user_form[key])
    return user_form