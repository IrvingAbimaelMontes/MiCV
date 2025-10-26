from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Base de datos inicializada")
        print("🚀 Aplicación iniciada en http://localhost:5000")
    app.run(debug=True)
