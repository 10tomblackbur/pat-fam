import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from datetime import datetime

app = Flask(__name__)

# Configure app.  API KEY is in different file
app.config["SESSION_PERMANENT"] = False
app.config["SECRET_KEY"] = 'Jo2KSnTytTpG7I5s'





