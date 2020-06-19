from flask import Flask
from flask import render_template, request, send_from_directory, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import params
from urllib import parse
import os

app = Flask(__name__)

app.config["DEBUG"] = True


# app.config["DOWNLOAD_PATH"] = os.path.join(os.getcwd(), 'static/tmp'+os.sep+'files')


class SearchForm(FlaskForm):
    search = StringField(label="search", validators=[DataRequired(message="不能为空")])
    submit = SubmitField()


@app.route('/', methods=['GET'])
def index():
    data = request.form.get("search")
    print(data)
    # return render_template("search.html")
    return render_template("index.html")


@app.route('/search', methods=["POST", "GET"])
def search():
    research = request.form.get("search")
    source = request.form.get("source")
    if source == 'netease':
        flag = True
    else:
        flag = False

    results = params.search_result(name=research, flag=flag)
    return render_template("result.html", results=results, result_count=len(results))


@app.route('/download/', methods=["GET", "POST"])
def download():
    req_id = request.args.get("id")
    req_name = request.args.get("name")
    artist = request.args.get("artist")
    path = './static/tmp/'
    filename = req_name + '-' + artist + '.mp3'
    if filename not in os.listdir(path):
        file_url = params.get_target_file_url(str(req_id))
        params.download(url=file_url, file_name=filename)

    response = make_response(send_from_directory(path, filename))
    response.headers["Content-Disposition"] = "attachment; filename={0}; filename*=utf-8''{0}".format(
        parse.quote(filename))
    return response


@app.route('/audio', methods=['GET', 'POST'])
def audio():
    req_id = request.args.get("id")
    req_name = request.args.get("name")
    artist = request.args.get('artist')

    ret = {
        'id': req_id,
        'name': req_name,
        'artist': artist
    }
    path = './static/tmp/'
    filename = req_name + '-' + artist + '.mp3'
    if filename not in os.listdir(path):
        file_url = params.get_target_file_url(str(req_id))
        params.download(url=file_url, file_name=filename)
    # response = make_response(render_template("audio.html", file=path+filename))
    # response.headers["Content-Disposition"] = "attachment; filename={0}; filename*=utf-8''{0}".format(
    #     parse.quote(filename))
    return render_template("audio.html", file=path + filename, result=ret, title=req_name)
    # return response


if __name__ == '__main__':
    app.run()
