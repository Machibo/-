"""
Generates Charter_ABP_EMEA_updated.docx
- Single document, font 10.5pt throughout
- Full detailed §2.5 (Honorary/Senior Members) and §2.6 (Admissions Committee)
- Certification block kept together so it never starts a page alone
"""

from docx import Document
from docx.shared import Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FS = 10.5   # base font size
FS_H1 = 11  # section heading
FS_H2 = 10.5  # sub-heading

doc = Document()

# ── Margins ────────────────────────────────────────────────────────────────────
s = doc.sections[0]
s.top_margin    = Cm(2.5)
s.bottom_margin = Cm(2.5)
s.left_margin   = Cm(3.0)
s.right_margin  = Cm(2.0)

# ── Helpers ───────────────────────────────────────────────────────────────────
def sp(p, before=0, after=4, line=14):
    fmt = p.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after  = Pt(after)
    fmt.line_spacing = Pt(line)


def keep(p):
    pPr = p._p.get_or_add_pPr()
    for tag in ('w:keepLines', 'w:keepNext'):
        el = OxmlElement(tag)
        pPr.append(el)


def H1(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(FS_H1)
    sp(p, before=6, after=3, line=14)
    return p


def H2(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(FS_H2)
    sp(p, before=4, after=2, line=14)
    return p


def body(text, indent=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.left_indent = Inches(0.3)
    r = p.add_run(text)
    r.font.size = Pt(FS)
    sp(p)
    return p


def clause(num, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.3)
    r1 = p.add_run(num + " ")
    r1.bold = True
    r1.font.size = Pt(FS)
    r2 = p.add_run(text)
    r2.font.size = Pt(FS)
    sp(p)
    return p


def inline(label, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r1 = p.add_run(label + " ")
    r1.bold = True
    r1.font.size = Pt(FS)
    r2 = p.add_run(text)
    r2.font.size = Pt(FS)
    sp(p)
    return p


def bul(text):
    p = doc.add_paragraph(style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p.add_run(text)
    r.font.size = Pt(FS)
    sp(p, before=0, after=2, line=14)
    return p


def subitem(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.45)
    r = p.add_run(text)
    r.font.size = Pt(FS)
    sp(p, before=0, after=2, line=14)
    return p


# ══════════════════════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════════════════════
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
rt = title.add_run("EXCERPT FROM THE CHARTER\nAssociation of Business Professionals (EMEA)")
rt.bold = True
rt.font.size = Pt(13)
sp(title, before=0, after=8, line=16)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1
# ══════════════════════════════════════════════════════════════════════════════
H1("1. Mission, Purpose, and Objectives")

H2("1.1. Mission")
body("The mission of the Association is to establish, unite, and support a professional "
     "community of highly qualified and internationally recognized individuals whose activities "
     "contribute to the advancement of entrepreneurship, strategic management, international trade, "
     "digital transformation, business innovation, and sustainable economic development within the "
     "EMEA region and globally.")

H2("1.2. Purpose")
body("The Association is established as a non-profit professional organization aimed at fostering "
     "collaboration, knowledge exchange, professional excellence, and the promotion of internationally "
     "recognized standards in business leadership and innovation.")

H2("1.3. Objectives")
body("To achieve its mission, the Association shall pursue the following objectives:")

for num, text in [
    ("1.3.1.", "To identify and bring together leading professionals in the fields of strategic management, international trade, supply chain management, product development, corporate governance, and business innovation whose activities demonstrate significant professional impact."),
    ("1.3.2.", "To develop and maintain an international professional network comprising executives, entrepreneurs, innovators, consultants, educators, and other industry leaders engaged in the advancement of sustainable business practices and modern economic models."),
    ("1.3.3.", "To promote the professional achievements and contributions of its Members at international level and to participate in global discussions related to digital transformation, technology-driven products, platform-based economies, creative industries, and innovation ecosystems."),
    ("1.3.4.", "To support continuous professional development, encourage adherence to high ethical and quality standards, and foster responsible and sustainable approaches to digital product development, financial technologies, corporate innovation, and user-centered design methodologies."),
    ("1.3.5.", "To contribute to the development and dissemination of best practices in business management, international cooperation, and innovation leadership."),
]:
    clause(num, text)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2
# ══════════════════════════════════════════════════════════════════════════════
H1("2. Membership")

H2("2.1. Eligibility")
body("Membership in the Association shall be open to individuals who meet the professional and "
     "reputational standards established by the Association and who satisfy the criteria defined in "
     "this Charter and in the internal regulations adopted by the Association.")

H2("2.2. Membership Criteria")
body("Candidates for membership must demonstrate:")
for num, text in [
    ("2.2.1.", "A high level of professional expertise, leadership experience, strategic competence, and recognized contributions in the fields of business, international trade, supply chain management, entrepreneurship, product development, or related disciplines."),
    ("2.2.2.", "Evidence of international professional recognition, including but not limited to: leadership roles, significant industry achievements, participation in international projects, advisory activities, or comparable contributions to the development of business practices."),
    ("2.2.3.", "Documented professional engagement, which may include publications, academic or industry articles, media appearances, public speaking engagements, teaching activities, conference participation, advisory services, or other forms of recognized professional contribution."),
    ("2.2.4.", "Demonstrable impact on the development of business ecosystems, digital products, innovation initiatives, strategic transformation programs, or related areas within the EMEA region and internationally."),
]:
    clause(num, text)

H2("2.3. Admission Procedure")
body("The procedure for admission, evaluation of candidates, approval of membership, suspension, and "
     "termination of membership shall be governed by internal regulations approved by the competent "
     "governing body of the Association.")

H2("2.4. Principles of Membership")
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
    bul(item)

# ══════════════════════════════════════════════════════════════════════════════
# 2.5 — HONORARY (SENIOR) MEMBERS
# ══════════════════════════════════════════════════════════════════════════════
H2("2.5. Honorary (Senior) Members")
body("The Association may grant Honorary (Senior) Member status to individuals who have demonstrated "
     "outstanding achievements in the field of business and whose professional legacy, influence, or "
     "contribution to the advancement of the business community has been recognized at an international level.")

inline("2.5.1. Definition.",
       "An Honorary (Senior) Member is an individual recognized by the Association for exceptional "
       "and sustained contributions to the field of business, including but not limited to: founding "
       "or scaling transformative enterprises, shaping industry standards, advancing international "
       "business cooperation, or mentoring the next generation of business leaders. Honorary (Senior) "
       "Member status is a distinction of honor and does not carry the obligations of regular "
       "membership, unless the individual voluntarily assumes them.")

inline("2.5.2. Eligibility Criteria.",
       "A candidate for Honorary (Senior) Member status must satisfy at least three (3) of the "
       "following criteria:")
for item in [
    "(a) has held a senior executive, board, or advisory position in one or more organizations of international significance for a cumulative period of not less than ten (10) years;",
    "(b) has made a measurable and recognized contribution to the development of a business sector, market, or professional community at the regional (EMEA) or global level, evidenced by industry reports, independent assessments, peer recognition, or comparable sources;",
    "(c) has been the recipient of internationally recognized professional honors, awards, fellowships, or distinctions in the field of business, entrepreneurship, innovation, or economic development;",
    "(d) has authored, co-authored, or substantially contributed to publications, research, frameworks, or standards that have demonstrably influenced business practices, governance models, or industry thought leadership;",
    "(e) has served as a mentor, educator, or advocate for emerging business leaders, contributing to the professional development of others in a sustained and verifiable manner;",
    "(f) has represented the business community in international forums, governmental advisory bodies, intergovernmental organizations, or multi-stakeholder platforms in a capacity that advanced the interests of the business profession.",
]:
    subitem(item)

inline("2.5.3. Nomination and Admission Procedure.",
       "Candidates may be nominated by: (i) any two (2) current Members; (ii) the President of the "
       "Association; or (iii) the Admissions Committee acting on its own initiative. Nominations must "
       "be submitted in writing with a statement of justification addressing the criteria in §2.5.2. "
       "The Admissions Committee shall review the nomination and make a recommendation to the governing "
       "body. The final decision shall be adopted by the governing body by simple majority.")

inline("2.5.4. Rights and Privileges.",
       "Honorary (Senior) Members are entitled to use the designation 'Honorary Member' or 'Senior "
       "Member'; participate in Association events and activities; receive publications; and be listed "
       "in the official register of Honorary Members. They are exempt from membership fees unless "
       "they elect to contribute voluntarily.")

inline("2.5.5. Revocation.",
       "Honorary (Senior) Member status may be revoked by the governing body following a review by "
       "the Admissions Committee in the event of conduct materially inconsistent with the values or "
       "reputation of the Association.")

# ══════════════════════════════════════════════════════════════════════════════
# 2.6 — ADMISSIONS COMMITTEE
# ══════════════════════════════════════════════════════════════════════════════
H2("2.6. Admissions Committee")
body("The Admissions Committee is the standing body of the Association responsible for evaluating "
     "applications and nominations for all categories of membership, including Honorary (Senior) Members.")

inline("2.6.1. Composition.",
       "The Committee shall consist of 3–7 members appointed by the governing body for a term of "
       "two (2) years, renewable once. It shall be chaired by a Chairperson elected from among its "
       "members. At least one member shall hold Honorary (Senior) Member status where such members "
       "exist. Members must be in good standing and free of conflicts of interest.")

inline("2.6.2. Functions and Powers.",
       "The Admissions Committee shall: (a) receive and process applications and nominations; "
       "(b) verify eligibility criteria; (c) conduct due diligence; (d) issue written recommendations "
       "on admission, deferral, or rejection; (e) maintain a confidential register of applications; "
       "(f) periodically review membership criteria; and (g) conduct reviews in revocation cases.")

inline("2.6.3. Procedure of Meetings.",
       "The Committee shall meet not less than four (4) times per year, in person or electronically. "
       "A quorum consists of a majority of members in office. Decisions are adopted by simple "
       "majority; in the event of a tie the Chairperson has a casting vote.")

inline("2.6.4. Minutes of Meetings.",
       "Minutes shall be drawn up for each meeting, recording: date, time and location; members "
       "present and absent; agenda; summary of deliberations; decisions on each application "
       "(approved / deferred / rejected) with brief reasons; and any dissenting opinions. Minutes "
       "shall be signed by the Chairperson and Secretary, approved at the following meeting, and "
       "retained for a minimum of five (5) years. Personal data shall be processed in accordance "
       "with applicable data protection laws.")

inline("2.6.5. Confidentiality.",
       "All deliberations and the content of individual applications shall be strictly confidential. "
       "Committee members shall not disclose information relating to specific candidates outside the "
       "Committee, except as required by the governing body or applicable law.")

# ══════════════════════════════════════════════════════════════════════════════
# CERTIFICATION  — kept together, never starts a page alone
# ══════════════════════════════════════════════════════════════════════════════
cert_items = []

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
r = p.add_run("Certification")
r.bold = True
r.font.size = Pt(FS_H2)
sp(p, before=8, after=3, line=14)
cert_items.append(p)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
r = p.add_run("This excerpt is issued in accordance with the original Charter of the Association.")
r.font.size = Pt(FS)
sp(p, before=0, after=6, line=14)
cert_items.append(p)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
p.add_run().add_picture("/workspace/Подпись устав .png", width=Inches(1.8))
sp(p, before=0, after=3, line=14)
cert_items.append(p)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
r = p.add_run("Date: November 17, 2025")
r.font.size = Pt(FS)
sp(p, before=0, after=6, line=14)
cert_items.append(p)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
r = p.add_run("Domenico Liguori")
r.bold = True
r.font.size = Pt(FS)
sp(p, before=0, after=2, line=14)
cert_items.append(p)

for line in ["President", "Association of Business Professionals (EMEA)", "info@emeaabp.org"]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(line)
    r.font.size = Pt(FS)
    sp(p, before=0, after=2, line=14)
    cert_items.append(p)

# Mark every cert paragraph to keep with the next one
for p in cert_items:
    keep(p)

doc.save("/workspace/Charter_ABP_EMEA_updated.docx")
print("Saved: Charter_ABP_EMEA_updated.docx")
