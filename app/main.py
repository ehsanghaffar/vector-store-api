from app.core.bootstrap.app import create_app


app = create_app()

app.get("/")(lambda: "API is up and running!")