from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from ItsAGramLive import ItsAGramLive
import json
from app.utils import fromPickle, toPickle, start_broadcast, stop_broadcast

api = Blueprint('api', __name__)

@api.route('/test')
def home():
    return {'msg':'loll'},200