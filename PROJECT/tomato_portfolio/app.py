from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key')

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

# Verify email configuration
logger.debug(f"Mail server: {app.config['MAIL_SERVER']}")
logger.debug(f"Mail port: {app.config['MAIL_PORT']}")
logger.debug(f"Mail username: {app.config['MAIL_USERNAME']}")
logger.debug(f"Mail password set: {'Yes' if app.config['MAIL_PASSWORD'] else 'No'}")

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))
        
        try:
            # Create email message
            msg = Message(
                subject=f'New Contact Form Submission from {name}',
                recipients=[os.getenv('MAIL_USERNAME')],  # Your email address
                body=f'''
                Name: {name}
                Email: {email}
                Message: {message}
                '''
            )
            
            # Send email
            logger.debug("Attempting to send email...")
            mail.send(msg)
            logger.debug("Email sent successfully!")
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}", exc_info=True)
            flash(f'An error occurred while sending your message: {str(e)}', 'error')
            return redirect(url_for('contact'))
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)  # gunicorn will handle binding/host

