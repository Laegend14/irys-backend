from flask import Flask, request, jsonify
import snscrape.modules.twitter as sntwitter

app = Flask(__name__)

@app.route("/count", methods=["GET"])
def count_mentions():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username required"}), 400

    query = f"from:{username} @irys_xyz"
    count = 0
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        count += 1
        if i > 1000:  # stop after 1000 tweets for safety
            break

    return jsonify({"username": username, "count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
