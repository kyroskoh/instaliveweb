from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from ItsAGramLive import ItsAGramLive
import json
from app.utils import fromPickle, toPickle, start_broadcast, stop_broadcast, get_viewers

api = Blueprint('api', __name__)

@api.route('/live/viewers')
def home():
    viewers = get_viewers()
    return {
        'count':len(viewers),
        'list_users':viewers
        },200