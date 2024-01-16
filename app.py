from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from views import views

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Replace with the appropriate port number
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'andreaelpz@gmail.com'
app.config['MAIL_PASSWORD'] = 'xhrb rspo cxwn ffvs'

mail = Mail(app)

app.register_blueprint(views, url_prefix='/')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message("New Contact Form Submission", sender=email, recipients=["andreaelpz@gmail.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        mail.send(msg)

        return jsonify({'success': True, 'message': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)