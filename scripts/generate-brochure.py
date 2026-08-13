"""Generate Stephen Mulingwa brochure PDF with positioning, projects, and pricing tiers."""
from pathlib import Path
from fpdf import FPDF

OUT = Path(__file__).resolve().parents[1] / "assets" / "brochure" / "stephen-mulingwa-brochure.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)


class Brochure(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 8, f"stephenmulingwa.com  |  Page {self.page_no()}", align="C")

    def section_title(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(15, 148, 136)
        self.ln(4)
        self.multi_cell(0, 8, text)
        self.set_x(self.l_margin)
        self.set_draw_color(45, 212, 191)
        self.set_line_width(0.4)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(4)

    def body(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(20, 20, 20)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(20, 20, 20)
        self.multi_cell(0, 5.5, f"- {text}")


pdf = Brochure(format="A4")
pdf.set_margins(14, 14, 14)
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()
pdf.set_x(pdf.l_margin)

pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(6, 13, 20)
pdf.multi_cell(0, 10, "Stephen Mulingwa")
pdf.set_x(pdf.l_margin)

pdf.set_font("Helvetica", "", 12)
pdf.set_text_color(15, 148, 136)
pdf.multi_cell(0, 7, "Software Developer  |  Web Developer  |  Data Scientist")
pdf.set_x(pdf.l_margin)
pdf.ln(2)

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(40, 40, 40)
pdf.multi_cell(
    0,
    5.5,
    "Nairobi, Kenya (EAT)  |  Available for Work\n"
    "stephenmulingwa.com  |  mulingwastephen200@gmail.com  |  +254 111 224 952",
)
pdf.set_x(pdf.l_margin)
pdf.ln(4)

pdf.body(
    "I build production web apps, analytics platforms, and AI-powered tools for Kenyan and "
    "international clients - from Next.js operations systems to agri-marketplaces and company websites."
)

pdf.section_title("Featured Projects")
pdf.bullet("Kiki's Mobile Wellness - Next.js PWA for appointments, sales, stock, staff and expenses (kiki-mobile.vercel.app)")
pdf.bullet("TaiStat AgroLink / Mkulima Sokoni - Kenya-first agri marketplace (mkulimasokoni.com)")
pdf.bullet("YodaAI - AI retrospective assistant for agile teams")
pdf.bullet("TaiStat Firm Website - company site for AI and data consultancy (taistat.com)")

pdf.section_title("Technical Toolkit")
pdf.body(
    "Next.js, Python, Neon, Supabase, AWS, Cloudinary, APIs, Vercel, Wialon, Telematics, "
    "Fleet Tracking, Software Development, Web Development, Power BI, SQL, Docker."
)

pdf.section_title("Project Complexity Tiers")
pdf.set_x(pdf.l_margin)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(20, 20, 20)
pdf.multi_cell(0, 6, "Tier 1: Frontend Only / MVP")
pdf.body(
    "Basic responsive landing pages, portfolios, or UI static prototypes built with Next.js/React. "
    "After deployment: 1 month free service and maintenance."
)
pdf.set_x(pdf.l_margin)
pdf.set_font("Helvetica", "B", 11)
pdf.multi_cell(0, 6, "Tier 2: Medium / Interactive Web App")
pdf.body(
    "Dynamic applications with user authentication, database CRUD operations, and dashboard elements. "
    "After deployment: 2 months free service and maintenance."
)
pdf.set_x(pdf.l_margin)
pdf.set_font("Helvetica", "B", 11)
pdf.multi_cell(0, 6, "Tier 3: Full E-Commerce / Advanced App")
pdf.body(
    "Web apps integrated with M-Pesa (Daraja API / Pesapal), custom notifications, calendars, "
    "and complex cloud backends. After deployment: 3 months free service and maintenance."
)

pdf.add_page()
pdf.set_x(pdf.l_margin)
pdf.section_title("Professional Service Breakdown")
pdf.bullet("1. Discovery, UI/UX Design and Wireframing (15%-20%) - mobile-first flows, UI assets, up to 2 design revisions before coding.")
pdf.bullet("2. Frontend and Backend Development (50%-60%) - responsive layouts, cloud DBs (Supabase / MongoDB / Vercel Postgres), JWT or NextAuth.")
pdf.bullet("3. Integrations and Localizations (variable add-on) - M-Pesa Daraja/Pesapal, SMS via Africa's Talking.")
pdf.bullet("4. Deployment, QA and Launch (10%-15%) - Vercel production, custom domains, SEO and performance for local mobile networks.")

pdf.section_title("Kenyan Pricing Nuances")
pdf.bullet("Domain and hosting are billed separately (.co.ke approx. KES 1,000-3,000/year; premium Vercel/DB if required).")
pdf.bullet("Milestone plan: 40% deposit to start design / 40% when core app works / 20% before custom-domain launch.")
pdf.bullet("After the free maintenance window, retainers typically range KES 10,000-30,000 per month.")

pdf.section_title("Training and Software Development")
pdf.body(
    "I also offer hands-on training covering my course tracks (APIs, Power BI, Excel, Python), "
    "software development, web development, and data analysis - with support on real client or academic projects."
)

pdf.section_title("Let's Work Together")
pdf.body(
    "Available for Work | Nairobi, Kenya (East Africa Time)\n"
    "Website: https://stephenmulingwa.com/home\n"
    "Projects: https://stephenmulingwa.com/projects\n"
    "Services: https://stephenmulingwa.com/services\n"
    "Email: mulingwastephen200@gmail.com | WhatsApp: +254 111 224 952"
)

pdf.output(str(OUT))
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
