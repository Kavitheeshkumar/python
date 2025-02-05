from flask import Flask, render_template, request
from form import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template('form.html', form=form)

@app.errorhandler(404)
def not_found(error):
    return "Page Not Found",404

@app.errorhandler(500)
def not_found(error):
    return "Internal Server Error",404

if __name__ == '__main__':
    app.run(debug=True)
