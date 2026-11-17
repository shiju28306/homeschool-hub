from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
OUTPUT = ROOT / 'assets/Kids-Capacity-Cupfuls-Pack.pdf'
for name, filename in [('Pack', 'DejaVuSans.ttf'), ('PackBold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('Which Holds More? Measure Capacity with Cupfuls | Homeschool Hub')
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
    text(42, 28, 'Capacity with Cupfuls | Ages about 5-7 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


def container(x, y, width, height, foot):
    # An outlined container, separate from the recorded measurement.
    p = c.beginPath()
    p.moveTo(x - width / 2, y + height)
    p.lineTo(x - foot / 2, y)
    p.lineTo(x + foot / 2, y)
    p.lineTo(x + width / 2, y + height)
    c.setLineWidth(1.6)
    c.drawPath(p)
    c.line(x - width / 2, y + height, x + width / 2, y + height)


def cup(x, y):
    c.setLineWidth(1.4)
    p = c.beginPath()
    p.moveTo(x, y + 21)
    p.lineTo(x + 4, y)
    p.lineTo(x + 20, y)
    p.lineTo(x + 24, y + 21)
    p.close()
    c.drawPath(p)
    c.arc(x + 21, y + 7, x + 32, y + 20, -90, 180)


def row(label, y, shape, count):
    c.setLineWidth(0.8)
    c.roundRect(42, y, 509, 91, 7)
    text(57, y + 40, label, 16, True)
    container(143, y + 17, *shape)
    for i in range(count):
        cup(225 + 45 * i, y + 34)


start('Which Holds More?', 1)
text(42, 714, 'Parent guide', 17, True)
lines(['Capacity is how much a container can hold when full.',
       'Try 5-10 minutes with a child who can count to 6.',
       'An adult can read aloud. A pencil is optional.',
       'Use the pictures and pretend measurements. No water is needed.',
       'Print pages 2-3 in black and white. Answers are on page 4.'], 682)
text(42, 540, 'Model: count equal cupfuls', 17, True)
lines(['Each little cup stands for one full cupful of water.',
       'Use the same measuring cup, filled to the same level each time.',
       'The marks show the cupfuls needed to fill each empty container.'], 510)
row('X', 341, (35, 61, 34), 2)
row('Y', 235, (76, 30, 69), 4)
lines(['X takes 2 cupfuls. Y takes 4 cupfuls.',
       'Y holds more. Four equal cupfuls is more than two.',
       'X looks taller. Use the counts to decide how much each holds.',
       'If two containers take the same number, they hold the same amount.'], 187)
c.showPage()

start('1. Compare the containers', 2)
lines(['Each cup mark shows one full cupful from the same measuring cup.',
       'These are three new containers. Count the cupfuls that fill each one.'], 712)
text(53, 637, 'Container', 13, True)
text(225, 637, 'Cupfuls to fill it', 13, True)
row('A', 531, (36, 55, 29), 3)
row('B', 427, (70, 36, 52), 5)
row('C', 323, (62, 39, 24), 3)
lines(['1. How many cupfuls fill each one? A: _____  B: _____  C: _____',
       '2. Which holds the most? _____',
       '3. Which two hold the same amount? _____ and _____',
       '4. Which holds less, A or B? _____'], 270, 13)
text(42, 133, 'You can point and say the answers while an adult writes.', 11)
c.showPage()

start('2. Choose a fair way', 3)
text(42, 710, '1. Which plan compares capacity fairly?', 16, True)
lines(['Both containers start empty and are filled completely.',
       'In each plan, fill the measuring cup to the same level each time.'], 677)
c.roundRect(42, 548, 509, 70, 7)
text(58, 589, 'Plan A', 14, True)
text(58, 567, 'Use the same measuring cup for both containers.', 13)
c.roundRect(42, 464, 509, 70, 7)
text(58, 505, 'Plan B', 14, True)
text(58, 483, 'Use a small measuring cup for one and a large cup for the other.', 13)
text(42, 427, 'Say or circle A or B. Explain why.', 13)
text(42, 363, '2. Use results from the same measuring cup', 16, True)
lines(['Container D takes 4 full cupfuls. Container E takes 6 full cupfuls.',
       'Which holds more? _____',
       'How many more cupfuls does it hold? _____'], 329, 13)
lines(['If you want, draw 4 tally marks and 6 tally marks.',
       'Pair the marks and count how many are left over.'], 159)
c.showPage()

start('Answers and parent prompts', 4)
text(42, 712, 'Page 2', 17, True)
lines(['1. A: 3 cupfuls. B: 5 cupfuls. C: 3 cupfuls.',
       '2. B holds the most.',
       '3. A and C hold the same amount.',
       '4. A holds less than B.'], 680, 13)
text(42, 546, 'Page 3', 17, True)
lines(['1. Plan A. Each counted cupful is the same amount.',
       '    With different measuring cups, the counts alone cannot',
       '    tell us which container holds more.',
       '2. E holds more. It holds 2 more cupfuls (6 compared with 4).'], 514, 13)
text(42, 377, 'Talk about the result', 17, True)
lines(['Ask your child to point to each cup mark as they count.',
       'On page 2, ask which two drawings look different but hold',
       'the same amount. A and C both take 3 equal cupfuls.',
       'If a child chooses by height, return to the measured counts.'], 345)
text(42, 220, 'Support', 17, True)
lines(['Read the question aloud and accept pointing or spoken answers.',
       'For the difference question, match four marks from each group.',
       'Two marks remain in the group of six.'], 188)
c.showPage()
c.save()
print(OUTPUT)
