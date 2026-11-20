from flask import Blueprint, jsonify
import os

api = Blueprint("api", __name__)

@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "AWS ECS Fargate Deployment",
        "application": "Flask REST API",
        "status": "running"
    }), 200

@api.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@api.route("/version", methods=["GET"])
def version():
    return jsonify({
        "version": os.getenv("APP_VERSION", "1.0.0")
    }), 200
    