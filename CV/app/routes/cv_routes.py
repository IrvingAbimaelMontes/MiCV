from flask import Blueprint, render_template, redirect, url_for, flash, request, send_file
from app import db
from app.models.cv_model import CV
from app.forms.cv_form import CVForm
from app.utils import generate_pdf, get_available_templates
import io

cv_bp = Blueprint("cv", __name__)

@cv_bp.route("/")
def mi_cv():
    """Mostrar el CV actual"""
    cv = CV.query.first()  # Solo habrá un CV
    return render_template("mi_cv.html", cv=cv)

@cv_bp.route("/modificar", methods=["GET", "POST"])
def modificar_cv():
    """Crear o modificar el CV"""
    cv = CV.query.first()
    form = CVForm()
    
    if form.validate_on_submit():
        if cv:
            # Actualizar CV existente
            cv.full_name = form.full_name.data
            cv.email = form.email.data
            cv.phone = form.phone.data
            cv.address = form.address.data
            cv.summary = form.summary.data
            cv.education = form.education.data
            cv.experience = form.experience.data
            cv.skills = form.skills.data
            db.session.commit()
            flash("CV actualizado exitosamente", "success")
        else:
            # Crear nuevo CV
            cv = CV(
                full_name=form.full_name.data,
                email=form.email.data,
                phone=form.phone.data,
                address=form.address.data,
                summary=form.summary.data,
                education=form.education.data,
                experience=form.experience.data,
                skills=form.skills.data
            )
            db.session.add(cv)
            db.session.commit()
            flash("CV creado exitosamente", "success")
        
        return redirect(url_for("cv.mi_cv"))
    
    # Si hay un CV existente, cargar los datos en el formulario
    if cv:
        form.full_name.data = cv.full_name
        form.email.data = cv.email
        form.phone.data = cv.phone
        form.address.data = cv.address
        form.summary.data = cv.summary
        form.education.data = cv.education
        form.experience.data = cv.experience
        form.skills.data = cv.skills
    
    return render_template("modificar_cv.html", form=form, cv=cv)

@cv_bp.route("/exportar")
def exportar_pdf():
    """Exportar CV a PDF"""
    cv = CV.query.first()
    if not cv:
        flash("No hay CV para exportar. Crea uno primero.", "error")
        return redirect(url_for("cv.mi_cv"))
    
    template_name = request.args.get('template', 'basic')
    pdf_file = generate_pdf(cv, template_name)
    return send_file(
        io.BytesIO(pdf_file),
        mimetype='application/pdf',
        download_name=f"{cv.full_name}_CV_{template_name}.pdf"
    )

@cv_bp.route("/plantillas")
def plantillas():
    """Mostrar plantillas disponibles para exportar"""
    cv = CV.query.first()
    if not cv:
        flash("No hay CV para exportar. Crea uno primero.", "error")
        return redirect(url_for("cv.mi_cv"))
    
    templates = get_available_templates()
    return render_template("plantillas.html", cv=cv, templates=templates)