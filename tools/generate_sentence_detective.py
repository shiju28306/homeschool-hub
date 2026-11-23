from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import fitz

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets/Kids-Sentence-Detective-Pack.pdf'
for name, filename in [('Pack', 'DejaVuSans.ttf'), ('PackBold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/' + filename))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('Sentence Detective: Capitals and Full Stops | Homeschool Hub')
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
    text(42, 28, 'Sentence Detective | Ages about 5-7 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


start('Sentence Detective', 1)
text(42, 712, 'Parent guide: capitals and full stops', 17, True)
lines(['Try 5-10 minutes with a child aged about 5-7.',
       'An adult can read every sentence aloud.',
       'Print pages 2-3 in black and white. Answers are on page 4.',
       'The child can point and speak while an adult writes.'], 680)
text(42, 555, 'Our two checks', 17, True)
lines(['These short sentences tell us something.',
       'Start each one with a capital letter.',
       'Finish each one with a full stop.'], 522, 14)
text(42, 416, 'Model: fix the beginning and the end', 17, True)
text(58, 369, 'Before:', 12, True)
text(160, 365, 'the cat naps', 22)
text(58, 312, 'After:', 12, True)
text(160, 308, 'The cat naps.', 22)
lines(['Change the first t to capital T. Put a full stop after naps.',
       'The words stay in the same order. Read the sentence together.'], 263)
text(42, 177, 'Say it, point to it, then check', 17, True)
lines(['Page 2: choose the sentence with both checks in place.',
       'Page 3: change the first letter and add the full stop.',
       'This is punctuation practice; an adult may help with reading.'], 144)
c.showPage()

start('1. Choose the sentence', 2)
lines(['Each sentence tells us something. Look at the start and the end.',
       'Say or circle A or B: which has a capital letter and a full stop?'], 712)
for number, y, a, b in [
    (1, 495, 'The dog sits.', 'the dog sits.'),
    (2, 320, 'A hen runs', 'A hen runs.'),
    (3, 145, 'We can hop.', 'we can hop.'),
]:
    c.setLineWidth(0.8)
    c.roundRect(42, y, 509, 145, 7)
    text(58, y + 113, str(number) + '.', 17, True)
    text(99, y + 87, 'A', 14, True)
    text(143, y + 87, a, 22)
    text(99, y + 37, 'B', 14, True)
    text(143, y + 37, b, 22)
text(42, 88, 'An adult can read both choices. Check the writing, not the voice.', 11)
c.showPage()

start('2. Fix the sentence', 3)
lines(['Change the first letter to a capital. Add a full stop at the end.',
       'Write the whole sentence, or tell an adult what to change.'], 712)
for number, y, sentence in [
    (1, 495, 'a pig digs'),
    (2, 320, 'the sun is hot'),
    (3, 145, 'we can run'),
]:
    c.setLineWidth(0.8)
    c.roundRect(42, y, 509, 145, 7)
    text(58, y + 111, str(number) + '.', 17, True)
    text(100, y + 108, sentence, 22)
    c.line(63, y + 45, 529, y + 45)
    text(64, y + 21, 'Capital at the start?   Full stop at the end?', 11)
text(42, 88, 'Keep the words in the same order. An adult may write your answer.', 11)
c.showPage()

start('Answers and parent prompts', 4)
text(42, 712, 'Page 2', 17, True)
lines(['1. A: The dog sits.',
       '    B starts with a lowercase t.',
       '2. B: A hen runs.',
       '    A has no full stop.',
       '3. A: We can hop.',
       '    B starts with a lowercase w.'], 679, 14)
text(42, 508, 'Page 3', 17, True)
lines(['1. A pig digs.',
       '2. The sun is hot.',
       '3. We can run.'], 475, 16)
text(42, 365, 'Use the two checks', 17, True)
lines(['Ask: Can you point to the capital at the start?',
       'Ask: Where is the full stop at the end?',
       'On page 3, accept spoken changes or an adult-written answer.',
       'Check both features before moving to the next sentence.'], 332)
text(42, 207, 'Support', 17, True)
lines(['Try one sentence at a time. Model the first change if needed.',
       'Read the words aloud so decoding does not hide the task.',
       'Other sentence types can have other ending marks;',
       'this pack practises short telling sentences with full stops.'], 174)
c.showPage()
c.save()
doc = fitz.open(OUTPUT)
doc[1].get_pixmap(matrix=fitz.Matrix(400 / W, 400 / W)).save(ROOT / 'assets/sentence-detective-preview.png')
print(OUTPUT)
