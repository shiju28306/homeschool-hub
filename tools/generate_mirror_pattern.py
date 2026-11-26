from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import fitz

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets/Kids-Mirror-Pattern-Pack.pdf'
for name, filename in [('Pack', 'DejaVuSans.ttf'), ('PackBold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/' + filename))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('Mirror the Pattern: Line Symmetry on a Grid | Homeschool Hub')
c.setAuthor('Homeschool Hub')
W, H = A4
MODEL = {(1, 2), (3, 1)}
PRACTICE = [{(1, 2), (2, 1), (4, 2)},
            {(1, 1), (2, 1), (3, 2), (4, 1)},
            {(1, 1), (1, 2), (2, 2), (3, 1)}]


def reflect(cells):
    return {(row, 5 - col) for row, col in cells}


def text(x, y, message, size=12, bold=False):
    c.setFont('PackBold' if bold else 'Pack', size)
    c.drawString(x, y, message)


def lines(messages, y, size=12):
    for message in messages:
        text(42, y, message, size)
        y -= 22


def start(title, page):
    c.setLineWidth(1.4)
    text(42, H - 40, 'HOMESCHOOL HUB  /  FREE PRINTABLE', 10, True)
    text(42, H - 78, title, 23, True)
    c.line(42, H - 94, W - 42, H - 94)
    text(42, 28, 'Mirror the Pattern | Ages about 6-8 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


def grid(x, y, cells, size=28):
    # Rows count down from the top; columns count from the left.
    for row, col in cells:
        c.rect(x + (col - 1) * size + 3, y + (4 - row) * size + 3,
               size - 6, size - 6, fill=1, stroke=0)
    c.setLineWidth(0.8)
    for i in range(5):
        c.line(x + i * size, y, x + i * size, y + 4 * size)
        c.line(x, y + i * size, x + 4 * size, y + i * size)
    c.setLineWidth(2.3)
    c.setDash(5, 3)
    c.line(x + 2 * size, y - 10, x + 2 * size, y + 4 * size + 10)
    c.setDash()


start('Mirror the Pattern', 1)
text(42, 712, 'Parent guide: line symmetry', 17, True)
lines(['Try 5-10 minutes with a child aged about 6-8.',
       'An adult can read and mark squares while the child points.',
       'Print pages 2-3 in black and white. Answers are on page 4.',
       'No mirror, cutting or special equipment is needed.'], 680)
text(42, 558, 'Match one row at a time', 17, True)
text(75, 518, 'Start: left side given', 12, True)
text(321, 518, 'Finished mirror pattern', 12, True)
grid(80, 328, MODEL, 40)
grid(330, 328, MODEL | reflect(MODEL), 40)
lines(['The dashed line is the mirror line.',
       'A square beside the line matches the square just across it.',
       'An outer square matches the outer square in the same row.',
       'Shaded AND empty squares must match on both sides.'], 284)
text(42, 156, 'Check the model together', 17, True)
lines(['Top row: the shaded square is next to the line on each side.',
       'Third row: both outer squares are shaded.',
       'Second and bottom rows: all squares stay empty.'], 123)
c.showPage()

start('1. Is it a mirror pattern?', 2)
lines(['Look across the dashed line, one row at a time.',
       'Do shaded and empty squares match? Say or circle Yes or No.'], 712)
examples = [
    {(1, 1), (2, 2), (1, 4), (2, 3)},
    {(1, 1), (2, 2), (1, 4), (2, 4)},
    {(1, 2), (3, 1), (4, 2), (1, 3), (3, 4), (4, 3)},
]
for label, y, cells in zip('ABC', [500, 310, 120], examples):
    c.setLineWidth(0.8)
    c.roundRect(42, y, 509, 161, 7)
    text(58, y + 126, label, 17, True)
    grid(110, y + 23, cells)
    text(303, y + 91, 'Mirror pattern?', 15, True)
    text(303, y + 54, 'Yes / No', 17)
text(42, 78, 'The same number of shaded squares is not enough. Check positions.', 11)
c.showPage()

start('2. Complete the other side', 3)
lines(['Keep the left side as it is. Shade squares on the right to match.',
       'Use the same row and the same distance from the dashed line.'], 712)
for label, y, cells in zip('ABC', [500, 310, 120], PRACTICE):
    c.setLineWidth(0.8)
    c.roundRect(42, y, 509, 161, 7)
    text(58, y + 126, label, 17, True)
    grid(110, y + 23, cells)
    text(304, y + 91, 'Check each row.', 14, True)
    text(304, y + 62, 'Leave matching', 13)
    text(304, y + 42, 'empty squares empty.', 13)
text(42, 78, 'You can point to the squares and ask an adult to shade them.', 11)
c.showPage()

start('Answers and parent prompts', 4)
text(42, 712, 'Page 2', 17, True)
lines(['A: Yes. Each row matches across the line.',
       'B: No. In the second row, the left shaded square is beside',
       'the line, but the right shaded square is at the outer edge.',
       'C: Yes. Both shaded and empty squares match.'], 678, 13)
text(42, 552, 'Page 3: completed patterns', 17, True)
for label, x, cells in zip('ABC', [55, 237, 419], PRACTICE):
    text(x, 508, label, 16, True)
    grid(x, 366, cells | reflect(cells), 28)
text(42, 308, 'Support', 17, True)
lines(['Point to one left square. Find its partner across the line.',
       'Ask: Is it in the same row? Is it just as far from the line?',
       'If both sides have equal counts but look different, check',
       'the square positions. Return to page 2 B as an example.',
       'Let an adult do the shading if pencil control is difficult.',
       'Stop after one pattern if that is enough for today.'], 275)
c.showPage()
c.save()
doc = fitz.open(OUTPUT)
doc[1].get_pixmap(matrix=fitz.Matrix(400 / W, 400 / W)).save(ROOT / 'assets/mirror-pattern-preview.png')
print(OUTPUT)
