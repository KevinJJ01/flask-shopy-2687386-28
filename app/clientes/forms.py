from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired,NumberRange, Email, Length




class ClientForm():    
    username =  StringField("Ingrese su usuario",validators=[InputRequired(message='usuario requerido')])
    password = PasswordField("Ingrese la contraseña",validators=[InputRequired(message='Contraseña requerida')])
    email =  StringField("Ingrese su correo",validators=[InputRequired(message='correo requerido')])



class NewClientForm(FlaskForm):
    
    username = StringField("Ingrese el usuario: ",
                        validators=[InputRequired()]
                        )
    password = PasswordField("Ingrese la constraseña",
                          validators=[InputRequired(), Length(8)]
                        )
    email = StringField("Ingrese el email: ",
                        validators=[ Email(message="se necesita un @ y su direccion")]
                        )
    submit = SubmitField("Guardar")
    

class EditClientForm(FlaskForm,
                          ClientForm):
        submit = SubmitField("Actualizar")


