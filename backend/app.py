from flask import Flask, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import speech_recognition as sr
import transcribe_basics as tr
from threading import Thread
from transcribe_basics import Transcribe
import time
import os


app = Flask(__name__, static_folder='/build', static_url_path='')
CORS(app)


# @app.route("/", methods=["GET", "POST"])
@app.route('/api',  methods=["GET", "POST"])
@cross_origin()
def index():
    transcript = " waiting "
    textfile_path = ""
    if request.method == "POST":
        if "file" not in request.files:
            return {"transcript": "you don't upload file "}

        file = request.files["file"]
        if file.filename == "":
            return {"transcript": "you don't choose file "}

        if file:
            audio_path = f'demo-{time.time_ns()}.wav'
            print(audio_path)
            print("-"*80)
            audio_name = f'demo-{time.time_ns()}'
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)

            with audioFile as source:
                data = recognizer.record(source)

            with open(audio_path, "wb") as f:
                f.write(data.get_wav_data())

            # transcript = tr.Transcribe(audio_path, audio_name)
                transcript = "بلادي، بلادي، بلادي هو النشيد الوطني المصري الحالي، ألّفه محمد يونس القاضي ولحنه سيد درويش، وهو مشتق من كلمات ألقاها مصطفى كامل في إحدى أشهر خطبه عام 1907م"

            # task(audio_path, audio_name)
            # transcript = " the text will be available a soon as possible "
    return({"transcript": transcript})


@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
    # app.run()
