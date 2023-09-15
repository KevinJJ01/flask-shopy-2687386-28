from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username=StringField(label="nombre de usuario",
                        validators=[InputRequired()]
                        )
    password=PasswordField(label="clave",
                           validators=[InputRequired(), Length(8)]
                        )
                           
    submit=SubmitField(label="Iniciar sesion")
