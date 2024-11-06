from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Please fill out all fields', 'error')
        return redirect(url_for('contact'))

    print(f"Contact Form Submission\nName: {name}\nEmail: {email}\nMessage: {message}")
    flash('Thank you for your message! We will get back to you shortly.', 'success')
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
