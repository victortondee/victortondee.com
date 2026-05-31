import re

SRC = '/home/user/victortondee.com/index.html'
OUT = '/home/user/victortondee.com/preview2/index.html'

# Pinned reading-order IDs (positions 1..N). Remaining items follow in source order.
pinned = [
    "67fb52032fbef7e18cf91334",  # 1  A02261
    "67f9f2ed832cdc06e48e02b2",  # 2  IMG_2040_2
    "67fb51fe286c19f6c0447abb",  # 3  2
    "67fb51fc7de0cd9c382952dd",  # 4  10
    "67fb51fef52442df000825d0",  # 5  c+A05537_mirrored
    "67fb51fd9a73c9d1d3164cda",  # 6  A03804_032209604
    "67fb51fcb4111978e8243136",  # 7  081703258
    "67fb51fe8fc388fc159a5545",  # 8  071702106+(bw)
    "67fb5200eb59624612b6ccc6",  # 9  dlt
    "67fb51fc0276e79ad6d7347f",  # 10 17_resized
    "67fb51fce1601bfa7ba8d91b",  # 11 13
    "67fb5200f233a60a03b00d0a",  # 12 a+A04020_mirrored_edited
    "67fb51fd7de0cd9c38295309",  # 13 1 (1)
    "67fb7d7e3af51c4fe9983be9",  # 14 A04170
    "67fb52005a584206e82b1269",  # 15 061807512_091808491_liquify
    "67fb51fd9daf8059744531c7",  # 16 7
    "67fb51fc286c19f6c04479bd",  # 17 0
    "67fb51fd499124434e8af5dd",  # 18 011805284_011805455_liquify
    "67fb520090d84f183a5102b1",  # 19 e+A03911_mirrored_v2+copy
    "67fb51fe5a584206e82b1163",  # 20 071701244_121809929+(I)
    "67fb51ffcad347c3931d4376",  # 21 36678
    "67fb51fd4e0bcefc2c2e4605",  # 22 16
    "67fb51fd1009eed541390e02",  # 23 be_now
    "67fb51fc711f1499326fdad5",  # 24 10
    "67fb51fe14dc5b7fe32f3d17",  # 25 A06309_mirrored_edited
    "67fb51fd91285205493a603e",  # 26 041806688_091808475_V2+(i)
    "67fb51fd8fc388fc159a54f8",  # 27 071904154_081904977
    "67fb51fe93824817822c965b",  # 28 071702005_111809547
    "67fb51fcefbb81d725969308",  # 29 8
    "67fb51fce897bdb3d6eb550e",  # 30 2
    "67fb51fccad347c3931d42b3",  # 31 1 (2)
    "67fb7fac91285205494fbce3",  # 32 A04154
    "67fb803bf233a60a03c7304f",  # 33 031806049_011805470_2
    "67fb56fb83fe906731577781",  # 34 IMG_8706_sand
    "67fb51fdcad347c3931d4307",  # 35 a+17234_mirrored
    "67fb51fe2abda3933caf4d22",  # 36 IMG_9970_shapes_edit
    "67fb520090d84f183a5101bd",  # 37 A04076
    "67fb8558e1601bfa7bc38f28",  # 38 28281
    "67fb51fea99339ceb58615d2",  # 39 h+20804+(mirrored)
    "67fb51fcdb493a47b84f8ee4",  # 40 4
    "67fb51fe7de0cd9c38295442",  # 41 f
    "67fb520057845eeb8b05674b",  # 42 A05623+(for+Sofi)
    "67fb89a2f52442df00250dc6",  # 43 bgdn2364(downsized)
    "67fb51fc92acf6bde6327dbc",  # 44 1
    "67fb51fd1009eed541390efc",  # 45 g+A03350_mirrored
    "67fb51fc8e1e98a169893203",  # 46 6
    "67fb51fc9daf805974453136",  # 47 3
    "67fb5200ee648dcac773bd8d",  # 48 051902503
    "67fb51fc2abda3933caf4b80",  # 49 8
    "67fb51fc4edb14179b2e7796",  # 50 bgdn2364
    "67fb51ff93824817822c9694",  # 51 A06248+A05933
    "67fb5200f52442df00082678",  # 52 A01873_mirrored
    "67fb51fe711f1499326fdb5a",  # 53 b+Screen
    "67fb5200d5dff2348d914784",  # 54 IMG_7516 (swap1: was 1)
    "67fb52010276e79ad6d73685",  # 55 A03714+A02981
    "67fb52032fbef7e18cf9133c",  # 56 21(2)
    "67fb51fcefbb81d7259692f4",  # 57 11
    "67fb51fea7124abc196053a3",  # 58 A03200
    "67fb51ff83fe90673155743c",  # 59 image-asset
    "67fb51ff4edb14179b2e7956",  # 60 image-asset(1) (swap3: was A03200)
    "67fb51fd499124434e8af5c7",  # 61 051807260
    "67fb51fe1746ed1633606b4c",  # 62 08
    "67fb51fc93824817822c948f",  # 63 31172
    "67fb51fffb163757cb9dedef",  # 64 d+071702165_mirrored
    "67fb5200f233a60a03b00d0d",  # 65 IMG_4265
]

CSS = """.w-webflow-badge { display: none !important; }.gallery .image{height:auto!important}
.gallery .columns{display:grid !important;grid-template-columns:repeat(3,1fr) !important;grid-auto-rows:1px !important;column-gap:16px !important;row-gap:0 !important;column-count:auto !important;-webkit-column-count:auto !important;}
@media screen and (max-width:991px){.gallery .columns{grid-template-columns:repeat(2,1fr) !important;}}
@media screen and (max-width:767px){.gallery .columns{grid-template-columns:1fr !important;}}
.gallery .masonry-item{width:auto !important;margin:0 !important;float:none !important;display:block !important;}
.gallery .image{width:100% !important;height:auto !important;display:block !important;}"""

JS_MASONRY = """<script>(function(){var UNIT=1,GAP=16;function colCount(){var w=window.innerWidth;if(w<=767)return 1;if(w<=991)return 2;return 3;}function layout(){var grid=document.querySelector('.gallery .columns');if(!grid)return;var items=grid.querySelectorAll('.masonry-item');var cols=colCount();var cursor=[];for(var c=0;c<cols;c++)cursor[c]=1;for(var i=0;i<items.length;i++){var it=items[i];var img=it.querySelector('.image');var h=img?img.getBoundingClientRect().height:0;if(!h)continue;var span=Math.ceil((h+GAP)/UNIT);var col=i%cols;it.style.gridColumnStart=String(col+1);it.style.gridRowStart=String(cursor[col]);it.style.gridRowEnd='span '+span;cursor[col]+=span;}}function s(){requestAnimationFrame(layout);}if(document.readyState!=='loading')s();else document.addEventListener('DOMContentLoaded',s);window.addEventListener('load',s);window.addEventListener('resize',s);document.querySelectorAll('.gallery .image').forEach(function(img){if(!img.complete)img.addEventListener('load',s);});[500,1500,3000].forEach(function(d){setTimeout(s,d);});})();</script>"""

JS_LAZY = """<script>(function(){var imgs=document.querySelectorAll('.gallery .masonry-item img[data-src]');if(!imgs.length)return;var io=new IntersectionObserver(function(entries){entries.forEach(function(e){if(!e.isIntersecting)return;var img=e.target;if(img.dataset.src){img.src=img.dataset.src;delete img.dataset.src;}if(img.dataset.srcset){img.srcset=img.dataset.srcset;delete img.dataset.srcset;}img.addEventListener('load',function(){window.dispatchEvent(new Event('resize'));},{once:true});io.unobserve(img);});},{rootMargin:'300px 0px'});imgs.forEach(function(img){io.observe(img);});})();</script>"""


def make_eager(item):
    item = re.sub(r'\bdata-src=', 'src=', item)
    item = re.sub(r'\bdata-srcset=', 'srcset=', item)
    item = re.sub(r'\bloading="lazy"', 'loading="eager"', item)
    if 'fetchpriority="high"' not in item:
        item = re.sub(r'(<img\b)', r'<img fetchpriority="high"', item)
    return item


def make_lazy(item):
    item = re.sub(r'\bsrc="https://', 'data-src="https://', item)
    item = re.sub(r'\bsrcset="https://', 'data-srcset="https://', item)
    item = re.sub(r'\bfetchpriority="high"\s*', '', item)
    item = re.sub(r'\bloading="eager"', 'loading="lazy"', item)
    return item


def main():
    with open(SRC) as f:
        src = f.read()

    items = re.findall(r'(<a[^>]*class="masonry-item[^"]*"[^>]*>.*?</a>)', src, re.DOTALL)
    assert len(items) == 65, f"expected 65 items, got {len(items)}"

    id_re = r'5ff19412fdd5f7521e1ac370/([a-f0-9]{24})_'
    ids = [re.search(id_re, it).group(1) for it in items]
    idx_by_id = {i: k for k, i in enumerate(ids)}

    for p in pinned:
        assert p in idx_by_id, f"pinned id not in source: {p}"

    pinned_set = set(pinned)
    order = [idx_by_id[p] for p in pinned]
    order += [k for k in range(65) if ids[k] not in pinned_set]
    assert len(order) == 65

    reordered = [make_eager(items[s]) if pos < 3 else make_lazy(items[s])
                 for pos, s in enumerate(order)]

    head = src[:src.find('</head>')]
    head = re.sub(r'<style>.*?</style>', f'<style>{CSS}\n</style>', head, count=1, flags=re.DOTALL)

    cols_marker = 'class="columns w-clearfix">'
    nav = src[src.find('<body'):src.find(cols_marker) + len(cols_marker)]
    nav = re.sub(r'href="/', 'href="https://www.victortondee.com/', nav)

    tail = re.search(r'</a></div></div>(<script.*?)</body>', src, re.DOTALL).group(1)
    tail = re.sub(r'<script>\(function\(\)\{var UNIT=1.*?</script>', '', tail, flags=re.DOTALL)
    tail = re.sub(r'<script>\(function\(\)\{var imgs=document.*?</script>', '', tail, flags=re.DOTALL)

    out = head + '</head>' + nav + ''.join(reordered) + '</div></div>' + tail + JS_MASONRY + JS_LAZY + '</body></html>'

    with open(OUT, 'w') as f:
        f.write(out)

    # report
    print(f"items: {len(reordered)}  pinned: {len(pinned)}")
    for pos, s in enumerate(order[:len(pinned)]):
        fn = re.search(r'5ff19412fdd5f7521e1ac370/[a-f0-9]{24}_([^"%.]+)', items[s])
        print(f"{pos+1:2d}. {fn.group(1) if fn else '?'}")


if __name__ == '__main__':
    main()
