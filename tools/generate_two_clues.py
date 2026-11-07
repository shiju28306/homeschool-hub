from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets/Kids-Listen-to-Two-Clues-Pack.pdf'
pdfmetrics.registerFont(TTFont('Pack', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PackBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('Listen to Two Clues | Homeschool Hub')
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
    text(42, 28, 'Listen to Two Clues | Ages about 4-6 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


def object_picture(name, x, y):
    c.setLineWidth(2)
    if name == 'cup':
        c.rect(x - 30, y - 25, 60, 60)
        c.ellipse(x + 30, y - 10, x + 53, y + 23)
        c.line(x - 39, y - 31, x + 44, y - 31)
    elif name == 'hat':
        c.ellipse(x - 60, y - 20, x + 60, y + 2)
        c.rect(x - 33, y - 8, 66, 47, fill=1, stroke=0)
        c.setFillColorRGB(1, 1, 1)
        c.rect(x - 31, y - 6, 62, 43, fill=1, stroke=0)
        c.setFillColorRGB(0, 0, 0)
        c.line(x - 31, y + 3, x + 31, y + 3)
    elif name == 'ball':
        c.circle(x, y, 41)
        seam = c.beginPath()
        seam.moveTo(x, y - 41)
        seam.curveTo(x - 28, y - 12, x - 28, y + 12, x, y + 41)
        seam.moveTo(x, y - 41)
        seam.curveTo(x + 28, y - 12, x + 28, y + 12, x, y + 41)
        c.drawPath(seam)
    elif name == 'book':
        c.rect(x - 42, y - 37, 84, 74)
        c.line(x - 31, y - 37, x - 31, y + 37)
        c.rect(x - 16, y - 2, 44, 22)
        for offset in (0, 5, 10):
            c.line(x - 28, y - 28 + offset, x + 34, y - 28 + offset)
    elif name == 'spoon':
        c.ellipse(x - 17, y + 6, x + 17, y + 49)
        c.roundRect(x - 5, y - 48, 10, 54, 4)
    elif name == 'key':
        c.circle(x - 27, y + 21, 20)
        c.circle(x - 27, y + 21, 9)
        c.rect(x - 10, y + 15, 63, 12)
        c.rect(x + 28, y, 10, 15)
        c.rect(x + 43, y + 5, 10, 10)


start('Listen to Two Clues', 1)
text(42, 710, 'Parent guide', 17, True)
lines(['A short listening and describing game for ages about 4-6.',
       'Your child listens to two clues, then points to a matching picture.',
       'No reading, writing or cutting is needed. Try 5-10 minutes.',
       'An adult reads aloud. Print page 2 for your child; keep page 3',
       'for yourself. The guide and answers can stay on your screen.'], 680)
text(42, 530, 'Before you begin', 17, True)
lines(['Name all six pictures together: cup, hat, ball, book, spoon, key.',
       'Explain any unfamiliar object. These are pictures, not real objects.',
       'Use the picture names throughout so the game tests listening.',
       'Say both clues slowly. Repeat them whenever your child asks.'], 500)
text(42, 377, 'Model one together', 17, True)
lines(['Say: "I am round. You can roll me. Which picture am I?"',
       'Point to the ball. Say: "The ball fits both clues."',
       'Now use the six new clue pairs on page 3 in the order shown.',
       'Ask: "What helped you choose?" Accept pointing or spoken words.'], 347)
text(42, 225, 'Keep it comfortable', 17, True)
lines(['If six choices feel too much, cover a row or offer two pictures.',
       'Always keep the matching picture visible. Give thinking time.',
       'Read one clue at a time, then repeat both. Stop when needed.',
       'There is no score or timed target. Answers are on page 4.'], 195)
c.showPage()

start('Which object? Point and tell', 2)
lines(['Look at the six pictures. Listen to both clues your adult reads.',
       'Point to the picture that fits. Tell or show what helped you.'], 714)
objects = ['cup', 'hat', 'ball', 'book', 'spoon', 'key']
for i, name in enumerate(objects):
    x = 42 + (i % 2) * 268
    y = 479 - (i // 2) * 181
    c.roundRect(x, y, 242, 158, 8)
    object_picture(name, x + 121, y + 88)
    c.setFont('PackBold', 14)
    c.drawCentredString(x + 121, y + 18, name)
c.showPage()

start('Read aloud: two clues', 3)
lines(['Adult page: keep this beside you while your child uses page 2.',
       'Read both clues, then ask "Which picture am I?"',
       'Repeat as needed. These questions are not a memory test.'], 714)
clues = [
    ('I have pages.', 'You can open me to look at a story.'),
    ('You wear me on your head.', 'In this picture, I have a brim.'),
    ('You can put a drink inside me.', 'My curved handle is on one side.'),
    ('I fit in a lock.', 'You can turn me to unlock it.'),
    ('I have a long handle and a small bowl.', 'You can use me to eat soup.'),
    ('You can roll me.', 'You can throw me in a game.'),
]
for i, pair in enumerate(clues):
    y = 600 - i * 79
    text(42, y, f'{i + 1}. {pair[0]}', 13, True)
    text(63, y - 25, pair[1], 13)
lines(['After a choice, ask: "Does that picture fit both clues?"',
       'Accept an everyday word for the object, such as mug for cup.'], 100, 11)
c.showPage()

start('Answers and next steps', 4)
text(42, 710, 'Answers for page 3', 17, True)
answers = [
    '1. Book: it has pages and can hold a story.',
    '2. Hat: it is worn on the head; this hat has a brim.',
    '3. Cup: it can hold a drink and has a curved side handle.',
    '4. Key: it fits in a lock and can turn to unlock it.',
    '5. Spoon: its small bowl and handle help you eat soup.',
    '6. Ball: it can be rolled and thrown in a game.',
]
lines(answers, 677, 13)
text(42, 500, 'Listen to the explanation', 17, True)
lines(['An example: "I chose the book because it has pages."',
       'Naming one useful clue is a good start. Repeat the second',
       'and check it together. A gesture or pointing is welcome.',
       'The expected answers refer to the six pictured objects.'], 469)
text(42, 341, 'If your child chooses another picture', 17, True)
lines(['Ask what they noticed. Check both clues together without rushing.',
       'For example, the spoon has a handle, but its handle is long',
       'and straight. The cup has a curved handle on its side.',
       'Clarify unfamiliar vocabulary, then try the pair again.'], 310)
text(42, 183, 'Optional next step', 17, True)
lines(['Let your child choose a picture and make two clues for you.',
       'Model a clear pair if needed. Many different clues can work.',
       'Keep all pictures available and welcome their own words.'], 152)
c.showPage()
c.save()
print(OUTPUT)
