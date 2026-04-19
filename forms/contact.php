<?php
  /**
  * Requires the "PHP Email Form" library
  * The "PHP Email Form" library is available only in the pro version of the template
  * The library should be uploaded to: vendor/php-email-form/php-email-form.php
  * For more info and help: https://bootstrapmade.com/php-email-form/
  *
  * ── Google Sheet vs this file ─────────────────────────────────────────────
  * The live contact page (../contact.html) does NOT post to this script. It sends
  * submissions to Google Apps Script (see CONTACT_SHEET_SCRIPT_URL in contact.html
  * and google-apps-script-ContactToSheet.gs). Changing $receiving_email_address
  * below does NOT add or remove rows in your sheet.
  *
  * This PHP file only runs if a form's action points to forms/contact.php.
  *
  * ── Receiving address (Gmail or your host) ─────────────────────────────────
  * Many hosts deliver Gmail reliably but fail or drop mail to custom domains unless
  * you configure SMTP (uncomment $contact->smtp below with your provider's settings).
  */

  $receiving_email_address = 'mulingwastephen200@gmail.com';

  if( file_exists($php_email_form = '../assets/vendor/php-email-form/php-email-form.php' )) {
    include( $php_email_form );
  } else {
    die( 'Unable to load the "PHP Email Form" Library!');
  }

  $contact = new PHP_Email_Form;
  $contact->ajax = true;
  
  $contact->to = $receiving_email_address;
  $contact->from_name = $_POST['name'];
  $contact->from_email = $_POST['email'];
  $contact->subject = $_POST['subject'];

  // Uncomment below code if you want to use SMTP to send emails. You need to enter your correct SMTP credentials
  /*
  $contact->smtp = array(
    'host' => 'example.com',
    'username' => 'example',
    'password' => 'pass',
    'port' => '587'
  );
  */

  $contact->add_message( $_POST['name'], 'From');
  $contact->add_message( $_POST['email'], 'Email');
  $contact->add_message( $_POST['message'], 'Message', 10);

  echo $contact->send();
?>
