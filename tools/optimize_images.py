"""Optimise les images du site — à exécuter UNE fois sur des originaux (réencode à chaque passage). Usage : python3 tools/optimize_images.py"""
import glob, os
from PIL import Image

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'img')
MAXW = 1000

def jpg(p):
    im = Image.open(p)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    im.save(p, 'JPEG', quality=72, optimize=True, progressive=True)

def png(p, maxw=None):
    im = Image.open(p).convert('RGBA')
    if maxw and im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.quantize(256, method=Image.Quantize.FASTOCTREE).save(p, 'PNG', optimize=True)

for p in glob.glob(os.path.join(D, '*.jpg')):
    if not p.endswith('-m.jpg'):
        jpg(p)
# Logo d'en-tête : affiché à 191 px max → 400 px suffit pour les écrans 2x
png(os.path.join(D, 'ssig-logo.png'), 400)
png(os.path.join(D, 'apvg-logo.png'), 520)
for p in glob.glob(os.path.join(D, '*.png')):
    if os.path.basename(p) not in ('ssig-logo.png', 'apvg-logo.png') and os.path.getsize(p) > 60_000:
        png(p)
# Bannière mobile
b = Image.open(os.path.join(D, 'banniere-accueil.jpg'))
b.resize((800, round(b.height * 800 / b.width)), Image.LANCZOS).save(os.path.join(D, 'banniere-accueil-m.jpg'), 'JPEG', quality=76, optimize=True, progressive=True)
