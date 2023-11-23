from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)
@app.route('/<username>/<int:post_id>')
def hello_world(username= None, post_id = None):
    return render_template('./index.html', name=username , post_id = post_id)


@app.route('/blog')
def blog():
    return 'this are my thoughts on blog '

@app.route('/blog/2020/dogs')
def dog():
    return 'this are my dogs on blog '