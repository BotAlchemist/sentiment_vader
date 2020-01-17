from flask import Flask, render_template, request, url_for, redirect
from nltk.sentiment.vader import SentimentIntensityAnalyzer

vader = SentimentIntensityAnalyzer()



app= Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST'])
def result():
    raw_text= [str(x) for x in request.form.values()]
    text= [raw_text]

    sentiment_result= vader.polarity_scores(text[0][0])

    return render_template('home.html', sentiment_text= text[0][0],
                           sentiment_result= sentiment_result)




if __name__ == '__main__':
    app.run(debug=True)
