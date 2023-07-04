from flask import Blueprint

app = Blueprint(
    "students",
    __name__,
    template_folder="templates",
)
