# forms.py
 
from wtforms import Form, StringField, SelectField
 
class MusicSearchForm(Form):
    search = StringField('')

class NameForm(Form):
    name = StringField('')
