from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/Kids-Picture-Graphs-to-5-Pack.pdf'
pdfmetrics.registerFont(TTFont('Pack', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PackBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
c = canvas.Canvas(str(OUT), pagesize=A4, invariant=1)
c.setTitle('Read a Picture Graph to 5 | Homeschool Hub')
c.setAuthor('Homeschool Hub')
W, H = A4

def text(x, y, s, size=13, bold=False):
    c.setFont('PackBold' if bold else 'Pack', size)
    c.drawString(x, y, s)

def lines(items, y, size=13):
    for s in items:
        text(42, y, s, size)
        y -= 23

def start(title, page):
    text(42, H-40, 'HOMESCHOOL HUB  /  FREE PRINTABLE', 10, True)
    text(42, H-78, title, 23, True)
    c.line(42, H-94, W-42, H-94)
    text(42, 28, 'Picture Graphs to 5 | Ages about 5-7 | Personal use', 9)
    text(W-80, 28, f'{page} / 4', 9)

def graph(y, values, blank=False):
    c.setLineWidth(1.2)
    for i, (label, count) in enumerate(values):
        yy = y-i*56
        text(48, yy+13, label, 14, True)
        for j in range(5):
            x = 160+j*57
            c.rect(x, yy, 57, 40)
            if not blank and j < count:
                c.circle(x+28.5, yy+20, 11, stroke=1, fill=0)
    c.circle(60, y-3*56-12, 8, stroke=1, fill=0)
    text(78, y-3*56-17, '= 1 toy. Empty boxes do not count.', 12, True)

start('Read a Picture Graph to 5', 1)
lines(['Parent guide', 'Try one activity for 5-10 minutes.',
       'Your child should be able to count up to 5.',
       'Read labels and questions aloud. Spoken answers are welcome.',
       'You need a pencil. No cutting or extra materials are needed.'], 714)
text(42, 575, 'Model it together: toys on a shelf', 17, True)
lines(['A circle stands for one toy. The labels tell the kind of toy.',
       'Count circles, not boxes. All circles have the same value.'], 546)
graph(446, [('Balls', 2), ('Kites', 1), ('Cars', 3)])
lines(['There are 2 balls, 1 kite and 3 cars.',
       'Cars are the largest group: they have the most circles.',
       'Kites are the smallest group: they have the fewest circles.'], 213)
lines(['Point to each circle once. Compare how many circles each row has.',
       'These are made-up toy collections, not a survey to fill in.',
       'Print pages 2-3 on A4. Black-and-white printing is suitable.',
       'Answers and a completed graph are on page 4.'], 111, 11)
c.showPage()

start('1. Read the toy graph', 2)
lines(['Count the circles in each row. Each circle stands for one toy.',
       'Write or say your answers. Empty boxes do not count.'], 714)
graph(604, [('Balls', 4), ('Kites', 2), ('Cars', 5)])
text(42, 370, 'How many?', 17, True)
lines(['1. Balls: ______    Kites: ______    Cars: ______',
       '2. Which kind of toy has the most? __________',
       '3. Which kind of toy has the fewest? __________'], 335, 14)
text(42, 230, 'Compare and explain', 17, True)
lines(['4. How many more cars than balls are there? ______',
       '5. How can the graph help you find the largest group?'], 196, 13)
c.line(42, 135, W-42, 135)
c.line(42, 100, W-42, 100)
c.showPage()

start('2. Complete a toy graph', 3)
lines(['A different toy shelf has: 3 balls, 3 kites and 1 car.',
       'Draw one circle for each toy. Start in the left-hand box.',
       'Put one circle in each box you use. Leave other boxes empty.'], 714)
graph(575, [('Balls', 3), ('Kites', 3), ('Cars', 1)], blank=True)
text(42, 340, 'Read your finished graph', 17, True)
lines(['1. Which two kinds have the same number? __________',
       '2. Which kind has the fewest? __________',
       '3. How many kites are there? ______'], 303, 13)
text(42, 193, 'Check together', 17, True)
lines(['Touch each circle once. Do the rows show 3, 3 and 1?',
       'Do both equal groups start at the left and end together?',
       'If drawing is difficult, an adult can draw as the child counts.'], 162, 12)
c.showPage()

start('Answers and next steps', 4)
text(42, 710, 'Page 2: Read the toy graph', 17, True)
lines(['1. Balls = 4; kites = 2; cars = 5.',
       '2. Cars.     3. Kites.     4. One more car: 5 - 4 = 1.',
       '5. Example: the row with the most circles is the largest group.',
       'Other clear explanations are welcome.'], 678, 12)
text(42, 555, 'Page 3: Completed graph', 17, True)
graph(484, [('Balls', 3), ('Kites', 3), ('Cars', 1)])
lines(['1. Balls and kites.     2. Cars.     3. Three kites.'], 247, 12)
text(42, 199, 'A short follow-up', 17, True)
lines(['Ask your child to explain why balls and kites are equal.',
       'Answer: both rows have 3 circles; each circle means one toy.',
       'Try fewer circles if needed. There is no timed target.',
       'Keep the key the same: one circle always stands for one toy.'], 169, 12)
c.showPage()
c.save()
print(OUT)
print('sha256', hashlib.sha256(OUT.read_bytes()).hexdigest())
