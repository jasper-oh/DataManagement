from flask import Flask, render_template, request, redirect, send_file
from scrap_stackover import get_jobs as get_stack
from scrap_wework import get_jobs as get_wework
from scrap_remoteok import get_jobs as get_remoteok
from exporter import save_to_file

app = Flask("Reddit-Reader")

db = {}


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/lang_search")
def search_result():
    lang_name = request.args.get("lang_name")
    if lang_name:
        lang_name = lang_name.lower()
        past_search = db.get(lang_name)
        if past_search:
            jobs = db[lang_name]
        else:
            jobs = get_stack(lang_name) + \
                get_wework(lang_name) + get_remoteok(lang_name)
            db[lang_name] = jobs
        result_value = len(jobs)
    else:
        return redirect("/")
    return render_template("result.html", lang_name=lang_name, jobs=jobs, result_value=result_value)


@app.route("/download")
def save_as():
    try:
        lang_name = request.args.get("lang_name")
        if not lang_name:
            raise Exception()
        lang_name = lang_name.lower()
        jobs = db.get(lang_name)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file('jobs.csv')
    except:
        return redirect("/")


app.run(host="0.0.0.0")
