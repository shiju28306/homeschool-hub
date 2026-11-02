from pathlib import Path
import hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/Kids-Halves-Equal-Parts-Pack.pdf'
pdfmetrics.registerFont(TTFont('Pack','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PackBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
c=canvas.Canvas(str(OUT),pagesize=A4,invariant=1)
c.setTitle('Halves: Two Equal Parts | Homeschool Hub');c.setAuthor('Homeschool Hub')
W,H=A4

def text(x,y,s,size=13,bold=False):
    c.setFont('PackBold'if bold else'Pack',size);c.drawString(x,y,s)

def lines(items,y,size=13):
    for s in items:text(42,y,s,size);y-=23

def start(title,page):
    c.setLineWidth(1.2)
    text(42,H-40,'HOMESCHOOL HUB  /  FREE PRINTABLE',10,True)
    text(42,H-78,title,23,True);c.line(42,H-94,W-42,H-94)
    text(42,28,'Halves | Ages about 5-7 | Personal use',9)
    text(W-80,28,f'{page} / 4',9)

def dots(x,y,n,step=24):
    c.setLineWidth(1.4)
    for i in range(n):c.circle(x+i*step,y,6,stroke=1,fill=0)

def shape(cx,y,kind):
    c.setLineWidth(1.8)
    if kind in ('circle-half','circle-unequal'):
        c.circle(cx,y+38,37)
        yy=y+38 if kind=='circle-half'else y+59
        dx=37 if kind=='circle-half'else (37**2-21**2)**.5
        c.line(cx-dx,yy,cx+dx,yy)
    elif kind=='diagonal':
        c.rect(cx-38,y,76,76);c.line(cx-38,y,cx+38,y+76)
    else:
        c.rect(cx-63,y,126,76)
        if kind=='thirds':
            for d in (-21,21):c.line(cx+d,y,cx+d,y+76)
        else:
            xx=cx if kind=='rect-half'else cx-21
            c.line(xx,y,xx,y+76)

start('Halves: Two Equal Parts',1)
lines(['Parent guide',
       'Try one activity for 5-10 minutes. Your child should count to 10.',
       'Read the instructions aloud. Spoken answers are welcome.',
       'You need a pencil. No scissors, ruler or real counters needed.'],714,12)
text(42,593,'Model a half of a shape',17,True)
lines(['A whole shape is split into two equal-sized parts.',
       'Each part is one half of the whole. Both parts together',
       'make the whole shape.'],562,13)
shape(185,400,'rect-half')
text(136,381,'one half',11);text(198,381,'one half',11)
text(42,332,'Model a half of a group',17,True)
lines(['There are 4 counters. Share them into 2 equal groups.',
       'Each group has 2 counters. Each group is half of the 4.'],301,13)
c.rect(85,207,170,51);dots(144,232,2)
c.rect(300,207,170,51);dots(359,232,2)
text(124,186,'one half: 2',11);text(339,186,'one half: 2',11)
lines(['Check both rules: two parts or groups, and equal size or number.',
       'Two unequal parts are not halves. Nothing is left out.',
       'Print pages 2-3 on A4 in black and white. Answers: page 4.'],124,11)
c.showPage()

start('1. Are these halves?',2)
lines(['Each picture shows a whole shape with dividing lines.',
       'Does it show TWO EQUAL parts? Circle Yes or No.',
       'An adult can read the questions and record spoken answers.'],714,12)
data=[('A','rect-half'),('B','rect-unequal'),('C','diagonal'),('D','circle-half'),('E','circle-unequal'),('F','thirds')]
for i,(label,kind)in enumerate(data):
    col=i%2;row=i//2;x=42+col*268;y=520-row*181
    text(x,y+89,label,16,True);shape(x+118,y,kind)
    text(x+57,y-30,'Yes / No',14,True)
lines(['Talk: Why is making just two parts not always enough?'],94,12)
c.showPage()

start('2. Share into two equal groups',3)
lines(['Each circle is one counter. Draw the counters in the two boxes.',
       'Put the SAME number in each box. Use every counter once.',
       'Do not add any extra counters. An adult can draw for you.'],714,12)
for i,n in enumerate((6,8,10)):
    y=590-i*180
    text(42,y+42,f'{i+1}. Share {n} counters.',15,True)
    dots(280,y+47,n,24)
    c.rect(58,y-23,204,49);c.rect(304,y-23,204,49)
    text(71,y-51,'Half of '+str(n)+' is ______ counters.',13)
lines(['Check: count the two groups together. Is the total unchanged?',
       'Explain: how do you know both groups are halves?'],91,11)
c.showPage()

start('Answers and next steps',4)
text(42,710,'Page 2: Are these halves?',17,True)
lines(['A: Yes. The rectangle has two equal-sized parts.',
       'B: No. There are two parts, but they are unequal.',
       'C: Yes. The square has two equal-sized triangular parts.',
       'D: Yes. The circle has two equal-sized parts.',
       'E: No. The two parts of the circle are unequal.',
       'F: No. There are three equal parts, not two.',
       'Talk: two parts must also be equal-sized to be halves.'],678,12)
text(42,480,'Page 3: Share into two equal groups',17,True)
lines(['1. Put 3 counters in each box. Half of 6 is 3.',
       '2. Put 4 counters in each box. Half of 8 is 4.',
       '3. Put 5 counters in each box. Half of 10 is 5.',
       'The positions of the counters in each box can vary.',
       'Check the totals: 3 + 3 = 6; 4 + 4 = 8; 5 + 5 = 10.',
       'Example explanation: there are two groups with the same',
       'number in each, and every counter is included.'],448,12)
text(42,248,'Support and stretch',17,True)
lines(['If needed, model 4 drawn counters shared as 2 and 2 first.',
       'Take turns pointing to each group as you count.',
       'Optional: ask your child to draw 8 counters in a new arrangement',
       'and share them into halves again. Each half still has 4.',
       'There is no timed target. Revisit one idea at a time.'],216,12)
c.showPage();c.save()
print(OUT);print('sha256',hashlib.sha256(OUT.read_bytes()).hexdigest())
