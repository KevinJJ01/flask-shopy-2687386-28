from flask import render_template
from app.productos import productos
import app
import os
from .forms import NewProductForm

@productos.route('/create',methods=['GET','POST'])
def crear():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        ##guardar el producto en base de datos 
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        ##subir imagen a carpeta images
        ##campo de image(filestorage)
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() + "/app/productos/images/" + p.imagen))
        return "producto registrado "
    return render_template('new.html',
                           form=form)

@productos.route('/update')
def actualizar():
    return 'aqui vamos a actualizar productos '

@productos.route('/delete')
def eliminar():
    return 'aqui vamos a eliminar productos '