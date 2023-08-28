from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese nombre producto")
    precio = IntegerField("Ingrese precio del producto")
    submit = SubmitField("Guardar")
    