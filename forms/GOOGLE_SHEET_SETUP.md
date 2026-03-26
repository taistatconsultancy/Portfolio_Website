# Connect `contact.html` to your Google Sheet

A normal website **cannot** write to Google Sheets by URL alone. You add a tiny **Google Apps Script** “web app” that receives the form and appends a row to your sheet.

Your sheet ID is already set in `google-apps-script-ContactToSheet.gs`.

## Steps (one-time)

1. Open your spreadsheet:  
   [Clients sheet](https://docs.google.com/spreadsheets/d/1RCDondkbaRWYc6WPAl3WIvb808OvgJKHF9gBYgPqnL4/edit)

2. Menu: **Extensions → Apps Script**

3. Remove the default `myFunction` code. Copy **all** contents of  
   `forms/google-apps-script-ContactToSheet.gs`  
   into the Apps Script editor and **Save** (floppy icon or Ctrl+S).

4. Click **Deploy → New deployment**

   - Click the gear ⚙️ next to “Select type” → **Web app**
   - **Execute as:** Me (`your@gmail.com`)
   - **Who has access:** **Anyone** — must be exactly **Anyone**, *not* “Anyone with Google account”  
     If you pick the wrong option, visitors never hit your script (you may see a **Google sign-in** page when opening the `/exec` URL in the browser).

5. Click **Deploy**, authorize when asked, then **Copy** the **Web App URL**  
   (looks like `https://script.google.com/macros/s/AKfycb.../exec`)

6. In **`contact.html`**, find:

   ```js
   const CONTACT_SHEET_SCRIPT_URL = '';
   ```

   Paste your URL between the quotes, save, and upload the site again.

## Sheet columns

If row 1 is empty, the script adds headers:

| Timestamp | Name | Email | Phone | Subject | Message | Page |

## Notes

- **“Anyone can edit”** on the sheet is separate from the form: the form talks only to the **web app URL**. Keep that URL in your HTML; you don’t need to expose edit links.
- If you change the script later, use **Deploy → Manage deployments → Edit (pencil) → Version: New version → Deploy** so the live URL updates.

## Test

1. In a **private/incognito** window, open your Web App URL (`…/exec`).  
   - **Good:** plain text like `Contact sheet webhook is running…`  
   - **Bad:** Google **Sign in** → fix **Who has access** → **Deploy** again (**New version**).
2. Submit the contact form on your site, then refresh the sheet—you should see a new row.

## Submissions not appearing?

- **Update the script:** Copy the latest `google-apps-script-ContactToSheet.gs` into Apps Script, then **Deploy → Manage deployments → Edit → New version → Deploy**.
- **Access:** Web app must be **Execute as: Me** and **Who has access: Anyone**.
- **Same spreadsheet:** The script uses the sheet with ID in `SPREADSHEET_ID`—must be your “Clients” file.
