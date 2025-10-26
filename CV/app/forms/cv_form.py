from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, Regexp

class CVForm(FlaskForm):
    full_name = StringField(
        "Nombre completo", 
        validators=[
            DataRequired(message="El nombre completo es obligatorio"),
            Length(min=2, max=100, message="El nombre debe tener entre 2 y 100 caracteres")
        ],
        render_kw={"placeholder": "Tu nombre completo"}
    )
    
    email = StringField(
        "Correo electrónico", 
        validators=[
            DataRequired(message="El correo electrónico es obligatorio"),
            Email(message="Ingresa un correo electrónico válido"),
            Length(max=120, message="El correo no puede exceder 120 caracteres")
        ],
        render_kw={"placeholder": "tu.email@ejemplo.com"}
    )
    
    phone = StringField(
        "Teléfono", 
        validators=[
            Optional(),
            Length(max=20, message="El teléfono no puede exceder 20 caracteres"),
            Regexp(r'^[\+]?[0-9\s\-\(\)]+$', message="Formato de teléfono inválido")
        ],
        render_kw={"placeholder": "+34 123 456 789"}
    )
    
    address = StringField(
        "Dirección", 
        validators=[
            Optional(),
            Length(max=200, message="La dirección no puede exceder 200 caracteres")
        ],
        render_kw={"placeholder": "Ciudad, País"}
    )
    
    summary = TextAreaField(
        "Resumen profesional", 
        validators=[
            Optional(),
            Length(max=1000, message="El resumen no puede exceder 1000 caracteres")
        ],
        render_kw={
            "placeholder": "Breve descripción de tu perfil profesional y objetivos...",
            "rows": 4
        }
    )
    
    education = TextAreaField(
        "Formación académica", 
        validators=[
            Optional(),
            Length(max=2000, message="La educación no puede exceder 2000 caracteres")
        ],
        render_kw={
            "placeholder": "• Licenciatura en Ingeniería Informática - Universidad XYZ (2018-2022)\n• Certificación en Desarrollo Web - Instituto ABC (2023)",
            "rows": 6
        }
    )
    
    experience = TextAreaField(
        "Experiencia laboral", 
        validators=[
            Optional(),
            Length(max=3000, message="La experiencia no puede exceder 3000 caracteres")
        ],
        render_kw={
            "placeholder": "• Desarrollador Full Stack - Empresa XYZ (2022-2024)\n  - Desarrollo de aplicaciones web con React y Node.js\n  - Gestión de bases de datos MySQL",
            "rows": 8
        }
    )
    
    skills = TextAreaField(
        "Habilidades y competencias", 
        validators=[
            Optional(),
            Length(max=1000, message="Las habilidades no pueden exceder 1000 caracteres")
        ],
        render_kw={
            "placeholder": "• Python, JavaScript, React\n• Inglés avanzado\n• Trabajo en equipo",
            "rows": 6
        }
    )
    
    submit = SubmitField("Guardar CV", render_kw={"class": "btn"})
