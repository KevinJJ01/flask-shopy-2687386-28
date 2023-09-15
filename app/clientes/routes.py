from flask import render_template, flash,redirect
from flask_login import login_required
from app.clientes import clientes
import app
import os
from .forms import NewClientForm, EditClientForm

@clientes.route('/createCliente',methods=['GET','POST'])
@login_required
def crear():
    p = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/clientes/listarC')
    return render_template('new.html',
                           form=form)


@clientes.route('/listarC')
@login_required
def listar():
     ## seleccionar los profuctos
    clientes = app.models.Cliente.query.all()
    return render_template("listC.html", 
                            clientes = clientes)  
 
@clientes.route('/editar/<cliente_id>',methods=['GET','POST'])
@login_required
def editar (cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('cliente actualizado')
        return redirect('/clientes/listarC')
    return render_template('new.html',
                           form=form)

@clientes.route('/eliminar/<cliente_id>')
@login_required
def eliminar (cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('cliente eliminado')
    return redirect('/clientes/listarC')


