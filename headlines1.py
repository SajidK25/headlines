from flask import Flask,render_template
import feedparser


app=Flask(__name__)
RSS_FEEDS = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn':'http://rss.cnn.com/rss/edition.rss',
             'fox':'http://feeds.foxnews.com/foxnews/latest',
             'iol':'http://www.iol.co.za/cmlink/1.640'}





@app.route('/')
@app.route('/<publication>')
def get_news(publication='fox'):
    
	feed=feedparser.parse(RSS_FEEDS[publication])
	#first_article=feed['entries'][0]
	articles=feed['entries']
	return render_template('home.html',articles=articles)
	# return '''<html>
	#    <body>
	#     <h1>BBC headlines:</h1>
	#     <i>{0}</i></br>
	#     <b>{1}</b></br>
	#     <p>{2}</p>
	#    </body>
	# </htmL>'''.format(first_article.get("title"),first_article.get("published"),first_article.get("summary"))

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0',port=5005)
