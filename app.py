from flask import Flask, request, render_template
import stories

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/madlibs")
def madlib():
    s = request.args.get("story")

    return render_template("form.html", story = s.title(), endpoint= s.split(' ')[0])

@app.route("/story/places")
def storyOne():
    req = request.args
    place = req.get("placeName")
    noun = req.get("nounName")
    verb = req.get("verbName")
    adj = req.get("adjName")
    plural = req.get("pluralName")

    ans = {"place": place, "noun": noun, "verb": verb, "adjective":adj, "plural_noun": plural}
    
    s = stories.places

    return render_template("story.html", story= s.generate(ans))

@app.route("/story/summer")
def storyTwo():
    req = request.args
    place = req.get("placeName")
    noun = req.get("nounName")
    verb = req.get("verbName")
    adj = req.get("adjName")
    plural = req.get("pluralName")

    ans = {"place": place, "noun": noun, "verb": verb, "adjective":adj, "plural_noun": plural}
    
    s = stories.summer

    return render_template("story.html", story= s.generate(ans))

@app.route("/story/once")
def storyThree():
    req = request.args
    place = req.get("placeName")
    noun = req.get("nounName")
    verb = req.get("verbName")
    adj = req.get("adjName")
    plural = req.get("pluralName")

    ans = {"place": place, "noun": noun, "verb": verb, "adjective":adj, "plural_noun": plural}
    
    s = stories.story

    return render_template("story.html", story= s.generate(ans))
