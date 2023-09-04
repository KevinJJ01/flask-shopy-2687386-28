from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired,NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed


class NewProductForm(FlaskForm):
    
    nombre = StringField("Ingrese nombre producto: ",
                        validators=[InputRequired()]
                        )
    precio = IntegerField("Ingrese precio del producto",
                          validators=[
                              InputRequired(
                                "Precio requerido"),

                              NumberRange(
                                  message="Precio fuera de rango",
                                  min = 1000,
                                  max = 100000
                              )
                          ])
    imagen = FileField(label="Imagen del producto",
                       validators=[
                           FileRequired(
                               message="Se necesita una imagen para continuar"
                           ),
                           FileAllowed(
                               ["jpg", "png", "jpge"],
                               message="solo se aceptan imagenes"
                           )

                       ])
    submit = SubmitField("Guardar")
    