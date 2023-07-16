<?php
// Retrieve form data
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Set up email headers
$to = "andreael@bu.edu"; 
$subject = "New Contact Form Submission";
$headers = "From: $email" . "\r\n" .
           "Reply-To: $email" . "\r\n" .
           "X-Mailer: PHP/" . phpversion();

// Send email
$mailSent = mail($to, $subject, $message, $headers);

// Check if email sent successfully
if ($mailSent) {
  echo "Email sent successfully!";
} else {
  echo "Failed to send email.";
}
?>
