from flask import Flask, render_template, request
from flask_mail import Mail, Message
from views import views

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Replace with the appropriate port number
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'andreaalpz1016@gmail.com'
app.config['MAIL_PASSWORD'] = 'ontzkuhpwsadbkhi'

mail = Mail(app)

app.register_blueprint(views, url_prefix='/')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message("New Contact Form Submission", sender=email, recipients=["andreaalpz1016@gmail.com"])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    mail.send(msg)

    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)