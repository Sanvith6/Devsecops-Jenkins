import os
from datetime import datetime, timezone

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["APP_NAME"] = os.getenv("APP_NAME", "starter-app")
    app.config["APP_ENV"] = os.getenv("APP_ENV", "dev")
    app.config["APP_VERSION"] = os.getenv("APP_VERSION", "1.0.0")
    app.config["LOG_LEVEL"] = os.getenv("LOG_LEVEL", "INFO")

    @app.get("/")
    def index():
        return jsonify(
            {
                "message": "Starter app is running.",
                "name": app.config["APP_NAME"],
                "environment": app.config["APP_ENV"],
            }
        )

    @app.get("/health")
    def health():
        return jsonify(
            {
                "status": "ok",
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "version": app.config["APP_VERSION"],
            }
        )

    @app.get("/ready")
    def ready():
        return jsonify({"ready": True})

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
