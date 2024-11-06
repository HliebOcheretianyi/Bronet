from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session/flash messaging


@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')


@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """Handles contact form submission."""
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Simple validation (you can expand this)
    if not name or not email or not message:
        flash('Please fill out all fields', 'error')
        return redirect(url_for('home'))

    # In a real app, you would save this data to a database or send an email
    print(f"Contact Form Submission\nName: {name}\nEmail: {email}\nMessage: {message}")

    # Flash a success message and redirect to the home page
    flash('Thank you for your message! We will get back to you shortly.', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)