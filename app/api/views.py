from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from InstaLiveCLI import InstaLiveCLI
import json
from app.utils import start_broadcast, stop_broadcast, get_viewers

api = Blueprint('api', __name__)

@api.route('/live/viewers')
def home():
    viewers = get_viewers()
    return {
        'count':len(viewers),
        'list_viewers':viewers
        },200