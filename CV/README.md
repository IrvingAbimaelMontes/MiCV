# 📄 CV Generator - Generador de Currículum Vitae Profesional

Un generador de CVs moderno y profesional construido con Flask que permite crear, editar y descargar currículums en formato PDF con múltiples plantillas elegantes.

## ✨ Características

- 🎨 **Múltiples Plantillas**: 3 diseños profesionales (Básica, Premium, Moderna)
- 📱 **Diseño Responsive**: Funciona perfectamente en dispositivos móviles y desktop
- 🔐 **Sistema de Autenticación**: Registro e inicio de sesión seguro
- 📄 **Generación de PDF**: Descarga tu CV en formato PDF de alta calidad
- ✏️ **Editor Intuitivo**: Interfaz fácil de usar para crear y editar CVs
- 🎯 **Validación en Tiempo Real**: Validación de formularios con feedback inmediato
- 💳 **Integración con Stripe**: Sistema de pagos para plantillas premium
- 🔒 **Seguridad Avanzada**: Headers de seguridad y protección CSRF

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/cv-generator.git
   cd cv-generator
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   # Crear archivo .env
   echo "SECRET_KEY=tu_clave_secreta_aqui" > .env
   echo "DATABASE_URL=sqlite:///cv_generator.db" >> .env
   echo "STRIPE_PUBLIC_KEY=tu_clave_publica_stripe" >> .env
   echo "STRIPE_SECRET_KEY=tu_clave_secreta_stripe" >> .env
   ```

5. **Inicializar la base de datos**
   ```bash
   python app.py
   ```

6. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

La aplicación estará disponible en `http://localhost:5000`

## 📁 Estructura del Proyecto

```
cv-generator/
├── app/
│   ├── __init__.py          # Inicialización de la aplicación
│   ├── config/              # Configuraciones
│   │   ├── config.py
│   │   ├── security.py
│   │   └── stripe_config.py
│   ├── forms/               # Formularios WTForms
│   │   └── cv_form.py
│   ├── models/              # Modelos de base de datos
│   │   ├── cv_model.py
│   │   ├── user_model.py
│   │   └── payment_model.py
│   ├── routes/              # Rutas de la aplicación
│   │   ├── auth_routes.py
│   │   ├── cv_routes.py
│   │   └── stripe_routes.py
│   ├── services/            # Lógica de negocio
│   │   ├── cv_service.py
│   │   └── payment_service.py
│   ├── static/              # Archivos estáticos
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/           # Plantillas HTML
│   │   ├── layout.html
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   ├── cv_form.html
│   │   ├── view_cv.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── cv_templates.html
│   │   └── templates/       # Plantillas de CV
│   │       ├── basic.html
│   │       ├── premium.html
│   │       └── modern.html
│   ├── utils.py             # Utilidades
│   └── webhooks/            # Webhooks
│       └── stripe_webhook.py
├── migrations/              # Migraciones de base de datos
├── app.py                   # Archivo principal
├── requirements.txt         # Dependencias
└── README.md
```

## 🎨 Plantillas Disponibles

### 1. Básica
- Diseño clásico y profesional
- Ideal para sectores tradicionales
- Colores sobrios y tipografía clara

### 2. Premium
- Diseño elegante con gradientes
- Perfecta para perfiles creativos
- Elementos visuales modernos

### 3. Moderna
- Diseño minimalista y limpio
- Ideal para profesionales tech
- Layout de dos columnas

## 🔧 Configuración

### Variables de Entorno

```bash
# Configuración básica
SECRET_KEY=tu_clave_secreta_super_segura
DATABASE_URL=sqlite:///cv_generator.db
FLASK_ENV=development

# Configuración de Stripe
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Configuración de producción
REDIS_URL=redis://localhost:6379
CORS_ORIGINS=https://tudominio.com
```

### Base de Datos

La aplicación usa SQLAlchemy con soporte para:
- SQLite (desarrollo)
- PostgreSQL (producción)
- MySQL (producción)

## 🚀 Despliegue

### Heroku

1. Crear archivo `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Configurar variables de entorno en Heroku
3. Desplegar:
   ```bash
   git push heroku main
   ```

### Docker

1. Crear `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
   ```

2. Construir y ejecutar:
   ```bash
   docker build -t cv-generator .
   docker run -p 5000:5000 cv-generator
   ```

## 🧪 Testing

```bash
# Ejecutar tests
python -m pytest tests/

# Con cobertura
python -m pytest --cov=app tests/
```

## 📝 API Endpoints

### Autenticación
- `POST /auth/register` - Registro de usuario
- `POST /auth/login` - Inicio de sesión
- `GET /auth/logout` - Cerrar sesión

### CVs
- `GET /cv/create` - Formulario de creación
- `POST /cv/create` - Crear CV
- `GET /cv/<id>` - Ver CV
- `GET /cv/<id>/edit` - Editar CV
- `POST /cv/<id>/edit` - Actualizar CV
- `GET /cv/<id>/download` - Descargar PDF
- `GET /cv/<id>/templates` - Seleccionar plantilla

### Pagos
- `POST /stripe/create-checkout-session` - Crear sesión de pago
- `GET /stripe/success` - Pago exitoso
- `GET /stripe/cancel` - Pago cancelado
- `POST /stripe/webhook` - Webhook de Stripe

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Tu Nombre** - *Desarrollo inicial* - [tu-github](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- Flask por el framework web
- WeasyPrint por la generación de PDFs
- Stripe por el procesamiento de pagos
- Bootstrap por los estilos base

## 📞 Soporte

Si tienes preguntas o necesitas ayuda:

- 📧 Email: soporte@cvgenerator.com
- 🐛 Issues: [GitHub Issues](https://github.com/tu-usuario/cv-generator/issues)
- 📖 Documentación: [Wiki del proyecto](https://github.com/tu-usuario/cv-generator/wiki)

---

⭐ ¡Si te gusta este proyecto, no olvides darle una estrella!
