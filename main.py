from flask import Flask, render_template, redirect, url_for, request
import quipbot

app = Flask(__name__)


@app.route('/getPrompt')
def getPrompt():
    quipbot.GenerateImage()
    return redirect("static/out.png")
