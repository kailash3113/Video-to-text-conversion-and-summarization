from flask import Flask, render_template,request
import modules
from main import main

app = Flask(__name__)
 
@app.route('/',methods = ['GET','POST'])
def front_end():
    if request.method == 'POST':
        youtubeLink = request.form.get('url')
        process = main(youtubeLink)
        return "The conversion have been successfully completed"

    return render_template('front_end.html')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)    