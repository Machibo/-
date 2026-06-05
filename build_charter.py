"""
Script to generate the updated Association charter as a .docx file.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Page margins ──────────────────────────────────────────────────────────────
section = doc.sections[0]
section.top_margin    = Inches(1.0)
section.bottom_margin = Inches(1.0)
section.left_margin   = Inches(1.25)
section.right_margin  = Inches(1.25)

# ── Helper functions ──────────────────────────────────────────────────────────
def heading(text, level=1, bold=True):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(12) if level == 1 else Pt(11)
    return p


def body(text, indent=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.left_indent = Inches(0.3)
    run = p.add_run(text)
    run.font.size = Pt(11)
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.size = Pt(11)
    return p


# ══════════════════════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════════════════════
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = title.add_run("EXCERPT FROM THE CHARTER\nAssociation of Business Professionals (EMEA)")
r.bold = True
r.font.size = Pt(13)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1
# ══════════════════════════════════════════════════════════════════════════════
heading("1. Mission, Purpose, and Objectives")

heading("1.1. Mission", level=2)
body(
    "The mission of the Association is to establish, unite, and support a professional "
    "community of highly qualified and internationally recognized individuals whose activities "
    "contribute to the advancement of entrepreneurship, strategic management, international trade, "
    "digital transformation, business innovation, and sustainable economic development within the "
    "EMEA region and globally."
)

heading("1.2. Purpose", level=2)
body(
    "The Association is established as a non-profit professional organization aimed at fostering "
    "collaboration, knowledge exchange, professional excellence, and the promotion of internationally "
    "recognized standards in business leadership and innovation."
)

heading("1.3. Objectives", level=2)
body("To achieve its mission, the Association shall pursue the following objectives:")

objectives = [
    (
        "1.3.1.",
        "To identify and bring together leading professionals in the fields of strategic management, "
        "international trade, supply chain management, product development, corporate governance, and "
        "business innovation whose activities demonstrate significant professional impact."
    ),
    (
        "1.3.2.",
        "To develop and maintain an international professional network comprising executives, "
        "entrepreneurs, innovators, consultants, educators, and other industry leaders engaged in "
        "the advancement of sustainable business practices and modern economic models."
    ),
    (
        "1.3.3.",
        "To promote the professional achievements and contributions of its Members at international "
        "level and to participate in global discussions related to digital transformation, "
        "technology-driven products, platform-based economies, creative industries, and innovation ecosystems."
    ),
    (
        "1.3.4.",
        "To support continuous professional development, encourage adherence to high ethical and quality "
        "standards, and foster responsible and sustainable approaches to digital product development, "
        "financial technologies, corporate innovation, and user-centered design methodologies."
    ),
    (
        "1.3.5.",
        "To contribute to the development and dissemination of best practices in business management, "
        "international cooperation, and innovation leadership."
    ),
]
for num, text in objectives:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.3)
    p.add_run(f"{num} ").bold = True
    p.add_run(text).font.size = Pt(11)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — MEMBERSHIP
# ══════════════════════════════════════════════════════════════════════════════
heading("2. Membership")

# 2.1
heading("2.1. Eligibility", level=2)
body(
    "Membership in the Association shall be open to individuals who meet the professional and "
    "reputational standards established by the Association and who satisfy the criteria defined in "
    "this Charter and in the internal regulations adopted by the Association."
)

# 2.2
heading("2.2. Membership Criteria", level=2)
body("Candidates for membership must demonstrate:")

criteria = [
    (
        "2.2.1.",
        "A high level of professional expertise, leadership experience, strategic competence, and "
        "recognized contributions in the fields of business, international trade, supply chain "
        "management, entrepreneurship, product development, or related disciplines."
    ),
    (
        "2.2.2.",
        "Evidence of international professional recognition, including but not limited to: leadership "
        "roles, significant industry achievements, participation in international projects, advisory "
        "activities, or comparable contributions to the development of business practices."
    ),
    (
        "2.2.3.",
        "Documented professional engagement, which may include publications, academic or industry "
        "articles, media appearances, public speaking engagements, teaching activities, conference "
        "participation, advisory services, or other forms of recognized professional contribution."
    ),
    (
        "2.2.4.",
        "Demonstrable impact on the development of business ecosystems, digital products, innovation "
        "initiatives, strategic transformation programs, or related areas within the EMEA region and internationally."
    ),
]
for num, text in criteria:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.3)
    r1 = p.add_run(f"{num} ")
    r1.bold = True
    r1.font.size = Pt(11)
    r2 = p.add_run(text)
    r2.font.size = Pt(11)

# 2.3
heading("2.3. Admission Procedure", level=2)
body(
    "The procedure for admission, evaluation of candidates, approval of membership, suspension, and "
    "termination of membership shall be governed by internal regulations approved by the competent "
    "governing body of the Association."
)

# 2.4
heading("2.4. Principles of Membership", level=2)
body("The Association shall operate on the basis of the principles of:")
for item in [
    "equality of Members;",
    "transparency in governance;",
    "professional integrity;",
    "ethical conduct;",
    "non-discrimination;",
    "voluntary participation;",
    "compliance with applicable laws and regulations.",
]:
    bullet(item)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# 2.5 — HONORARY (SENIOR) MEMBERS  ← NEW
# ══════════════════════════════════════════════════════════════════════════════
heading("2.5. Honorary (Senior) Members", level=2)

body(
    "The Association may grant Honorary (Senior) Member status to individuals who have demonstrated "
    "outstanding achievements in the field of business and whose professional legacy, influence, or "
    "contribution to the advancement of the business community has been recognized at an international "
    "level. This section governs the conditions, criteria, and procedure for conferring such status."
)

# 2.5.1
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.5.1. Definition. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "An Honorary (Senior) Member is an individual recognized by the Association for exceptional and "
    "sustained contributions to the field of business, including but not limited to: founding or "
    "scaling transformative enterprises, shaping industry standards, advancing international business "
    "cooperation, or mentoring the next generation of business leaders. Honorary (Senior) Member status "
    "is a distinction of honor and does not carry the obligations of regular membership, unless the "
    "individual voluntarily assumes them."
)
r2.font.size = Pt(11)

# 2.5.2
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.5.2. Eligibility Criteria. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "A candidate for Honorary (Senior) Member status must satisfy at least three (3) of the "
    "following criteria:"
)
r2.font.size = Pt(11)

criteria_senior = [
    "(a) has held a senior executive, board, or advisory position in one or more organizations of "
    "international significance for a cumulative period of not less than ten (10) years;",

    "(b) has made a measurable and recognized contribution to the development of a business sector, "
    "market, or professional community at the regional (EMEA) or global level, evidenced by industry "
    "reports, independent assessments, peer recognition, or comparable sources;",

    "(c) has been the recipient of internationally recognized professional honors, awards, fellowships, "
    "or distinctions in the field of business, entrepreneurship, innovation, or economic development;",

    "(d) has authored, co-authored, or substantially contributed to publications, research, frameworks, "
    "or standards that have demonstrably influenced business practices, governance models, or industry "
    "thought leadership;",

    "(e) has served as a mentor, educator, or advocate for emerging business leaders, contributing to "
    "the professional development of others in a sustained and verifiable manner;",

    "(f) has represented the business community in international forums, governmental advisory bodies, "
    "intergovernmental organizations, or multi-stakeholder platforms in a capacity that advanced the "
    "interests of the business profession.",
]
for item in criteria_senior:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.5)
    r = p.add_run(item)
    r.font.size = Pt(11)

# 2.5.3
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.5.3. Nomination and Admission Procedure. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "Candidates for Honorary (Senior) Member status may be nominated by: (i) any two (2) current "
    "Members of the Association; (ii) the President of the Association; or (iii) the Admissions "
    "Committee acting on its own initiative. Nominations must be submitted in writing and accompanied "
    "by a statement of justification addressing the eligibility criteria set out in Section 2.5.2. "
    "The Admissions Committee shall review the nomination in accordance with the procedure described "
    "in Section 2.6 and shall make a recommendation to the governing body of the Association. "
    "The final decision to confer Honorary (Senior) Member status shall be adopted by the governing "
    "body by a simple majority of votes."
)
r2.font.size = Pt(11)

# 2.5.4
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.5.4. Rights and Privileges. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "Honorary (Senior) Members shall be entitled to: use the designation 'Honorary Member' or "
    "'Senior Member' of the Association; participate in Association events, conferences, and "
    "professional activities; receive communications and publications issued by the Association; "
    "and be listed in the official register of Honorary Members maintained by the Association. "
    "Honorary (Senior) Members are exempt from membership fees unless they elect to contribute voluntarily."
)
r2.font.size = Pt(11)

# 2.5.5
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.5.5. Revocation. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "Honorary (Senior) Member status may be revoked by the governing body of the Association in the "
    "event of conduct that is materially inconsistent with the values, principles, or reputation of "
    "the Association, following a review by the Admissions Committee and in accordance with the "
    "procedure set out in Section 2.6."
)
r2.font.size = Pt(11)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# 2.6 — ADMISSIONS COMMITTEE  ← NEW
# ══════════════════════════════════════════════════════════════════════════════
heading("2.6. Admissions Committee", level=2)

body(
    "The Admissions Committee is the standing body of the Association responsible for evaluating "
    "applications and nominations for all categories of membership, including Honorary (Senior) "
    "Members, and for ensuring that admission decisions are made in a fair, consistent, and transparent manner."
)

# 2.6.1
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.6.1. Composition. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "The Admissions Committee shall consist of not fewer than three (3) and not more than seven (7) "
    "members appointed by the governing body of the Association for a term of two (2) years, renewable "
    "once. The Committee shall be chaired by a Chairperson elected from among its members. At least one "
    "member of the Committee shall hold Honorary (Senior) Member status, where such members exist. "
    "Committee members must be in good standing with the Association and must not have a conflict of "
    "interest in respect of any application or nomination under review."
)
r2.font.size = Pt(11)

# 2.6.2
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.6.2. Functions and Powers. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "The Admissions Committee shall: (a) receive and process applications and nominations for "
    "membership; (b) verify that candidates satisfy the applicable eligibility criteria; "
    "(c) conduct due diligence on submitted documentation; (d) issue written recommendations to "
    "the governing body with respect to the admission, deferral, or rejection of each candidate; "
    "(e) maintain a confidential register of all applications reviewed; (f) conduct periodic reviews "
    "of membership criteria and recommend updates to the governing body; and (g) initiate or conduct "
    "reviews in cases of potential revocation of membership or Honorary (Senior) Member status."
)
r2.font.size = Pt(11)

# 2.6.3
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.6.3. Procedure of Meetings. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "The Admissions Committee shall meet as required and not less than four (4) times per year, "
    "whether in person or by electronic means. Meetings shall be convened by the Chairperson or, "
    "in their absence, by any two (2) Committee members. A quorum shall consist of a majority of "
    "the Committee members then in office. Decisions shall be adopted by a simple majority of "
    "members present and voting; in the event of a tie, the Chairperson shall have a casting vote."
)
r2.font.size = Pt(11)

# 2.6.4
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.6.4. Minutes of Meetings. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "Minutes shall be drawn up for each meeting of the Admissions Committee. The minutes shall record: "
    "the date, time, and location (or virtual platform) of the meeting; the names of members present "
    "and absent; the agenda items discussed; a summary of the deliberations; the decisions adopted, "
    "including the outcome of each application or nomination reviewed (approved, deferred, or rejected) "
    "with brief reasons; and any dissenting opinions where a member so requests. Minutes shall be "
    "signed by the Chairperson and the designated Secretary of the meeting, approved at the following "
    "meeting, and kept in the official records of the Association for a minimum of five (5) years. "
    "Copies of minutes shall be made available to the governing body upon request. Personal data "
    "contained in the minutes shall be processed in accordance with applicable data protection laws."
)
r2.font.size = Pt(11)

# 2.6.5
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
r1 = p.add_run("2.6.5. Confidentiality. ")
r1.bold = True
r1.font.size = Pt(11)
r2 = p.add_run(
    "All deliberations of the Admissions Committee and the content of individual applications and "
    "nominations shall be treated as strictly confidential. Committee members shall not disclose "
    "information relating to specific candidates outside the Committee, except as required by the "
    "governing body of the Association or by applicable law."
)
r2.font.size = Pt(11)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# CERTIFICATION
# ══════════════════════════════════════════════════════════════════════════════
heading("Certification", level=2)
body("This excerpt is issued in accordance with the original Charter of the Association.")
body("Date: November 17, 2025")

doc.add_paragraph()

# Signature image
sig_img_para = doc.add_paragraph()
sig_img_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
sig_run = sig_img_para.add_run()
sig_run.add_picture("/workspace/Подпись устав .png", width=Inches(2.2))

# Name and details
sig_name = doc.add_paragraph()
sig_name.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_name = sig_name.add_run("Domenico Liguori")
r_name.bold = True
r_name.font.size = Pt(11)

for line in ["President", "Association of Business Professionals (EMEA)", "info@emeaabp.org"]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(line)
    r.font.size = Pt(11)

# ══════════════════════════════════════════════════════════════════════════════
# Save
# ══════════════════════════════════════════════════════════════════════════════
output_path = "/workspace/Charter_ABP_EMEA_updated.docx"
doc.save(output_path)
print(f"Saved: {output_path}")
