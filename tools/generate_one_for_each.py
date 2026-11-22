from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import fitz

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets/Kids-One-for-Each-Pack.pdf'
for name, filename in [('Pack', 'DejaVuSans.ttf'), ('PackBold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/' + filename))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('One for Each: Is There Enough? | Homeschool Hub')
c.setAuthor('Homeschool Hub')
W, H = A4


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
    text(42, 28, 'One for Each | Ages about 3-5 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


def bowl(x, y):
    c.setLineWidth(1.4)
    c.ellipse(x - 20, y + 3, x + 20, y + 11)
    p = c.beginPath()
    p.moveTo(x - 20, y + 7)
    p.curveTo(x - 16, y - 16, x + 16, y - 16, x + 20, y + 7)
    c.drawPath(p)


def spoon(x, y):
    c.setLineWidth(1.4)
    c.ellipse(x - 5, y + 1, x + 5, y + 11)
    p = c.beginPath()
    p.moveTo(x - 2, y + 1)
    p.lineTo(x - 2, y - 8)
    p.curveTo(x - 2, y - 12, x + 2, y - 12, x + 2, y - 8)
    p.lineTo(x + 2, y + 1)
    c.drawPath(p)


def panel(number, y, bowls, spoons, category=False):
    c.setLineWidth(0.8)
    c.roundRect(42, y, 509, 170, 7)
    text(55, y + 149, str(number) + '.', 15, True)
    text(119, y + 149, 'Bowls', 12, True)
    text(364, y + 149, 'Spoons', 12, True)
    for i in range(bowls):
        bowl(140, y + 123 - 27 * i)
    for i in range(spoons):
        spoon(387, y + 123 - 27 * i)
    if category:
        text(58, y + 13, 'Just enough / Too few / One left over', 12)
    else:
        text(58, y + 13, 'Enough spoons for every bowl?   Yes / No', 12)


start('One for Each', 1)
text(42, 714, 'Parent guide: Is there enough?', 17, True)
lines(['Try 5-10 minutes with a child aged about 3-5.',
       'An adult reads. Counting to 4 may help, but matching is the goal.',
       'Print pages 2-3 in black and white. Answers are on page 4.',
       'Point and answer aloud, trace with a finger, or use a pencil.'], 681)
text(42, 565, 'Our rule: one spoon for each bowl', 17, True)
lines(['Match each bowl to one spoon. Use each spoon only once.',
       'Stop when every bowl has a spoon or there are no spoons left.'], 534)
text(117, 461, 'Bowls', 12, True)
text(364, 461, 'Spoons', 12, True)
for y in [418, 368]:
    bowl(140, y)
    spoon(387, y)
    c.line(169, y, 370, y)
lines(['Both bowls have a spoon. There are just enough.',
       'If a bowl has no spoon, there are too few spoons.',
       'If all bowls have a spoon and one spoon is spare,',
       'there are enough, with one left over.'], 306, 13)
text(42, 178, 'Ask: Does every bowl have one?', 16, True)
lines(['On page 2, say Yes or No. On page 3, choose the matching words.',
       'A spare spoon still means there are enough spoons.'], 146)
c.showPage()

start('1. Is there enough?', 2)
lines(['Match one spoon to each bowl. Use each spoon only once.',
       'Trace or draw the joining lines. Then say or circle Yes or No.'], 712)
for number, y, counts in [(1, 490, (2, 2)), (2, 300, (3, 2)), (3, 110, (2, 3))]:
    panel(number, y, *counts)
text(42, 73, 'Remember: a spare spoon is fine if every bowl has one.', 11)
c.showPage()

start('2. What is left?', 3)
lines(['Match one spoon to each bowl. Use each spoon only once.',
       'Say or circle: Just enough, Too few, or One left over.'], 712)
for number, y, counts in [(1, 490, (4, 4)), (2, 300, (4, 3)), (3, 110, (3, 4))]:
    panel(number, y, *counts, category=True)
text(42, 73, 'Look for a bowl without a spoon or a spoon with no bowl.', 11)
c.showPage()

start('Answers and parent prompts', 4)
text(42, 712, 'Page 2: Is there enough?', 17, True)
lines(['1. Yes. Two bowls and two spoons: just enough.',
       '2. No. Three bowls and two spoons: one bowl has no spoon.',
       '3. Yes. Two bowls and three spoons: one spoon is left over.'], 678, 13)
text(42, 570, 'Page 3: What is left?', 17, True)
lines(['1. Just enough. Four bowls and four spoons.',
       '2. Too few. Four bowls and three spoons.',
       '    One bowl has no spoon.',
       '3. One left over. Three bowls and four spoons.',
       '    Every bowl has a spoon and one spoon is spare.'], 536, 13)
text(42, 388, 'Check the matching, not the line shape', 16, True)
lines(['Different pairing lines can be correct, even if they cross.',
       'Each bowl should get one spoon. No spoon is used twice.',
       'For a No answer, ask your child to point to an empty bowl.',
       'For a spare, ask them to point to the spoon left over.'], 354)
text(42, 227, 'Support', 17, True)
lines(['Try just one panel at a time. Model the first pair if needed.',
       'An adult can trace the lines while the child directs or points.',
       'No numeral writing or independent reading is needed.'], 195)
c.showPage()
c.save()
doc = fitz.open(OUTPUT)
doc[1].get_pixmap(matrix=fitz.Matrix(400 / W, 400 / W)).save(ROOT / 'assets/one-for-each-preview.png')
print(OUTPUT)
