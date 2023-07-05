from flask import Flask,jsonify,render_template


app = Flask(__name__)

Channels = {
"Kurzgesagt" : "UCsXVk37bltHxD1rDPwtNM8Q",
"T-series" : "UCq-Fj5jknLsUf-MWSy4_brA",
"BBC" : "UCN7B-QD0Qgn2boVH5Q0pOWg"
}


import requests
@app.route('/')
def index():

    url = "https://youtube138.p.rapidapi.com/channel/videos/"

    querystring = {"id":Channels['T-series'],"hl":"en","gl":"US"}

    headers = {
        "X-RapidAPI-Key": "598bb9d4bemsh676064900aa37a0p119a20jsn7e1ac956a96d",
        "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data=response.json()
    content=data['contents']
    video=[videos['video'] for videos in content if videos['video']['publishedTimeText']]
   
    return render_template('YT_clone.html',video=video)


@app.template_filter()
def image(thumbnails):
    return thumbnails[3]['url'] if len(thumbnails)>=4 else thumbnails[0]['url']


app.run(host='0.0.0.0',port=81)