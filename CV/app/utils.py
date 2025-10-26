from jinja2 import Environment, FileSystemLoader
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO

def generate_pdf(cv, template_name="basic"):
    """
    Genera un PDF del CV usando reportlab
    
    Args:
        cv: Objeto CV con los datos
        template_name: Nombre de la plantilla ('basic', 'premium', 'modern')
    
    Returns:
        bytes: Contenido del PDF generado
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=1  # Centrado
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor='#2c3e50'
    )
    
    # Contenido del PDF
    story = []
    
    # Título
    story.append(Paragraph(cv.full_name, title_style))
    story.append(Spacer(1, 12))
    
    # Información de contacto
    contact_info = f"<b>Email:</b> {cv.email}"
    if cv.phone:
        contact_info += f"<br/><b>Teléfono:</b> {cv.phone}"
    if cv.address:
        contact_info += f"<br/><b>Dirección:</b> {cv.address}"
    story.append(Paragraph(contact_info, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Resumen profesional
    if cv.summary:
        story.append(Paragraph("Resumen Profesional", heading_style))
        story.append(Paragraph(cv.summary.replace('\n', '<br/>'), styles['Normal']))
        story.append(Spacer(1, 20))
    
    # Educación
    if cv.education:
        story.append(Paragraph("Formación Académica", heading_style))
        story.append(Paragraph(cv.education.replace('\n', '<br/>'), styles['Normal']))
        story.append(Spacer(1, 20))
    
    # Experiencia
    if cv.experience:
        story.append(Paragraph("Experiencia Laboral", heading_style))
        story.append(Paragraph(cv.experience.replace('\n', '<br/>'), styles['Normal']))
        story.append(Spacer(1, 20))
    
    # Habilidades
    if cv.skills:
        story.append(Paragraph("Habilidades", heading_style))
        story.append(Paragraph(cv.skills.replace('\n', '<br/>'), styles['Normal']))
    
    # Generar PDF
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

def get_available_templates():
    """Retorna la lista de plantillas disponibles"""
    return [
        {"name": "basic", "display_name": "Básica", "description": "Diseño clásico y profesional"},
        {"name": "premium", "display_name": "Premium", "description": "Diseño elegante con gradientes"},
        {"name": "modern", "display_name": "Moderno", "description": "Diseño minimalista y moderno"}
    ]
