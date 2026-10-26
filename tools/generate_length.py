from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import hashlib

pdfmetrics.registerFont(TTFont('Pack', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PackBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/Kids-Comparing-Lengths-Pack.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(OUT), pagesize=A4, invariant=1)
c.setTitle('Comparing Lengths with Equal Units | Homeschool Hub')
c.setAuthor('Homeschool Hub')
W,H = A4
def text(x,y,s,size=13,bold=False):
    c.setFont('PackBold' if bold else 'Pack',size)
    c.drawString(x,y,s)
def start(title,page):
    text(42,H-40,'HOMESCHOOL HUB  /  FREE PRINTABLE',10,True)
    text(42,H-78,title,23,True)
    c.line(42,H-94,W-42,H-94)
    text(42,28,'Comparing Lengths | Ages about 5-7 | Personal use',9)
    text(W-80,28,f'{page} / 4',9)
def lines(items,y,size=13):
    for s in items:
        text(42,y,s,size); y-=23
def bar(x,y,n,label,units=True):
    text(x-26,y+7,label,14,True)
    c.setLineWidth(1.4)
    c.rect(x,y,n*32,24)
    if units:
        for j in range(1,n): c.line(x+j*32,y,x+j*32,y+24)
def end(): c.showPage()

start('Comparing Lengths',1)
lines(['Parent guide: use equal-sized units',
       'Try one activity at a time for 5-10 minutes.',
       'Your child should be able to count up to 8.',
       'Read the instructions aloud. Spoken answers are welcome.',
       'You need a pencil. No ruler or cutting is needed.'],H-128)
text(42,565,'Model it together',17,True)
lines(['Each small box is one unit. All the boxes are the same size.',
       'Count the boxes, not the dividing lines.'],537)
bar(85,450,4,'A');bar(85,400,6,'B')
lines(['A is 4 units long. B is 6 units long.',
       'B is longer than A. A is shorter than B.',
       'The left ends line up so the lengths are easy to compare.'],360)
text(42,260,'Help without giving the answer',17,True)
lines(['Ask: "Where does it start? Where does it end?"',
       'Ask: "Can you touch each box once as you count?"',
       'If counting is tricky, compare the aligned ends first.',
       'When measuring with objects, use equal-sized units placed',
       'end to end, with no gaps or overlaps. These are units, not cm.'],231)
lines(['Print pages 2-3 on A4, preferably at actual size.',
       'Black-and-white printing is suitable. Answers are on page 4.'],84,11)
end()

start('1. Compare the strips',2)
lines(['The left ends line up. Look at where each strip ends.',
       'Circle A or B for questions 1-3; Yes or No for question 4.'],H-123)
for y,n,a,b,prompt in [(605,1,3,5,'Which strip is longer?'),(440,2,7,4,'Which strip is shorter?'),(275,3,6,2,'Which strip is longer?')]:
    text(42,y+40,f'{n}. {prompt}     A / B',15,True)
    bar(85,y,a,'A',False);bar(85,y-45,b,'B',False)
text(42,145,'4. Are these strips the same length?   Yes / No',15,True)
bar(85,100,4,'A',False);bar(85,60,4,'B',False)
end()

start('2. Count equal units',3)
lines(['Each small box is one unit. Count the boxes in each strip.',
       'Write or say how many units long each strip is.'],H-123)
for y,label,n in [(620,'A',3),(525,'B',5),(430,'C',8),(335,'D',6)]:
    bar(85,y,n,label)
    text(85,y-30,f'{label} is ______ units long.',14)
text(42,245,'Now compare',17,True)
lines(['1. Which strip is the longest?   ______',
       '2. Which strip is the shortest?   ______',
       '3. How many units longer is B than A?   ______'],215,15)
text(42,104,'Explain: How did the boxes help you compare?',13,True)
c.line(42,77,W-42,77)
end()

start('Answers and next steps',4)
text(42,710,'Page 2: Compare the strips',17,True)
lines(['1. B is longer.', '2. B is shorter.', '3. A is longer.',
       '4. Yes. A and B are the same length.'],678)
text(42,555,'Page 3: Count equal units',17,True)
lines(['A = 3 units     B = 5 units     C = 8 units     D = 6 units',
       '1. C is the longest.', '2. A is the shortest.',
       '3. B is 2 units longer than A: 5 - 3 = 2.',
       'Possible explanation: each box is the same size, so more',
       'boxes in a row make a longer strip. Other clear explanations',
       'are welcome.'],523)
text(42,330,'A short hands-on follow-up',17,True)
lines(['Draw two straight strips with their left ends lined up.',
       'Ask your child to point to the longer and shorter strip.',
       'Then draw a pair that are the same length.',
       'Optional stretch: ask your child to draw a strip 7 boxes long',
       'and one 5 boxes long using equal-sized boxes in a row.',
       'How much longer is the first strip? Answer: 2 units.'],298)
lines(['Notice whether your child compares length rather than width,',
       'counts each unit once and uses the same-sized unit throughout.',
       'Repeat with fewer boxes if needed; there is no timed target.'],113,12)
end()
c.save()
print(OUT)
print('sha256',hashlib.sha256(OUT.read_bytes()).hexdigest())
