import sys, base64, io, json
from PIL import Image
src, tpl, out = sys.argv[1], sys.argv[2], sys.argv[3]
def jpg(name, w, q=76):
    im = Image.open(f"{src}/{name}").convert("RGB")
    if im.width > w: im = im.resize((w, round(im.height*w/im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()
def png(name, w):
    im = Image.open(f"{src}/{name}").convert("RGBA")
    im = im.resize((w, round(im.height*w/im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()
m = {"portre": jpg("kurucu-portre-3.jpg", 1000, 80), "mor": jpg("sahne-piyano-mor-elbise.jpg", 675),
     "beyaz": jpg("sahne-piyano-beyaz-elbise.jpg", 675), "erkek": jpg("sahne-piyano-erkek-ogrenci.jpg", 675),
     "genis": jpg("sahne-piyano-genis.jpg", 675), "toplu": jpg("konser-Toplu-Fotograf.jpg", 896),
     "kons": jpg("konservatuvar-hazirlik-sahne-piyano.jpg", 1000), "ders": jpg("ders-piyano-pencere.jpg", 1000),
     "logo": png("erendemir-logo-beyaz-1200.png", 600)}
h = open(tpl, encoding="utf-8").read()
assert h.count("{{IMG}}") == 1
h = h.replace("{{IMG}}", json.dumps(m))
open(out, "w", encoding="utf-8").write(h); print(len(h)//1024, "KB")
