from pathlib import Path
import hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/Kids-First-Next-Last-Stories-Pack.pdf'
pdfmetrics.registerFont(TTFont('Pack', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PackBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
c = canvas.Canvas(str(OUT), pagesize=A4, invariant=1)
c.setTitle('First, Next, Last: Tell a Three-Step Story | Homeschool Hub')
c.setAuthor('Homeschool Hub')
W,H = A4

def text(x,y,s,size=13,bold=False):
    c.setFont('PackBold' if bold else 'Pack', size)
    c.drawString(x,y,s)

def lines(items,y,size=13):
    for s in items:
        text(42,y,s,size)
        y-=23

def start(title,page):
    c.setLineWidth(1.2)
    text(42,H-40,'HOMESCHOOL HUB  /  FREE PRINTABLE',10,True)
    text(42,H-78,title,23,True)
    c.line(42,H-94,W-42,H-94)
    text(42,28,'First, Next, Last | Ages about 4-6 | Personal use',9)
    text(W-80,28,f'{page} / 4',9)

def pot(cx,y,stage):
    c.setLineWidth(1.7)
    p=c.beginPath();p.moveTo(cx-39,y+39);p.lineTo(cx-29,y-15)
    p.lineTo(cx+29,y-15);p.lineTo(cx+39,y+39);p.close()
    c.drawPath(p)
    c.rect(cx-44,y+39,88,11)
    if stage==0:
        c.line(cx-32,y+25,cx+32,y+25)
        c.ellipse(cx-5,y+12,cx+5,y+18,fill=0)
        text(cx-34,y+62,'Soil cutaway',9)
    else:
        top=y+(92 if stage==1 else 119)
        c.line(cx,y+50,cx,top)
        c.ellipse(cx-24,y+63,cx,y+75)
        c.ellipse(cx,y+76,cx+24,y+88)
        if stage==2:
            for dx,dy in [(0,18),(17,5),(10,-15),(-10,-15),(-17,5)]:
                c.circle(cx+dx,top+dy,10)
            c.setFillColorRGB(1,1,1);c.circle(cx,top,9,stroke=1,fill=1)
            c.setFillColorRGB(0,0,0)

def ice(cx,y,stage):
    c.setLineWidth(1.7)
    c.ellipse(cx-59,y-22,cx+59,y+9)
    if stage in (1,2):
        radius=32 if stage==1 else 47
        c.ellipse(cx-radius,y-11,cx+radius,y+3)
        c.line(cx-32,y-6,cx-15,y-6)
        c.line(cx+19,y-5,cx+34,y-5)
    if stage<2:
        z=47 if stage==0 else 24
        xx=cx-z/2;yy=y+1
        c.rect(xx,yy,z,z)
        p=c.beginPath();p.moveTo(xx,yy+z);p.lineTo(xx+12,yy+z+10)
        p.lineTo(xx+z+12,yy+z+10);p.lineTo(xx+z,yy+z)
        c.drawPath(p)
        c.line(xx+z,yy,xx+z+12,yy+10)
        c.line(xx+z+12,yy+10,xx+z+12,yy+z+10)
        c.line(cx-10,yy+z*.55,cx+1,yy+z*.75)

def gift(cx,y,stage):
    c.setLineWidth(1.7);c.rect(cx-39,y,78,60)
    if stage>=1:
        for dx,dy in [(-24,15),(19,13),(-18,44),(24,42)]:
            c.circle(cx+dx,y+dy,3)
    if stage==2:
        c.rect(cx-5,y,10,60);c.rect(cx-39,y+25,78,9)
        c.ellipse(cx-24,y+60,cx,y+77)
        c.ellipse(cx,y+60,cx+24,y+77)

def cards(y,items,kind):
    for i,(label,stage,caption) in enumerate(items):
        x=42+i*174;cx=x+81
        c.setLineWidth(1.2);c.roundRect(x,y,163,232,9)
        text(x+12,y+207,label,16,True)
        if kind=='plant':pot(cx,y+76,stage)
        elif kind=='ice':ice(cx,y+96,stage)
        else:gift(cx,y+99,stage)
        for j,s in enumerate(caption):text(x+10,y+42-j*18,s,11)

def response(y):
    lines(['Point to the pictures in story order. Say:',
           '"First ... Next ... Last ..."'],y,14)
    text(42,y-77,'Optional: an adult can write the picture letters.',12)
    text(42,y-110,'First: ______     Next: ______     Last: ______',14,True)

start('First, Next, Last',1)
lines(['Parent guide: tell a three-step story',
       'Try one story for 5-10 minutes. No child reading is needed.',
       'Read the captions aloud. Let your child point and talk.',
       'No cutting is needed. A pencil is optional for adult notes.'],714)
text(42,589,'Model together: getting a present ready',16,True)
lines(['In this story, we wrap a box and then add a ribbon.'],560,12)
cards(290,[('First',0,['We have a plain','box.']),('Next',1,['We wrap it in','spotty paper.']),('Last',2,['We add a ribbon','and a bow.'])],'gift')
lines(['Say the whole story, using first, next and last.',
       'Ask: "What changed?" Pause and give your child time.',
       'If needed, model the first part and let your child finish.',
       'Accept short phrases, pointing or different clear wording.'],242,12)
lines(['On pages 2-3 the pictures are mixed up. Read every caption.',
       'Do one story at a time. No speed or memory test is needed.',
       'Print pages 2-3 on A4 in black and white. Answers: page 4.'],116,11)
c.showPage()

start('1. From seed to flower',2)
lines(['These pictures show one flowering plant as it grows.',
       'An adult reads the captions. Put the story in order.'],714)
cards(398,[('A',2,['A flower opens on','the plant.']),('B',0,['A seed is planted','in the soil.']),('C',1,['A small shoot','grows above the soil.'])],'plant')
response(348)
text(42,181,'Talk together',17,True)
lines(['What changed between the first and last pictures?',
       'Tell the story again in your own words.',
       'These pictures skip some stages; growing takes time.'],149,12)
c.showPage()

start('2. The melting ice cube',3)
lines(['The same ice cube is left on a plate in a warm room.',
       'It melts completely. Put these pictures in story order.'],714)
cards(398,[('A',1,['Some ice has melted.','A smaller piece is left.']),('B',2,['All the ice has melted.','Only water is left.']),('C',0,['An ice cube is put','on the plate.'])],'ice')
response(348)
text(42,181,'Talk together',17,True)
lines(['What happened to the piece of ice?',
       'Tell the story again using first, next and last.',
       'This is a picture activity; no ice experiment is needed.'],149,12)
c.showPage()

start('Answers and next steps',4)
text(42,710,'Page 2: From seed to flower',17,True)
lines(['Picture order: B, C, A.',
       'First, a seed is planted in the soil.',
       'Next, a small shoot grows above the soil.',
       'Last, a flower opens on the plant.',
       'What changed? Example: a plant grew from the seed',
       'and later had a flower.'],678,12)
text(42,501,'Page 3: The melting ice cube',17,True)
lines(['Picture order: C, A, B.',
       'First, an ice cube is put on the plate.',
       'Next, some ice melts and a smaller piece is left.',
       'Last, all the ice has melted and only water is left.',
       'What happened? The ice melted into liquid water.'],469,12)
text(42,313,'Support a spoken story',17,True)
lines(['These are example sentences, not words to memorise.',
       'Accept different wording that keeps the events in order.',
       'If the order is unclear, reread the captions and compare',
       'two pictures together. Ask: "What has changed?"',
       'An adult may write the letters; letter knowledge is not tested.'],281,12)
lines(['Next step: retell a familiar short routine together,',
       'such as putting on socks, then shoes, then going outside.',
       'Choose a routine that fits your family. No recording is needed.'],126,11)
c.showPage()
c.save()
print(OUT)
print('sha256',hashlib.sha256(OUT.read_bytes()).hexdigest())
