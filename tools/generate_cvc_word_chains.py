from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
OUTPUT = ROOT / 'assets/Kids-CVC-Word-Chains-Pack.pdf'
pdfmetrics.registerFont(TTFont('Pack', str(FONT_DIR / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('PackBold', str(FONT_DIR / 'DejaVuSans-Bold.ttf')))
c = canvas.Canvas(str(OUTPUT), pagesize=A4, invariant=1)
c.setTitle('Change One Letter: CVC Word Chains | Homeschool Hub')
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
    text(42, 28, 'CVC Word Chains | Ages about 5-7 | Personal use', 9)
    text(W - 80, 28, f'{page} / 4', 9)


def boxes(x, y, word='   '):
    c.setFont('Pack', 24)
    for i, letter in enumerate(word):
        left = x + i * 43
        c.roundRect(left, y, 40, 39, 4)
        c.drawCentredString(left + 20, y + 11, letter)


def row(y, label, word='   '):
    text(42, y + 13, label, 12, True)
    boxes(390, y, word)


start('Change One Letter', 1)
text(42, 711, 'CVC word chains', 17, True)
lines(['Try 5-10 minutes with a child who can already blend simple',
       'three-letter words such as cat and dog.',
       'An adult reads the instructions. A pencil is useful.',
       'Print pages 2-3 on A4 in black and white. Keep page 4 handy.'], 680)
text(42, 548, 'Model: cat, cot, dot', 17, True)
boxes(42, 468, 'cat')
boxes(236, 468, 'cot')
boxes(430, 468, 'dot')
lines(['Point to c, a, t. Say each sound, then blend them to read cat.',
       'Change the middle letter a to o. Read cot. Keep c and t.',
       'Change the first letter c to d. Read dot. Keep o and t.',
       'Every new word changes just one letter from the word before it.'], 432)
text(42, 307, 'Work from the row above', 17, True)
lines(['Say which letter changes. Copy the other two into the same places.',
       'Say each sound and blend the new word. Point to the changed box.',
       'On page 2, the instruction gives the new letter.',
       'On page 3, say the target word aloud using the script on page 4.'], 276)
text(42, 153, 'Support', 17, True)
lines(['Stop after a few changes if needed. You can write for your child.',
       'Say letter sounds without adding an extra vowel sound.'], 122)
c.showPage()

start('1. Change the letter', 2)
lines(['Read the starter word. At each step, use the word just above.',
       'Change the letter in the named place. Keep the other two letters.',
       'Say the sounds and read the new word. Point to the box you changed.'], 714)
row(610, 'Start here', 'sat')
steps = ['Change the middle letter to i.', 'Change the last letter to p.',
         'Change the first letter to t.', 'Change the middle letter to a.',
         'Change the first letter to m.']
for i, instruction in enumerate(steps, 1):
    row(610 - 86 * i, f'{i}. {instruction}')
lines(['Try reading the whole chain from top to bottom.'], 96, 11)
c.showPage()

start('2. Listen and change a letter', 3)
lines(['Read the starter word. Listen to your adult say the next word.',
       'Change one letter in the word just above to make that word.',
       'Read your new word and point to the box you changed.'], 714)
row(610, 'Start here', 'dog')
for i in range(1, 5):
    row(610 - 94 * i, f'{i}. Listen, then write or say the new word.')
lines(['Adult: read one word at a time from the page 4 script.',
       'Repeat the word if asked. Write the letters if your child prefers to speak.'], 145, 11)
c.showPage()

start('Answers and parent script', 4)
text(42, 711, 'Page 2 answers', 17, True)
lines(['Start sat.',
       '1. sit. Middle a changes to i.',
       '2. sip. Last t changes to p.',
       '3. tip. First s changes to t.',
       '4. tap. Middle i changes to a.',
       '5. map. First t changes to m.'], 679, 13)
text(42, 504, 'Page 3 words to say', 17, True)
lines(['Start dog. Say the bold word for each numbered row.'], 475)
for i, (word, change) in enumerate([('dig', 'Middle o changes to i.'),
                                     ('pig', 'First d changes to p.'),
                                     ('pin', 'Last g changes to n.'),
                                     ('pan', 'Middle i changes to a.')], 1):
    y = 451 - i * 33
    text(42, y, f'{i}. {word}', 13, True)
    text(121, y, change, 13)
text(42, 268, 'If a word is tricky', 17, True)
lines(['Read the previous word together. Then say the new word slowly.',
       'Point to the box that changes. Ask which two letters stay.',
       'Give a meaning when needed. For example, sip means take a small drink.',
       'Optional: say pan, then pat. The last letter changes from n to t.'], 236)
c.showPage()
c.save()
print(OUTPUT)
