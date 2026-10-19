"""Generate the original Homeschool Hub o'clock pack (ReportLab, A4)."""
from pathlib import Path
from math import sin, cos, pi
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Hub', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('Hub-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'Kids-Telling-Time-Oclock-Pack.pdf'
OUT.parent.mkdir(exist_ok=True)
c = canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
c.setTitle("Telling Time to the Hour | Homeschool Hub")
c.setAuthor('Homeschool Hub')
W, H = A4

def text(x, y, s, size=12, bold=False):
    c.setFont('Hub-Bold' if bold else 'Hub', size)
    c.drawString(x, y, s)

def page(n, title, subtitle):
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0, 0, 0)
    text(42, H-43, 'HOMESCHOOL HUB  /  FREE PRINTABLE', 10, True)
    text(42, H-80, title, 24, True)
    text(42, H-106, subtitle, 12)
    c.setLineWidth(.7)
    c.line(42, 46, W-42, 46)
    text(42, 30, 'Personal use | Homeschool Hub | Telling time to the hour', 9)
    text(W-75, 30, f'{n} / 4', 9)

def clock(x, y, r=60, hour=None, minute=True):
    c.setLineWidth(1.4)
    c.circle(x, y, r)
    for h in range(1, 13):
        a = h*pi/6
        c.setLineWidth(.6)
        c.line(x+sin(a)*r*.89, y+cos(a)*r*.89,
               x+sin(a)*r*.97, y+cos(a)*r*.97)
        c.setFont('Hub', 12)
        c.drawCentredString(x+sin(a)*r*.73, y+cos(a)*r*.73-4, str(h))
    if minute:
        c.setLineWidth(1.8)
        c.line(x, y, x, y+r*.59)
    if hour is not None:
        a = hour*pi/6
        # Thick, short hour hand stays visible when both hands point to 12.
        c.setLineWidth(4)
        c.line(x, y, x+sin(a)*r*.39, y+cos(a)*r*.39)
    c.setFillColorRGB(0, 0, 0)
    c.circle(x, y, 2.8, stroke=0, fill=1)

page(1, 'Telling Time to the Hour', "O'clock | Ages about 5-7 | Parent guide")
text(42, 693, 'Start with a short conversation', 17, True)
for i, s in enumerate([
    'Use this pack when your child can recognise the numbers 1 to 12.',
    'Print pages 2 and 3 at actual size on A4 paper. Black and white is fine.',
    'You need a pencil and, if available, a real clock with two hands.',
    'Try one page for 5-10 minutes. Read the instructions aloud together.'
]): text(42, 665-i*22, s)
clock(145, 454, 85, 3)
text(266, 499, 'This clock shows 3 o\'clock.', 16, True)
text(266, 464, 'The long minute hand points to 12.', 12)
text(266, 439, 'The short hour hand points to 3.', 12)
text(266, 414, 'At o\'clock, the minutes are 00.', 12)
text(266, 389, '3 o\'clock is written 3:00.', 12)
text(42, 314, 'Say it. Point to it. Then try it.', 17, True)
for i,s in enumerate([
    '1. Ask: "Which hand is longer? Where does it point?"',
    '2. Ask: "Where does the short hand point? What time is it?"',
    '3. On page 2, say each time and write the missing hour.',
    '4. On page 3, draw both hands. Answers are on page 4.',
    'If writing is difficult, let your child point or say the time and write for them.',
    'At 12 o\'clock both hands point to 12; the shorter hand overlaps the longer.',
    'A clock face alone does not tell us whether it is morning or evening.'
]): text(42, 283-i*25, s, 11.5)
c.showPage()

read_hours = [1, 3, 5, 7, 9, 11]
draw_hours = [2, 4, 6, 8, 10, 12]
positions = [(165,620),(430,620),(165,420),(430,420),(165,220),(430,220)]
page(2, "Read the o'clock times", 'The long hand points to 12. Look at the short hand. Write the hour.')
for i, ((x,y),h) in enumerate(zip(positions,read_hours),1):
    text(x-90,y+53,f'{i}.',12,True)
    clock(x,y,61,h)
    c.setFont('Hub',14)
    c.drawCentredString(x,y-94,"_____ o'clock")
c.showPage()

page(3, 'Draw both clock hands', 'Draw the long hand to 12. Draw the short hand to the hour shown.')
for i, ((x,y),h) in enumerate(zip(positions,draw_hours),1):
    text(x-90,y+53,f'{i}.',12,True)
    clock(x,y,61,minute=False)
    c.setFont('Hub',14)
    c.drawCentredString(x,y-94,f"{h} o'clock")
c.showPage()

page(4, 'Answers for grown-ups', 'Page 2: read the time. Page 3: check the direction and length of both hands.')
text(42,697,"Page 2: 1. 1 o'clock   2. 3 o'clock   3. 5 o'clock",12,True)
text(42,675,"             4. 7 o'clock   5. 9 o'clock   6. 11 o'clock",12,True)
for i, ((x,y),h) in enumerate(zip(positions,draw_hours),1):
    clock(x,y-17,52,h)
    c.setFont('Hub',12)
    c.drawCentredString(x,y-92,f"Page 3, no. {i}: {h} o'clock")
text(42,78,'At 12:00 both hands point up. The short, thick hand sits over the long hand.',10)
c.showPage()
c.save()
print(OUT)
