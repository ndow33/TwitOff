from flask import Blueprint, request, jsonify, render_template
from sklearn.linear_model import LogisticRegression 
from web_app.models import User, Tweet
from web_app.services.basilica_services import connection as basilica_api_client

stats_routes = Blueprint("stats_routes", __name__) # what does this do?

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE....")
    print("FORM DATA: ", dict(request.form)) # what does this do?

    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]
    
    print("----------------------------------------")
    print("FETCHING TWEETS FROM THE DATABASE")
    user_a = User.query.filter_by(screen_name = screen_name_a).one() # what does .one() do?
    user_b = User.query.filter_by(screen_name = screen_name_b).one()
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets
    print("USER A ", user_a.screen_name, len(user_a.tweets))
    print("USER B ", user_b.screen_name, len(user_b.tweets))
    
    print("-------------------------------------------")
    print("TRAINING THE MODEL")
    embeddings = [] # an empty list that will be filled with numeric embeddings of the tweets
    labels = [] # an empty list that will be filled with who tweeted those embedded tweets
    for tweet in user_a_tweets:
        labels.append(user_a.screen_name) # what does this do?
        embeddings.append(tweet.embedding) # what does this do? Which package is it from?
    
    for tweet in user_b_tweets:
        labels.append(user_b.screen_name)
        embeddings.append(tweet.embedding)
    
    classifier = LogisticRegression()
    classifier.fit(embeddings, labels) # embeddings = x values, labels = y values
    
    print("-----------------------------------------")
    print("MAKING A PREDICTION")

    example_embedding = basilica_api_client.embed_sentence(tweet_text, model="twitter")
    result = classifier.predict([example_embedding])
    

    return render_template("prediction_results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely= result[0]
        )
