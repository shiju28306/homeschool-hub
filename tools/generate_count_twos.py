from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets/Kids-Count-in-Twos-Pack.pdf'
pdfmetrics.registerFont(TTFont('Pack', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PackBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('Count in Twos: Pairs to 20 | Homeschool Hub')
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
    text(42, 28, 'Count in Twos | Ages about 5-7 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


def pair(x, y):
    c.setLineWidth(1.4)
    c.roundRect(x, y - 12, 49, 28, 6)
    c.circle(x + 15, y + 2, 5)
    c.circle(x + 34, y + 2, 5)


start('Count in Twos: Pairs to 20', 1)
text(42, 711, 'Parent guide', 17, True)
lines(['Try 5-10 minutes with a child who can count objects to 20.',
       'An adult reads aloud. Your child can point and speak.',
       'A pencil is useful. An adult can record answers if needed.',
       'Print pages 2-3 on A4 in black and white. Answers are on page 4.'], 680)
text(42, 557, 'A pair means two', 17, True)
lines(['Each rounded box holds one pair of dots. Count all the dots,',
       'then touch each box once and say the running total in twos.'], 526)
for i in range(4):
    pair(65 + i * 125, 438)
    text(82 + i * 125, 402, str((i + 1) * 2), 17, True)
lines(['Say 2, 4, 6, 8 as you touch the four pairs.',
       'There are 4 pairs and 8 dots altogether.',
       'Each new pair adds 2 dots to the total.'], 354, 13)
text(42, 237, 'Support and next steps', 17, True)
lines(['Point to both dots in each box before counting in twos.',
       'If needed, count every dot in ones to check your total.',
       'Use fewer pairs first, then return to the larger groups.',
       'Repeat the model whenever needed. There is no timed target.',
       'The optional pattern questions can wait until page 2 feels easy.'], 206)
c.showPage()

start('1. Count the dots in twos', 2)
lines(['Touch each pair once. Say the total so far in twos.',
       'Write or say how many DOTS there are altogether.',
       'Check by counting every dot in ones if you wish.'], 714)
for i, pairs in enumerate((3, 5, 7, 10)):
    y = 600 - i * 139
    text(42, y + 28, f'{i + 1}.', 15, True)
    for j in range(pairs):
        pair(100 + (j % 5) * 90, y - (j // 5) * 39)
    text(100, y - 79, 'Total dots: __________', 13)
c.showPage()

start('2. Keep counting in twos', 3)
lines(['These patterns go up by 2 each time.',
       'Write or say the missing numbers. Read the whole pattern aloud.'], 714)
text(42, 636, 'A. Start at 2. Fill the empty boxes.', 15, True)
values = ['2', '4', '', '8', '', '12', '14', '', '18', '']
for i, value in enumerate(values):
    x = 47 + (i % 5) * 101
    y = 557 - (i // 5) * 82
    c.rect(x, y, 91, 55)
    c.setFont('PackBold', 20)
    c.drawCentredString(x + 45.5, y + 18, value)
lines(['Read across the top row, then across the bottom row.'], 441, 11)
text(42, 365, 'B. This time, start at 4.', 15, True)
text(55, 318, '4, 6, 8, ______, 12, ______', 20)
text(42, 238, 'C. Find and fix one mistake.', 15, True)
lines(['This pattern should go up by 2 each time.',
       'Which number needs changing? Say what it should be.'], 207)
text(55, 137, '2, 4, 7, 8, 10', 22, True)
c.showPage()

start('Answers and next steps', 4)
text(42, 711, 'Page 2', 17, True)
lines(['1. 3 pairs give 6 dots. Count 2, 4, 6.',
       '2. 5 pairs give 10 dots. Count 2, 4, 6, 8, 10.',
       '3. 7 pairs give 14 dots. Count 2, 4, 6, 8, 10, 12, 14.',
       '4. 10 pairs give 20 dots. Count 2, 4, 6, 8, 10,',
       '    12, 14, 16, 18, 20.'], 677, 13)
text(42, 520, 'Page 3', 17, True)
lines(['A. Missing numbers, in order: 6, 10, 16, 20.',
       '    Full pattern: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.',
       'B. Missing numbers: 10, 14.',
       '    Full pattern: 4, 6, 8, 10, 12, 14.',
       'C. Change 7 to 6. The pattern is 2, 4, 6, 8, 10.'], 486, 13)
text(42, 329, 'Talk together', 17, True)
lines(['Ask how the pair boxes helped your child keep track.',
       'Example answer: each box has two dots, so I add two each time.',
       'If your child gives the number of pairs instead of total dots,',
       'count the two dots inside each box together.'], 297)
text(42, 174, 'Optional practice', 17, True)
lines(['Draw 6 pair boxes with two dots in each. Ask for the total.',
       'There are 12 dots. The 6 counts the pairs; the 12 counts the dots.',
       'Accept spoken answers and revisit the pictures as needed.'], 142)
c.showPage()
c.save()
print(OUTPUT)
