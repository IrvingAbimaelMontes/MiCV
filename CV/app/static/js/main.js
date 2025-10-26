// Funciones principales para mejorar la experiencia del usuario

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips y animaciones
    initializeAnimations();
    initializeFormValidation();
    initializeCharacterCounters();
});

// Animaciones suaves para elementos
function initializeAnimations() {
    // Animar cards al hacer scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observar todas las cards
    document.querySelectorAll('.card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

// Validación en tiempo real de formularios
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea');
        
        inputs.forEach(input => {
            // Validación en tiempo real
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                clearFieldError(this);
            });
        });
        
        // Validación al enviar
        form.addEventListener('submit', function(e) {
            let isValid = true;
            
            inputs.forEach(input => {
                if (!validateField(input)) {
                    isValid = false;
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('Por favor corrige los errores antes de continuar', 'error');
            }
        });
    });
}

// Validar un campo individual
function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    let isValid = true;
    let errorMessage = '';
    
    // Limpiar errores previos
    clearFieldError(field);
    
    // Validaciones específicas
    if (field.hasAttribute('required') && !value) {
        errorMessage = 'Este campo es obligatorio';
        isValid = false;
    } else if (fieldName === 'email' && value && !isValidEmail(value)) {
        errorMessage = 'Ingresa un correo electrónico válido';
        isValid = false;
    } else if (fieldName === 'phone' && value && !isValidPhone(value)) {
        errorMessage = 'Formato de teléfono inválido';
        isValid = false;
    } else if (fieldName === 'full_name' && value && value.length < 2) {
        errorMessage = 'El nombre debe tener al menos 2 caracteres';
        isValid = false;
    }
    
    if (!isValid) {
        showFieldError(field, errorMessage);
    }
    
    return isValid;
}

// Mostrar error en un campo
function showFieldError(field, message) {
    field.classList.add('error');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    errorDiv.style.color = '#dc3545';
    errorDiv.style.fontSize = '0.875rem';
    errorDiv.style.marginTop = '0.25rem';
    
    field.parentNode.appendChild(errorDiv);
}

// Limpiar error de un campo
function clearFieldError(field) {
    field.classList.remove('error');
    const errorDiv = field.parentNode.querySelector('.field-error');
    if (errorDiv) {
        errorDiv.remove();
    }
}

// Validar email
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Validar teléfono
function isValidPhone(phone) {
    const phoneRegex = /^[\+]?[0-9\s\-\(\)]+$/;
    return phoneRegex.test(phone);
}

// Contadores de caracteres
function initializeCharacterCounters() {
    const textareas = document.querySelectorAll('textarea[maxlength]');
    
    textareas.forEach(textarea => {
        const maxLength = textarea.getAttribute('maxlength');
        const counter = document.createElement('div');
        counter.className = 'character-counter';
        counter.style.fontSize = '0.875rem';
        counter.style.color = '#6c757d';
        counter.style.textAlign = 'right';
        counter.style.marginTop = '0.25rem';
        
        textarea.parentNode.appendChild(counter);
        
        function updateCounter() {
            const remaining = maxLength - textarea.value.length;
            counter.textContent = `${textarea.value.length}/${maxLength} caracteres`;
            
            if (remaining < 50) {
                counter.style.color = '#dc3545';
            } else if (remaining < 100) {
                counter.style.color = '#ffc107';
            } else {
                counter.style.color = '#6c757d';
            }
        }
        
        textarea.addEventListener('input', updateCounter);
        updateCounter();
    });
}

// Mostrar notificaciones
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `flash flash-${type}`;
    notification.textContent = message;
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '9999';
    notification.style.maxWidth = '400px';
    notification.style.animation = 'slideIn 0.3s ease';
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Confirmar eliminación
function confirmDelete(message = '¿Estás seguro de que quieres eliminar este elemento?') {
    return confirm(message);
}

// Cargar vista previa de CV
function loadCVPreview(cvId, template) {
    const previewContainer = document.getElementById('cv-preview');
    if (previewContainer) {
        previewContainer.innerHTML = '<div style="text-align: center; padding: 2rem;">Cargando vista previa...</div>';
        
        // Aquí podrías cargar una vista previa del CV
        // Por ahora solo mostramos un mensaje
        setTimeout(() => {
            previewContainer.innerHTML = '<div style="text-align: center; padding: 2rem; color: #666;">Vista previa no disponible en este momento</div>';
        }, 1000);
    }
}

// Efectos de hover para botones
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

// CSS adicional para errores
const style = document.createElement('style');
style.textContent = `
    .form-control.error {
        border-color: #dc3545;
        box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25);
    }
    
    @keyframes slideOut {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100%);
        }
    }
`;
document.head.appendChild(style);
