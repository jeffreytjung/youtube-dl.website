from flask import Flask, render_template, request, send_file
from pytube import YouTube
from os.path import basename

app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome to the index page."

@app.route('/form')
def form():
    return render_template('form.html')

@app.route("/submit", methods=['POST'])
def my_form_post():

	#****************************************
	#****for testing passing form data****

	#test = request.values['url']
	#url = test.upper()

	#return url

	#****************************************

	url = request.values['url']

	#****************************************
	#****this will download the file but it goes to the directory where the python file is located****

	#my_video = YouTube(url)
	#stream = my_video.streams.first()
        #stream.download()

	#****************************************
	local_download_path = YouTube(url).streams[0].download("static")
	video_filename = basename(local_download_path)
	return render_template('download.html', video_filename = video_filename)
	

	#**************************************
	#****for testing that pytube would take the input of a url and make some kind of output****

	#return my_video.title

	#**************************************


	#*******************************************
	#****this part of the code is what will make the program download the file and then open a download dialogue right away****

	#fname = local_download_path.split("//")[-1]
	#return send_file(fname,as_attachment=True)

	#*******************************************
if __name__ == "__main__":
	app.run(debug=True)
