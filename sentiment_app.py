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
    negative_value = round(sentiment_result['neg']*100,2)
    neutral_value = round(sentiment_result['neu']*100,2)
    positive_value = round(sentiment_result['pos']*100,2)
    compound_value = sentiment_result['compound']*100
    if compound_value >= 0.05:
        overall_value= "Positive"
    elif compound_value <= -0.05:
        overall_value= "Negative"
    else:
        overall_value= "Neutral"

    return render_template('home.html', sentiment_text= text[0][0],
                           sentiment_result= sentiment_result,
                           negative_value= negative_value,
                           neutral_value= neutral_value,
                           positive_value= positive_value,
                           compound_value= abs(round(compound_value,2)),
                           overall_value=overall_value
                           )




if __name__ == '__main__':
    app.run(debug=True)
