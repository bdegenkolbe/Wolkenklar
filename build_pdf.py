#!/usr/bin/env python3
"""
build_pdf.py — PDF-Export des Hauptdokuments gemäß Formatvorlage.md
Bibliothek: reportlab
"""

import re
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY, TA_RIGHT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Preformatted, KeepTogether, HRFlowable
)
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate, Frame
from reportlab.lib.fonts import addMapping

DOCUMENT = "Wolkenfrei.md"
OUTPUT = "Wolkenfrei.pdf"

# Colors
NAVY = HexColor("#1B3A5C")
ACCENT = HexColor("#2E75B6")
TABLE_ALT = HexColor("#F2F7FB")
TABLE_BORDER = HexColor("#B0C4DE")
BLOCKQUOTE_BG = HexColor("#F0F5FA")
CODE_BG = HexColor("#F5F5F5")
META_GRAY = HexColor("#666666")
FOOTER_GRAY = HexColor("#999999")
FOOTER_LINE = HexColor("#CCCCCC")
DARK_GRAY = HexColor("#333333")

# Emoji replacements for PDF compatibility
EMOJI_MAP = {
    "🟢": "[G]", "🟡": "[Y]", "🔴": "[R]", "🟠": "[O]",
    "⚠️": "[!]", "❌": "[X]", "✅": "[OK]",
    "🇨🇳": "CN", "🇷🇺": "RU", "🇸🇦": "SA", "🇦🇪": "AE",
    "🇮🇳": "IN", "🇯🇵": "JP", "🇪🇺": "EU", "🇧🇷": "BR",
    "🇮🇱": "IL", "🌍": "AF",
}


def replace_emojis(text):
    for emoji, replacement in EMOJI_MAP.items():
        text = text.replace(emoji, replacement)
    return text


def extract_version(text):
    m = re.search(r"\*\*Version:\*\*\s+(\d+\.\d+)", text)
    return m.group(1) if m else "12.0"


def clean_inline(text):
    """Convert inline Markdown to reportlab XML tags."""
    text = replace_emojis(text)
    # Escape XML chars first
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r'<font face="Courier" size="7.5">\1</font>', text)
    # Links [text](url) → text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Strip anchor IDs {#...}
    text = re.sub(r"\s*\{#[^}]+\}", "", text)
    return text


def create_styles():
    styles = {}

    styles["h1"] = ParagraphStyle(
        "H1", fontName="Helvetica-Bold", fontSize=22,
        textColor=NAVY, spaceAfter=6*mm, spaceBefore=2*mm,
        leading=26
    )
    styles["subtitle"] = ParagraphStyle(
        "Subtitle", fontName="Helvetica", fontSize=11,
        textColor=ACCENT, spaceAfter=3*mm
    )
    styles["meta"] = ParagraphStyle(
        "Meta", fontName="Helvetica", fontSize=9,
        textColor=META_GRAY, spaceAfter=1*mm, leading=12
    )
    styles["h2"] = ParagraphStyle(
        "H2", fontName="Helvetica-Bold", fontSize=14,
        textColor=NAVY, spaceBefore=4*mm, spaceAfter=3*mm,
        leading=17
    )
    styles["h3"] = ParagraphStyle(
        "H3", fontName="Helvetica-Bold", fontSize=12,
        textColor=ACCENT, spaceBefore=3*mm, spaceAfter=2*mm,
        leading=15
    )
    styles["h4"] = ParagraphStyle(
        "H4", fontName="Helvetica-Bold", fontSize=10.5,
        textColor=DARK_GRAY, spaceBefore=2*mm, spaceAfter=1.5*mm,
        leading=13
    )
    styles["body"] = ParagraphStyle(
        "Body", fontName="Helvetica", fontSize=9.5,
        textColor=black, alignment=TA_JUSTIFY,
        spaceBefore=1*mm, spaceAfter=2*mm, leading=13
    )
    styles["blockquote"] = ParagraphStyle(
        "Blockquote", fontName="Helvetica-Oblique", fontSize=9,
        textColor=DARK_GRAY, alignment=TA_LEFT,
        leftIndent=8*mm, spaceBefore=2*mm, spaceAfter=2*mm,
        leading=12, backColor=BLOCKQUOTE_BG,
        borderColor=ACCENT, borderWidth=1.5, borderPadding=4*mm,
    )
    styles["code"] = ParagraphStyle(
        "Code", fontName="Courier", fontSize=7.5,
        textColor=DARK_GRAY, leftIndent=6*mm,
        spaceBefore=2*mm, spaceAfter=2*mm, leading=10,
        backColor=CODE_BG,
    )
    styles["bullet"] = ParagraphStyle(
        "Bullet", fontName="Helvetica", fontSize=9.5,
        textColor=black, alignment=TA_LEFT,
        leftIndent=10*mm, bulletIndent=4*mm,
        spaceBefore=0.5*mm, spaceAfter=0.5*mm, leading=13,
        bulletFontName="Helvetica", bulletFontSize=9.5,
    )
    return styles


def parse_table(lines, start_idx):
    """Parse a Markdown table starting at start_idx. Returns (rows, end_idx)."""
    rows = []
    i = start_idx
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith("|"):
            break
        # Skip separator rows
        if re.match(r"^\|[\s\-:|]+\|$", line):
            i += 1
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        rows.append(cells)
        i += 1
    return rows, i


def build_table(rows, styles, content_width):
    """Build a reportlab Table from parsed rows."""
    if not rows:
        return None

    # Convert cells to Paragraphs
    header_style = ParagraphStyle(
        "TH", fontName="Helvetica-Bold", fontSize=7.5,
        textColor=white, leading=10
    )
    cell_style = ParagraphStyle(
        "TD", fontName="Helvetica", fontSize=7.5,
        textColor=black, leading=10
    )

    table_data = []
    for row_idx, row in enumerate(rows):
        style = header_style if row_idx == 0 else cell_style
        table_data.append([
            Paragraph(clean_inline(cell), style) for cell in row
        ])

    ncols = max(len(r) for r in table_data) if table_data else 1
    col_width = content_width / ncols

    t = Table(table_data, colWidths=[col_width] * ncols, repeatRows=1)

    # Table style
    ts = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.5),
        ("GRID", (0, 0), (-1, -1), 0.5, TABLE_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("WORDWRAP", (0, 0), (-1, -1), True),
    ]

    # Alternating row colors
    for row_idx in range(1, len(table_data)):
        if row_idx % 2 == 0:
            ts.append(("BACKGROUND", (0, row_idx), (-1, row_idx), TABLE_ALT))

    t.setStyle(TableStyle(ts))
    return t


def build_blockquote_table(raw_lines, content_width):
    """Render a blockquote as a nested Table: outer table for left indent,
    inner table with accent-colored bar column and content column.
    This avoids ReportLab's borderPadding height-calculation bug."""
    inner_style = ParagraphStyle(
        "BQText", fontName="Helvetica-Oblique", fontSize=9,
        textColor=DARK_GRAY, leading=12, spaceBefore=1 * mm,
    )
    bullet_style = ParagraphStyle(
        "BQBullet", fontName="Helvetica-Oblique", fontSize=9,
        textColor=DARK_GRAY, leading=12, leftIndent=4 * mm, spaceBefore=0.5 * mm,
    )

    items = []
    for raw in raw_lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith("- ") or line.startswith("* "):
            items.append(Paragraph(f"\u2022 {clean_inline(line[2:])}", bullet_style))
        else:
            t = clean_inline(line)
            if t:
                items.append(Paragraph(t, inner_style))

    if not items:
        return None

    BAR_W = 3 * mm
    INDENT = 8 * mm
    PAD = 4 * mm
    box_width = content_width - INDENT

    inner = Table(
        [["", items]],
        colWidths=[BAR_W, box_width - BAR_W],
    )
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLOCKQUOTE_BG),
        ("BACKGROUND", (0, 0), (0, 0), ACCENT),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
        ("TOPPADDING", (0, 0), (0, 0), 0),
        ("BOTTOMPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), PAD),
        ("RIGHTPADDING", (1, 0), (1, 0), PAD),
        ("TOPPADDING", (1, 0), (1, 0), PAD),
        ("BOTTOMPADDING", (1, 0), (1, 0), PAD),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    wrapper = Table(
        [["", inner]],
        colWidths=[INDENT, box_width],
    )
    wrapper.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    return wrapper


class DocTemplate(BaseDocTemplate):
    def __init__(self, filename, version, **kwargs):
        self.version = version
        super().__init__(filename, **kwargs)

    def afterPage(self):
        pass


def header_footer(canvas, doc):
    """Draw header and footer on each page."""
    canvas.saveState()
    width, height = A4

    # Header
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(FOOTER_GRAY)
    y_header = height - 1.5 * cm
    canvas.drawString(2 * cm, y_header, "US CLOUD Act & Deutsche Datensouveränität")
    canvas.drawRightString(width - 2 * cm, y_header, "4K Analytics GmbH / HIGL")
    # Header line
    canvas.setStrokeColor(FOOTER_LINE)
    canvas.setLineWidth(0.5)
    canvas.line(2 * cm, y_header - 3, width - 2 * cm, y_header - 3)

    # Footer
    y_footer = 1.5 * cm
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(FOOTER_GRAY)
    version = getattr(doc, "version", "12.0")
    canvas.drawString(2 * cm, y_footer, f"Version {version} — April 2026 — Vertraulich")
    canvas.drawRightString(width - 2 * cm, y_footer, f"Seite {canvas.getPageNumber()}")
    # Footer line
    canvas.setStrokeColor(FOOTER_LINE)
    canvas.line(2 * cm, y_footer + 10, width - 2 * cm, y_footer + 10)

    canvas.restoreState()


def build_pdf():
    with open(DOCUMENT, "r", encoding="utf-8") as f:
        text = f.read()

    version = extract_version(text)
    lines = text.split("\n")
    styles = create_styles()

    width, height = A4
    content_width = width - 4 * cm  # 2cm left + 2cm right

    doc = DocTemplate(
        OUTPUT,
        version=version,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    frame = Frame(
        2 * cm, 2.5 * cm,
        content_width, height - 5 * cm,
        id="main"
    )
    template = PageTemplate(id="main", frames=[frame], onPage=header_footer)
    doc.addPageTemplates([template])

    story = []
    i = 0
    first_h2 = True
    in_code_block = False
    code_lines = []
    in_blockquote = False
    blockquote_lines = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code block
        if stripped.startswith("```"):
            if in_code_block:
                # End code block
                code_text = "\n".join(code_lines)
                code_text = replace_emojis(code_text)
                code_text = code_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                story.append(Preformatted(code_text, styles["code"]))
                code_lines = []
                in_code_block = False
            else:
                # Flush blockquote if pending
                if in_blockquote and blockquote_lines:
                    bq_table = build_blockquote_table(blockquote_lines, content_width)
                    if bq_table:
                        story.append(bq_table)
                    blockquote_lines = []
                    in_blockquote = False
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            # Preserve inner content as-is (including "- " bullet prefix)
            blockquote_lines.append(stripped[1:])
            in_blockquote = True
            i += 1
            continue
        elif in_blockquote and blockquote_lines:
            bq_table = build_blockquote_table(blockquote_lines, content_width)
            if bq_table:
                story.append(bq_table)
            blockquote_lines = []
            in_blockquote = False

        # Separator
        if stripped == "---":
            i += 1
            continue

        # Empty line
        if stripped == "":
            i += 1
            continue

        # H1
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title = clean_inline(stripped[2:])
            story.append(Paragraph(title, styles["h1"]))
            i += 1
            continue

        # H2
        if stripped.startswith("## ") and not stripped.startswith("### "):
            # Skip ToC heading
            if "Inhaltsverzeichnis" in stripped:
                # Skip ToC section
                i += 1
                while i < len(lines) and not lines[i].strip().startswith("---"):
                    i += 1
                i += 1  # skip the ---
                continue

            # Subtitle (line 2)
            if not re.match(r"^## \d+\.", stripped) and "Fazit" not in stripped:
                title = clean_inline(stripped[3:])
                story.append(Paragraph(title, styles["subtitle"]))
                i += 1
                continue

            if not first_h2:
                story.append(PageBreak())
                # Accent line
                story.append(HRFlowable(
                    width="100%", thickness=1.5, color=ACCENT,
                    spaceBefore=0, spaceAfter=2*mm
                ))
            first_h2 = False

            title = clean_inline(stripped[3:])
            story.append(Paragraph(title, styles["h2"]))
            i += 1
            continue

        # H3
        if stripped.startswith("### ") and not stripped.startswith("#### "):
            title = clean_inline(stripped[4:])
            story.append(Paragraph(title, styles["h3"]))
            i += 1
            continue

        # H4
        if stripped.startswith("#### "):
            title = clean_inline(stripped[5:])
            story.append(Paragraph(title, styles["h4"]))
            i += 1
            continue

        # Table
        if stripped.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
            rows, end_idx = parse_table(lines, i)
            if rows:
                t = build_table(rows, styles, content_width)
                if t:
                    story.append(Spacer(1, 2*mm))
                    story.append(t)
                    story.append(Spacer(1, 2*mm))
            i = end_idx
            continue

        # Bullet
        if stripped.startswith("- ") or stripped.startswith("* "):
            bullet_text = clean_inline(stripped[2:])
            story.append(Paragraph(
                f"• {bullet_text}", styles["bullet"]
            ))
            i += 1
            continue

        # Metadata lines (bold key: value)
        if stripped.startswith("**") and ":**" in stripped and i < 10:
            text_clean = clean_inline(stripped)
            story.append(Paragraph(text_clean, styles["meta"]))
            i += 1
            continue

        # Regular paragraph
        para_lines = [stripped]
        i += 1
        while i < len(lines):
            next_line = lines[i].strip()
            if (next_line == "" or next_line.startswith("#") or
                next_line.startswith("|") or next_line.startswith(">") or
                next_line.startswith("```") or next_line.startswith("---") or
                next_line.startswith("- ") or next_line.startswith("* ")):
                break
            para_lines.append(next_line)
            i += 1

        para_text = clean_inline(" ".join(para_lines))
        if para_text.strip():
            story.append(Paragraph(para_text, styles["body"]))

    # Flush any trailing blockquote
    if in_blockquote and blockquote_lines:
        bq_table = build_blockquote_table(blockquote_lines, content_width)
        if bq_table:
            story.append(bq_table)

    # Build PDF
    doc.build(story)
    print(f"PDF erstellt: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
