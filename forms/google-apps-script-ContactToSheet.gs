/**
 * Google Apps Script — append contact form rows to your sheet
 *
 * 1. Open your spreadsheet: https://docs.google.com/spreadsheets/d/1RCDondkbaRWYc6WPAl3WIvb808OvgJKHF9gBYgPqnL4
 * 2. Extensions → Apps Script
 * 3. Delete any code, paste this entire file
 * 4. Save (Ctrl+S), then Deploy → New deployment
 *    - Type: Web app
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 5. Copy the Web App URL and paste it into contact.html as CONTACT_SHEET_SCRIPT_URL
 */
var SPREADSHEET_ID = '1RCDondkbaRWYc6WPAl3WIvb808OvgJKHF9gBYgPqnL4';

function doPost(e) {
  try {
    if (!e) {
      return jsonOut({ ok: false, error: 'No event' });
    }

    var name, email, phone, subject, message, page;

    var raw = (e.postData && e.postData.contents) ? String(e.postData.contents).trim() : '';
    // 1) JSON body (fetch with text/plain / application/json)
    if (raw.length > 0 && raw.charAt(0) === '{') {
      var data;
      try {
        data = JSON.parse(raw);
      } catch (parseErr) {
        return jsonOut({ ok: false, error: 'Invalid JSON' });
      }
      name = String(data.name || '').trim();
      email = String(data.email || '').trim();
      phone = String(data.phone || '').trim();
      subject = String(data.subject || '').trim();
      message = String(data.message || '').trim();
      page = String(data._page || data.source_page || '').trim();
    } else {
      // 2) Form POST (hidden iframe) — fields in e.parameter
      var p = e.parameter || {};
      name = String(p.name || '').trim();
      email = String(p.email || '').trim();
      phone = String(p.phone || '').trim();
      subject = String(p.subject || '').trim();
      message = String(p.message || '').trim();
      page = String(p.source_page || p._page || '').trim();
      if (!name && !email && !message) {
        return jsonOut({ ok: false, error: 'No form fields' });
      }
    }

    var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    var sheet = ss.getSheets()[0];
    ensureHeaderRow(sheet);

    sheet.appendRow([
      new Date(),
      name,
      email,
      phone,
      subject,
      message,
      page
    ]);

    return jsonOut({ ok: true });
  } catch (err) {
    return jsonOut({ ok: false, error: String(err) });
  }
}

/** Optional: open this URL in browser after deploy to confirm script runs */
function doGet() {
  return ContentService.createTextOutput('Contact sheet webhook is running. Use POST from your site.')
    .setMimeType(ContentService.MimeType.TEXT);
}

function ensureHeaderRow(sheet) {
  var a1 = sheet.getRange(1, 1).getValue();
  if (a1 === '' || a1 === null) {
    sheet.getRange(1, 1, 1, 7).setValues([[
      'Timestamp', 'Name', 'Email', 'Phone', 'Subject', 'Message', 'Page'
    ]]);
  }
}

function jsonOut(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
