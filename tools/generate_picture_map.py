from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
OUTPUT = ROOT / 'assets/Kids-Picture-Map-Pack.pdf'
pdfmetrics.registerFont(TTFont('Pack', str(FONT_DIR / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('PackBold', str(FONT_DIR / 'DejaVuSans-Bold.ttf')))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('Read a Picture Map: Follow the Arrows | Homeschool Hub')
c.setAuthor('Homeschool Hub')
W, H = A4


def text(x, y, words, size=12, bold=False):
    c.setFont('PackBold' if bold else 'Pack', size)
    c.drawString(x, y, words)


def lines(words, y, size=12):
    for line in words:
        text(42, y, line, size)
        y -= 23


def start(title, page):
    c.setLineWidth(1.4)
    text(42, H - 40, 'HOMESCHOOL HUB  /  FREE PRINTABLE', 10, True)
    text(42, H - 78, title, 23, True)
    c.line(42, H - 94, W - 42, H - 94)
    text(42, 28, 'Picture Map | Ages about 5-7 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


def symbol(name, x, y):
    c.setLineWidth(1.5)
    if name == 'tree':
        c.rect(x - 4, y - 16, 8, 13)
        c.circle(x, y + 7, 13)
    elif name == 'tent':
        path = c.beginPath()
        path.moveTo(x - 18, y - 13)
        path.lineTo(x, y + 16)
        path.lineTo(x + 18, y - 13)
        path.close()
        c.drawPath(path)
        c.line(x, y - 13, x, y + 16)
    else:
        c.ellipse(x - 20, y - 13, x + 20, y + 13)
        c.line(x - 10, y + 2, x + 10, y + 2)
        c.line(x - 6, y - 4, x + 6, y - 4)


def key(x, y):
    text(x, y, 'Map key', 15, True)
    for i, name in enumerate(('tree', 'tent', 'pond')):
        row = y - 48 - 57 * i
        symbol(name, x + 20, row)
        text(x + 49, row - 4, name, 13)


def grid(x, y, cells, size=70):
    c.setLineWidth(1.3)
    for col in range(3):
        for row in range(3):
            left, bottom = x + col * size, y + (2 - row) * size
            c.rect(left, bottom, size, size)
            name = cells.get((col, row))
            if name == 'start':
                c.setFont('PackBold', 11)
                c.drawCentredString(left + size / 2, bottom + size / 2 - 4, 'START')
            elif name:
                symbol(name, left + size / 2, bottom + size / 2)


def arrow(x, y, direction):
    angle = {"R": 0, "U": 90, "L": 180, "D": -90}[direction]
    c.saveState()
    c.translate(x, y)
    c.rotate(angle)
    c.setLineWidth(2)
    c.line(-10, 0, 10, 0)
    c.line(10, 0, 3, 6)
    c.line(10, 0, 3, -6)
    c.restoreState()


def route_row(label, directions, y):
    text(42, y - 4, label, 13, True)
    for i, direction in enumerate(directions):
        arrow(93 + i * 38, y, direction)
    text(275, y - 4, 'I land at: __________________', 13)


MAP_A = {(0, 0): 'tree', (2, 0): 'tent', (0, 2): 'pond', (1, 1): 'start'}
MAP_B = {(2, 0): 'tree', (0, 1): 'tent', (2, 2): 'pond', (1, 2): 'start'}

start('Read a Picture Map', 1)
text(42, 714, 'Parent guide', 17, True)
lines(['Try 5-10 minutes. An adult reads aloud. Your child can move a',
       'finger and say the answers. A pencil is optional.',
       'Print pages 2-3 on A4 in black and white. Answers are on page 4.'], 683)
text(42, 580, 'Read the key and model a route', 17, True)
lines(['The key tells you what each picture means. Keep the page upright.',
       'Put your finger on START. Read the arrows from left to right.',
       'Move one square per arrow. Up means toward the top of the page.',
       'You can move through any square, including one with a picture.'], 547)
grid(43, 231, MAP_A)
key(307, 420)
text(42, 181, 'Try these two arrows.', 14, True)
arrow(233, 185, 'U')
arrow(271, 185, 'L')
lines(['Move up one square, then left one square.',
       'Use the key. You land on the tree.',
       'Go back to START before each new route.'], 146)
c.showPage()

start('1. Follow the route', 2)
lines(['Put your finger on START. Follow the arrows in order.',
       'Move one square for each arrow. Use the key to name the place.',
       'Go back to START before each question.'], 714)
grid(43, 416, MAP_A)
key(307, 606)
for i, directions in enumerate(('LU', 'RU', 'DL', 'RDLL'), 1):
    route_row(f'{i}.', directions, 365 - (i - 1) * 64)
lines(['If you get lost, return to START and try the arrows slowly.'], 110, 11)
c.showPage()

start('2. Read a different map', 3)
lines(['Look for the new START square. Read each route from left to right.',
       'Move one square per arrow and use the key to name the place.',
       'Return to START before each question.'], 714)
grid(43, 416, MAP_B)
key(307, 606)
for i, directions in enumerate(('RUU', 'UL', 'R'), 1):
    route_row(f'{i}.', directions, 365 - (i - 1) * 62)
text(42, 161, '4. Find another way to the tent in exactly two moves.', 13, True)
text(42, 132, 'Draw two arrows or say the directions in order.', 12)
c.rect(48, 62, 53, 47)
c.rect(115, 62, 53, 47)
c.showPage()

start('Answers and parent prompts', 4)
text(42, 714, 'Page 2', 17, True)
lines(['1. Left, up: tree.',
       '2. Right, up: tent.',
       '3. Down, left: pond.',
       '4. Right, down, left, left: pond.'], 680, 13)
text(42, 545, 'Page 3', 17, True)
lines(['1. Right, up, up: tree.',
       '2. Up, left: tent.',
       '3. Right: pond.',
       '4. Left, up: tent. Up, left is the route already used in question 2.'], 510, 13)
text(42, 375, 'Talk together', 17, True)
lines(['Ask your child to point to the matching picture in the key.',
       'You can say each direction while your child moves one square.',
       'If your child misses a move, return to START and read one arrow',
       'at a time. You can cover the arrows you have already used.'], 340)
text(42, 210, 'Optional practice', 17, True)
lines(['On page 3, ask for another route to the tree in three moves.',
       'Example: up, up, right. Up, right, up also reaches the tree.',
       'Let your child show the moves with a finger.'], 175)
c.showPage()
c.save()
print(OUTPUT)
