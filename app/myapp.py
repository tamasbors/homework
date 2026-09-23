import os
from threading import Lock

from flask import Flask, jsonify, request

app = Flask(__name__)
config_store = {}
config_lock = Lock()

@app.get("/health")
def health():
  return jsonify(status="ok")

@app.get("/version")
def version():
  return jsonify(version="1.0.0")

@app.get("/env")
def environment():
  return jsonify(environment=os.getenv("ENVIRONMENT", ""))

@app.post("/config")
def create_config():
  payload = request.get_json(silent=True)
  if not isinstance(payload, dict) or not isinstance(payload.get("name"), str) or not isinstance(payload.get("value"), str):
    return jsonify(error="name and value are required strings"), 400

  name = payload["name"]
  value = payload["value"]
  with config_lock:
    config_store[name] = value
  return jsonify(name=name, value=value)

@app.get("/config/<name>")
def get_config(name):
  with config_lock:
      value = config_store.get(name)
  if value is None:
      return jsonify(error="configuration not found"), 404
  return jsonify(name=name, value=value)

@app.delete("/config/<name>")
def delete_config(name):
  with config_lock:
      deleted = config_store.pop(name, None) is not None
  return jsonify(deleted=deleted)

if __name__ == "__main__":
  port = int(os.getenv("PORT", "8080"))
  app.run(host="0.0.0.0", port=port)