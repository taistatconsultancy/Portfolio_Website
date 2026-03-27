/**
 * Contact form -> Google Sheets webhook
 *
 * Target workbook name: Clienteles
 * Target tab name: Clients
 *
 * IMPORTANT:
 * 1) In Apps Script, set SPREADSHEET_ID below to your Clienteles file ID.
 * 2) Deploy as Web app:
 *    - Execute as: Me
 *    - Who has access: Anyone
 */

const SPREADSHEET_ID = '1dLK1eLhgxF4BzZm2_llZoKDKpBgC1ILzhsCLAk24mbM';
const SHEET_NAME = 'Clients';

function doGet() {
  return ContentService
    .createTextOutput('Contact sheet webhook is running.')
    .setMimeType(ContentService.MimeType.TEXT);
}

function doPost(e) {
  try {
    var payload = e && e.parameter ? e.parameter : {};
    var name = (payload.name || '').toString().trim();
    var email = (payload.email || '').toString().trim();
    var phone = (payload.phone || '').toString().trim();
    var subject = (payload.subject || '').toString().trim();
    var message = (payload.message || '').toString().trim();

    var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    var sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);

    // Create header row once.
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Timestamp', 'Name', 'Email', 'Phone', 'Subject', 'Message']);
    }

    sheet.appendRow([new Date(), name, email, phone, subject, message]);

    return ContentService
      .createTextOutput('OK')
      .setMimeType(ContentService.MimeType.TEXT);
  } catch (err) {
    return ContentService
      .createTextOutput('ERROR: ' + err.message)
      .setMimeType(ContentService.MimeType.TEXT);
  }
}
