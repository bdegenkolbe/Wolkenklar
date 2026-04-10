#!/usr/bin/env node
/**
 * build_docx.js — Generates a professional DOCX from Wolkenfrei.md
 * Uses the docx npm library and follows Formatvorlage.md design specs.
 */

const fs = require("fs");
const path = require("path");
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  WidthType,
  AlignmentType,
  HeadingLevel,
  Header,
  Footer,
  PageNumber,
  BorderStyle,
  ShadingType,
  TableLayoutType,
  convertMillimetersToTwip,
  ExternalHyperlink,
  PageBreak,
  Tab,
  TabStopPosition,
  TabStopType,
} = require("docx");

// ---------- Configuration ----------

const INPUT_FILE = path.join(__dirname, "Wolkenfrei.md");
const OUTPUT_FILE = path.join(__dirname, "Wolkenfrei.docx");

const COLORS = {
  primary: "1B3A5C",
  accent: "2E75B6",
  h4: "333333",
  body: "000000",
  tableHeaderBg: "1B3A5C",
  tableHeaderText: "FFFFFF",
  tableAltRow: "F2F7FB",
  tableBorder: "B0C4DE",
  blockquoteBg: "F0F5FA",
  blockquoteBar: "2E75B6",
  codeBg: "F5F5F5",
  codeText: "333333",
  metadata: "666666",
  headerFooter: "999999",
  headerFooterLine: "CCCCCC",
};

const FONT = "Arial";
const CODE_FONT = "Consolas";

// pt to half-points (docx uses half-points for font size)
const pt = (n) => n * 2;

// ---------- Read and extract version ----------

const md = fs.readFileSync(INPUT_FILE, "utf-8");

function extractVersion(text) {
  const match = text.match(/\*\*Version:\*\*\s*(.+?)(?:\n|$)/);
  if (match) {
    // e.g. "11.0 — April 2026 · 161 Quellen · 18 Kapitel"
    const verLine = match[1].trim();
    const verNum = verLine.match(/^([\d.]+)/);
    return verNum ? verNum[1] : "11.0";
  }
  return "11.0";
}

const versionNumber = extractVersion(md);
const footerVersionText = `Version ${versionNumber} \u2014 April 2026 \u2014 Vertraulich`;

// ---------- Markdown Parser ----------

function parseMarkdown(text) {
  const lines = text.split("\n");
  const elements = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Blank line
    if (line.trim() === "") {
      i++;
      continue;
    }

    // Horizontal rule
    if (/^---+\s*$/.test(line.trim())) {
      i++;
      continue;
    }

    // Code block
    if (line.trim().startsWith("```")) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith("```")) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // skip closing ```
      elements.push({ type: "code", content: codeLines.join("\n") });
      continue;
    }

    // Table
    if (line.trim().startsWith("|") && i + 1 < lines.length && /^\|[-\s|:]+\|$/.test(lines[i + 1].trim())) {
      const tableLines = [];
      while (i < lines.length && lines[i].trim().startsWith("|")) {
        tableLines.push(lines[i]);
        i++;
      }
      elements.push(parseTable(tableLines));
      continue;
    }

    // Blockquote
    if (line.startsWith(">") || line.startsWith("> ")) {
      const quoteLines = [];
      while (i < lines.length && (lines[i].startsWith(">") || lines[i].startsWith("> "))) {
        let qLine = lines[i].replace(/^>\s?/, "");
        quoteLines.push(qLine);
        i++;
      }
      elements.push({ type: "blockquote", content: quoteLines.join("\n") });
      continue;
    }

    // Headings
    const h1Match = line.match(/^# (.+)$/);
    if (h1Match) {
      elements.push({ type: "h1", content: h1Match[1].trim() });
      i++;
      continue;
    }

    const h2Match = line.match(/^## (.+?)(?:\s*\{#[^}]+\})?\s*$/);
    if (h2Match) {
      elements.push({ type: "h2", content: h2Match[1].trim() });
      i++;
      continue;
    }

    const h3Match = line.match(/^### (.+?)(?:\s*\{#[^}]+\})?\s*$/);
    if (h3Match) {
      elements.push({ type: "h3", content: h3Match[1].trim() });
      i++;
      continue;
    }

    const h4Match = line.match(/^#### (.+?)(?:\s*\{#[^}]+\})?\s*$/);
    if (h4Match) {
      elements.push({ type: "h4", content: h4Match[1].trim() });
      i++;
      continue;
    }

    // Bullet list
    if (/^- /.test(line)) {
      const items = [];
      while (i < lines.length && /^- /.test(lines[i])) {
        let item = lines[i].replace(/^- /, "");
        // Continuation lines (indented)
        while (i + 1 < lines.length && lines[i + 1].match(/^\s+\S/) && !lines[i + 1].match(/^- /)) {
          i++;
          item += " " + lines[i].trim();
        }
        items.push(item);
        i++;
      }
      elements.push({ type: "bullets", items });
      continue;
    }

    // Numbered list
    if (/^\d+\.\s/.test(line)) {
      const items = [];
      while (i < lines.length && /^\d+\.\s/.test(lines[i])) {
        let item = lines[i].replace(/^\d+\.\s/, "");
        items.push(item);
        i++;
      }
      elements.push({ type: "numbered", items });
      continue;
    }

    // Regular paragraph (may span multiple non-blank lines)
    let para = line;
    i++;
    while (
      i < lines.length &&
      lines[i].trim() !== "" &&
      !lines[i].startsWith("#") &&
      !lines[i].startsWith(">") &&
      !lines[i].startsWith("|") &&
      !lines[i].startsWith("```") &&
      !lines[i].startsWith("- ") &&
      !/^\d+\.\s/.test(lines[i]) &&
      !/^---+\s*$/.test(lines[i].trim())
    ) {
      // Handle soft line breaks (trailing two spaces or explicit <br>)
      if (para.endsWith("  ")) {
        para = para.trimEnd() + "\n" + lines[i];
      } else {
        para += " " + lines[i];
      }
      i++;
    }
    elements.push({ type: "paragraph", content: para.trim() });
  }

  return elements;
}

function parseTable(tableLines) {
  // Parse header
  const headerLine = tableLines[0];
  // Skip separator line (index 1)
  const dataLines = tableLines.slice(2);

  function parseCells(line) {
    return line
      .split("|")
      .slice(1, -1)
      .map((c) => c.trim());
  }

  return {
    type: "table",
    headers: parseCells(headerLine),
    rows: dataLines
      .filter((l) => l.trim() !== "")
      .map((l) => parseCells(l)),
  };
}

// ---------- Inline formatting parser ----------

function parseInline(text, options = {}) {
  const runs = [];
  const fontSize = options.fontSize || pt(9.5);
  const fontColor = options.color || COLORS.body;
  const fontName = options.font || FONT;
  const isBold = options.bold || false;
  const isItalic = options.italic || false;

  // Regex to match inline patterns: **bold**, *italic*, [text](url), `code`
  const regex = /(\*\*(.+?)\*\*)|(\*(.+?)\*)|(\[([^\]]+)\]\(([^)]+)\))|(`([^`]+)`)/g;

  let lastIndex = 0;
  let match;

  while ((match = regex.exec(text)) !== null) {
    // Text before match
    if (match.index > lastIndex) {
      const before = text.slice(lastIndex, match.index);
      if (before) {
        runs.push(
          new TextRun({
            text: before,
            font: fontName,
            size: fontSize,
            color: fontColor,
            bold: isBold,
            italics: isItalic,
          })
        );
      }
    }

    if (match[1]) {
      // **bold**
      runs.push(
        new TextRun({
          text: match[2],
          font: fontName,
          size: fontSize,
          color: fontColor,
          bold: true,
          italics: isItalic,
        })
      );
    } else if (match[3]) {
      // *italic*
      runs.push(
        new TextRun({
          text: match[4],
          font: fontName,
          size: fontSize,
          color: fontColor,
          bold: isBold,
          italics: true,
        })
      );
    } else if (match[5]) {
      // [text](url)
      runs.push(
        new ExternalHyperlink({
          children: [
            new TextRun({
              text: match[6],
              font: fontName,
              size: fontSize,
              color: COLORS.accent,
              underline: { type: "single" },
              bold: isBold,
              italics: isItalic,
            }),
          ],
          link: match[7],
        })
      );
    } else if (match[8]) {
      // `code`
      runs.push(
        new TextRun({
          text: match[9],
          font: CODE_FONT,
          size: pt(7.5),
          color: COLORS.codeText,
          bold: isBold,
          italics: isItalic,
          shading: { type: ShadingType.CLEAR, fill: COLORS.codeBg },
        })
      );
    }

    lastIndex = match.index + match[0].length;
  }

  // Remaining text
  if (lastIndex < text.length) {
    runs.push(
      new TextRun({
        text: text.slice(lastIndex),
        font: fontName,
        size: fontSize,
        color: fontColor,
        bold: isBold,
        italics: isItalic,
      })
    );
  }

  if (runs.length === 0) {
    runs.push(
      new TextRun({
        text: text,
        font: fontName,
        size: fontSize,
        color: fontColor,
        bold: isBold,
        italics: isItalic,
      })
    );
  }

  return runs;
}

// ---------- Table border helper ----------

const tableBorder = {
  style: BorderStyle.SINGLE,
  size: 1, // 0.5pt = 1 (in eighths of a point... size is in 1/8 pt, so 4 = 0.5pt)
  color: COLORS.tableBorder,
};

const tableBorders = {
  top: tableBorder,
  bottom: tableBorder,
  left: tableBorder,
  right: tableBorder,
  insideHorizontal: tableBorder,
  insideVertical: tableBorder,
};

// ---------- Build document children ----------

function buildChildren(elements) {
  const children = [];
  let h2Count = 0;
  let isFirstElement = true;

  for (const el of elements) {
    switch (el.type) {
      case "h1": {
        children.push(
          new Paragraph({
            children: [
              new TextRun({
                text: el.content,
                font: FONT,
                size: pt(22),
                bold: true,
                color: COLORS.primary,
              }),
            ],
            spacing: { after: 120 },
          })
        );
        break;
      }

      case "h2": {
        h2Count++;
        const h2Children = [
          new TextRun({
            text: el.content,
            font: FONT,
            size: pt(14),
            bold: true,
            color: COLORS.primary,
          }),
        ];

        children.push(
          new Paragraph({
            children: h2Children,
            spacing: { before: 240, after: 120 },
            // Page break before each H2 except the first
            ...(h2Count > 1
              ? { pageBreakBefore: true }
              : {}),
            border: {
              top: {
                style: BorderStyle.SINGLE,
                size: 3, // 1.5pt in eighths = 12, but docx lib uses different unit; 3 = ~1.5pt
                color: COLORS.accent,
                space: 4,
              },
            },
          })
        );
        break;
      }

      case "h3": {
        children.push(
          new Paragraph({
            children: [
              new TextRun({
                text: el.content,
                font: FONT,
                size: pt(12),
                bold: true,
                color: COLORS.accent,
              }),
            ],
            spacing: { before: 200, after: 80 },
          })
        );
        break;
      }

      case "h4": {
        children.push(
          new Paragraph({
            children: [
              new TextRun({
                text: el.content,
                font: FONT,
                size: pt(10.5),
                bold: true,
                color: COLORS.h4,
              }),
            ],
            spacing: { before: 160, after: 60 },
          })
        );
        break;
      }

      case "paragraph": {
        // Handle multi-line paragraphs (with \n for line breaks)
        const lines = el.content.split("\n");
        const runs = [];
        for (let li = 0; li < lines.length; li++) {
          if (li > 0) {
            runs.push(new TextRun({ break: 1 }));
          }
          runs.push(...parseInline(lines[li]));
        }
        children.push(
          new Paragraph({
            children: runs,
            alignment: AlignmentType.JUSTIFIED,
            spacing: {
              line: 276, // 1.15 * 240
              before: 20, // ~1mm
              after: 40,  // ~2mm
            },
          })
        );
        break;
      }

      case "blockquote": {
        // Parse blockquote content into paragraphs
        const bqParagraphs = el.content.split("\n\n");
        for (const bqp of bqParagraphs) {
          const bqLines = bqp.split("\n");
          const runs = [];
          for (let li = 0; li < bqLines.length; li++) {
            const bqLine = bqLines[li];
            if (li > 0) {
              runs.push(new TextRun({ break: 1 }));
            }
            // Handle bullet points inside blockquotes
            if (bqLine.startsWith("- ")) {
              runs.push(
                new TextRun({
                  text: "\u2022 ",
                  font: FONT,
                  size: pt(9),
                  italics: true,
                  color: COLORS.codeText,
                })
              );
              runs.push(
                ...parseInline(bqLine.replace(/^- /, ""), {
                  fontSize: pt(9),
                  color: COLORS.codeText,
                  font: FONT,
                  italic: true,
                })
              );
            } else {
              runs.push(
                ...parseInline(bqLine, {
                  fontSize: pt(9),
                  color: COLORS.codeText,
                  font: FONT,
                  italic: true,
                })
              );
            }
          }
          children.push(
            new Paragraph({
              children: runs,
              indent: { left: convertMillimetersToTwip(8) },
              spacing: { before: 60, after: 60 },
              shading: {
                type: ShadingType.CLEAR,
                fill: COLORS.blockquoteBg,
              },
              border: {
                left: {
                  style: BorderStyle.SINGLE,
                  size: 3,
                  color: COLORS.blockquoteBar,
                  space: 8,
                },
              },
            })
          );
        }
        break;
      }

      case "code": {
        const codeLines = el.content.split("\n");
        for (const codeLine of codeLines) {
          children.push(
            new Paragraph({
              children: [
                new TextRun({
                  text: codeLine || " ",
                  font: CODE_FONT,
                  size: pt(7.5),
                  color: COLORS.codeText,
                }),
              ],
              indent: { left: convertMillimetersToTwip(6) },
              spacing: { before: 0, after: 0, line: 260 },
              shading: {
                type: ShadingType.CLEAR,
                fill: COLORS.codeBg,
              },
            })
          );
        }
        break;
      }

      case "bullets": {
        for (const item of el.items) {
          const runs = [
            new TextRun({
              text: "\u2022  ",
              font: FONT,
              size: pt(9.5),
              color: COLORS.body,
            }),
            ...parseInline(item),
          ];
          children.push(
            new Paragraph({
              children: runs,
              indent: {
                left: convertMillimetersToTwip(10),
                hanging: convertMillimetersToTwip(4),
              },
              spacing: { line: 276, before: 20, after: 20 },
              alignment: AlignmentType.JUSTIFIED,
            })
          );
        }
        break;
      }

      case "numbered": {
        el.items.forEach((item, idx) => {
          const runs = [
            new TextRun({
              text: `${idx + 1}. `,
              font: FONT,
              size: pt(9.5),
              color: COLORS.body,
            }),
            ...parseInline(item),
          ];
          children.push(
            new Paragraph({
              children: runs,
              indent: {
                left: convertMillimetersToTwip(10),
                hanging: convertMillimetersToTwip(5),
              },
              spacing: { line: 276, before: 20, after: 20 },
              alignment: AlignmentType.JUSTIFIED,
            })
          );
        });
        break;
      }

      case "table": {
        const colCount = el.headers.length;
        // Calculate equal column widths based on content area
        // Content width = 210mm - 20mm - 20mm = 170mm
        const contentWidthTwip = convertMillimetersToTwip(170);
        const colWidthTwip = Math.floor(contentWidthTwip / colCount);

        // Cell margins/padding: 3pt top/bottom, 4pt left/right
        const cellMargins = {
          top: 60,
          bottom: 60,
          left: 80,
          right: 80,
        };

        // Build header row
        const headerRow = new TableRow({
          tableHeader: true,
          children: el.headers.map(
            (h) =>
              new TableCell({
                children: [
                  new Paragraph({
                    children: parseInline(h, {
                      fontSize: pt(7.5),
                      color: COLORS.tableHeaderText,
                      bold: true,
                    }),
                    spacing: { before: 20, after: 20 },
                  }),
                ],
                shading: {
                  type: ShadingType.CLEAR,
                  fill: COLORS.tableHeaderBg,
                },
                width: { size: colWidthTwip, type: WidthType.DXA },
                margins: cellMargins,
              })
          ),
        });

        // Build data rows
        const dataRows = el.rows.map(
          (row, rowIdx) =>
            new TableRow({
              children: row.map(
                (cell, cellIdx) =>
                  new TableCell({
                    children: [
                      new Paragraph({
                        children: parseInline(cell, {
                          fontSize: pt(7.5),
                          color: COLORS.body,
                        }),
                        spacing: { before: 20, after: 20 },
                      }),
                    ],
                    shading: {
                      type: ShadingType.CLEAR,
                      fill: rowIdx % 2 === 1 ? COLORS.tableAltRow : "FFFFFF",
                    },
                    width: { size: colWidthTwip, type: WidthType.DXA },
                    margins: cellMargins,
                  })
              ),
            })
        );

        // Handle rows with fewer cells than headers
        const fixedDataRows = dataRows.map((row, rowIdx) => {
          const rowData = el.rows[rowIdx];
          if (rowData.length < colCount) {
            // Pad with empty cells
            const extra = [];
            for (let c = rowData.length; c < colCount; c++) {
              extra.push(
                new TableCell({
                  children: [new Paragraph({ children: [] })],
                  width: { size: colWidthTwip, type: WidthType.DXA },
                  margins: cellMargins,
                  shading: {
                    type: ShadingType.CLEAR,
                    fill: rowIdx % 2 === 1 ? COLORS.tableAltRow : "FFFFFF",
                  },
                })
              );
            }
            return new TableRow({
              children: [...row.root[1].root.slice(0), ...extra],
            });
          }
          return row;
        });

        children.push(
          new Table({
            rows: [headerRow, ...dataRows],
            width: { size: 100, type: WidthType.PERCENTAGE },
            layout: TableLayoutType.FIXED,
            borders: tableBorders,
          })
        );

        // Add small spacing after table
        children.push(
          new Paragraph({
            children: [],
            spacing: { before: 40, after: 40 },
          })
        );
        break;
      }
    }

    isFirstElement = false;
  }

  return children;
}

// ---------- Build document ----------

async function main() {
  console.log("Parsing Markdown...");
  const elements = parseMarkdown(md);
  console.log(`Parsed ${elements.length} elements.`);

  console.log("Building DOCX...");
  const docChildren = buildChildren(elements);

  // Right-aligned tab stop for header/footer
  const rightTabStop = convertMillimetersToTwip(170); // content width

  const doc = new Document({
    sections: [
      {
        properties: {
          page: {
            size: {
              width: convertMillimetersToTwip(210),
              height: convertMillimetersToTwip(297),
            },
            margin: {
              top: convertMillimetersToTwip(25),
              bottom: convertMillimetersToTwip(25),
              left: convertMillimetersToTwip(20),
              right: convertMillimetersToTwip(20),
            },
          },
        },
        headers: {
          default: new Header({
            children: [
              new Paragraph({
                children: [
                  new TextRun({
                    text: "US CLOUD Act & Deutsche Datensouver\u00e4nit\u00e4t",
                    font: FONT,
                    size: pt(7.5),
                    color: COLORS.headerFooter,
                  }),
                  new TextRun({
                    children: [new Tab()],
                  }),
                  new TextRun({
                    text: "4K Analytics GmbH / HIGL",
                    font: FONT,
                    size: pt(7.5),
                    color: COLORS.headerFooter,
                  }),
                ],
                tabStops: [
                  {
                    type: TabStopType.RIGHT,
                    position: rightTabStop,
                  },
                ],
                border: {
                  bottom: {
                    style: BorderStyle.SINGLE,
                    size: 1,
                    color: COLORS.headerFooterLine,
                    space: 4,
                  },
                },
                spacing: { after: 120 },
              }),
            ],
          }),
        },
        footers: {
          default: new Footer({
            children: [
              new Paragraph({
                children: [
                  new TextRun({
                    text: footerVersionText,
                    font: FONT,
                    size: pt(7.5),
                    color: COLORS.headerFooter,
                  }),
                  new TextRun({
                    children: [new Tab()],
                  }),
                  new TextRun({
                    text: "Seite ",
                    font: FONT,
                    size: pt(7.5),
                    color: COLORS.headerFooter,
                  }),
                  new TextRun({
                    children: [PageNumber.CURRENT],
                    font: FONT,
                    size: pt(7.5),
                    color: COLORS.headerFooter,
                  }),
                ],
                tabStops: [
                  {
                    type: TabStopType.RIGHT,
                    position: rightTabStop,
                  },
                ],
                border: {
                  top: {
                    style: BorderStyle.SINGLE,
                    size: 1,
                    color: COLORS.headerFooterLine,
                    space: 4,
                  },
                },
                spacing: { before: 120 },
              }),
            ],
          }),
        },
        children: docChildren,
      },
    ],
    defaultRunProperties: {
      font: FONT,
      size: pt(9.5),
      color: COLORS.body,
    },
  });

  console.log("Packing DOCX...");
  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(OUTPUT_FILE, buffer);
  console.log(`Written: ${OUTPUT_FILE} (${(buffer.length / 1024).toFixed(0)} KB)`);
}

main().catch((err) => {
  console.error("Error:", err);
  process.exit(1);
});
