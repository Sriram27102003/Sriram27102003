import math, os
import os
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
PAPER="#F3F0E9"; PAPER2="#EAE5DC"; INK="#1C1F1D"; SAGE="#476556"; DSAGE="#2E4238"; AMBER="#E0A526"; MUTED="#77736A"; LINE="#DCD6CA"; CHIP="#E6E1D7"
SERIF="Georgia, 'Times New Roman', serif"
MONO="ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"

def corners(x,y,w,h,l=14,color=AMBER,sw=2.5,cls=""):
    p=[f"M{x},{y+l} V{y} H{x+l}", f"M{x+w-l},{y} H{x+w} V{y+l}",
       f"M{x+w},{y+h-l} V{y+h} H{x+w-l}", f"M{x+l},{y+h} H{x} V{y+h-l}"]
    return f'<path class="{cls}" d="{" ".join(p)}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="square"/>'

# ---------- face landmarks ----------
def face_points(cx, cy, s):
    pts=[]; segs=[]
    def add(seq, closed=False):
        i0=len(pts); pts.extend(seq)
        idx=list(range(i0,len(pts)))
        for a,b in zip(idx, idx[1:]): segs.append((a,b))
        if closed: segs.append((idx[-1],idx[0]))
    jaw=[(cx+ s*0.92*math.cos(t), cy+ s*1.05*math.sin(t)) for t in [math.pi*(k/16) for k in range(0,17)]]
    jaw=[(cx+s*0.95*math.cos(math.radians(a)), cy-s*0.15+s*1.15*math.sin(math.radians(a))) for a in range(-5,186,12)]
    add(jaw)
    for side in (-1,1):
        brow=[(cx+side*s*(0.18+0.12*k), cy-s*0.42 - s*0.08*math.sin(math.pi*k/4)) for k in range(5)]
        add(brow)
        ex=cx+side*s*0.38; ey=cy-s*0.22
        eye=[(ex+s*0.17*math.cos(math.radians(a)), ey+s*0.07*math.sin(math.radians(a))) for a in range(0,360,60)]
        add(eye, True)
    nose=[(cx, cy-s*0.2+s*0.09*k) for k in range(4)]; add(nose)
    base=[(cx+s*0.07*k, cy+s*0.18+ s*0.03*abs(k)*-0.6) for k in range(-2,3)]; add(base)
    mouth=[(cx+s*0.3*math.cos(math.radians(a)), cy+s*0.5+s*0.11*math.sin(math.radians(a))) for a in range(0,360,30)]
    add(mouth, True)
    return pts, segs

def header():
    W,H=900,380
    fx,fy,fw,fh=628,52,236,262
    pts,segs=face_points(fx+fw/2, fy+fh/2+14, 86)
    mesh="".join(f'<line x1="{pts[a][0]:.1f}" y1="{pts[a][1]:.1f}" x2="{pts[b][0]:.1f}" y2="{pts[b][1]:.1f}"/>' for a,b in segs)
    dots="".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.1" style="animation-delay:{(i%9)*0.12:.2f}s"/>' for i,(x,y) in enumerate(pts))
    bx,by,bw,bh = fx+26, fy+36, fw-52, fh-52
    log=[("$","detect --subject sriram"),
         ("role","Software Developer @ AJSolutions"),
         ("venture","Co-builder, Snaptrace (Unit3A)"),
         ("edu","B.Tech CSE, AI &amp; Robotics, VIT Chennai"),
         ("base","Bangalore &amp; Chennai, India")]
    loglines=""
    for i,(k,v) in enumerate(log):
        y=250+i*22
        if k=="$":
            loglines+=f'<text x="40" y="{y}" class="mono" fill="{SAGE}">› <tspan fill="{INK}">{v}</tspan></text>'
        else:
            loglines+=f'<text x="40" y="{y}" class="mono line" style="animation-delay:{0.9+i*0.25:.2f}s"><tspan fill="{MUTED}">{k.ljust(8)}</tspan><tspan fill="{INK}" dx="6">{v}</tspan></text>'
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="S Sriram, software developer. Full-stack and applied AI.">
<style>
.mono{{font-family:{MONO};font-size:13px;white-space:pre}}
.serif{{font-family:{SERIF}}}
.af{{transform-origin:176px 132px;animation:snap 1.1s cubic-bezier(.2,.9,.3,1.2) .2s both}}
@keyframes snap{{0%{{opacity:0;transform:scale(1.35)}}60%{{opacity:1}}100%{{opacity:1;transform:scale(1)}}}}
.tag{{animation:fade .4s ease 1.2s both}}
.line{{animation:fade .5s ease both}}
@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
.scan{{animation:scan 3.2s ease-in-out infinite alternate}}
@keyframes scan{{from{{transform:translateY(0)}}to{{transform:translateY({bh-2}px)}}}}
.dots circle{{animation:blink 2.4s ease-in-out infinite}}
@keyframes blink{{0%,100%{{opacity:.95}}50%{{opacity:.35}}}}
.rec{{animation:rec 1.6s steps(1) infinite}}
@keyframes rec{{50%{{opacity:.15}}}}
.cursor{{animation:rec 1.1s steps(1) infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="{PAPER}" stroke="{LINE}" stroke-width="1.5"/>
{corners(14,14,W-28,H-28,l=22,color=INK,sw=1.5)}
<circle class="rec" cx="42" cy="44" r="4.5" fill="#C2402F"/>
<text x="54" y="48" class="mono" font-size="12" fill="{MUTED}">cam_01  /  github.com/Sriram27102003</text>

<text x="40" y="154" class="serif" font-size="68" fill="{INK}" letter-spacing="-1">S Sriram</text>
<g class="af">{corners(24,88,304,88,l=16)}</g>
<g class="tag"><rect x="24" y="66" width="112" height="20" fill="{AMBER}"/>
<text x="31" y="80" class="mono" font-size="11.5" fill="{INK}">subject  0.98</text></g>
<text x="40" y="206" class="serif" font-size="19" font-style="italic" fill="{SAGE}">Software developer shipping full-stack products and applied AI.</text>
{loglines}
<rect class="cursor" x="{246}" y="{238}" width="8" height="15" fill="{SAGE}"/>

<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="10" fill="{DSAGE}"/>
<g stroke="{PAPER}" stroke-opacity=".28" stroke-width="1">{mesh}</g>
<g class="dots" fill="{PAPER}">{dots}</g>
<clipPath id="fc"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}"/></clipPath>
<g clip-path="url(#fc)"><g class="scan"><rect x="{bx}" y="{by}" width="{bw}" height="2" fill="{AMBER}"/><rect x="{bx}" y="{by-26}" width="{bw}" height="26" fill="{AMBER}" opacity=".12"/></g></g>
{corners(bx,by,bw,bh,l=16)}
<text x="{fx+14}" y="{fy+22}" class="mono" font-size="11" fill="{PAPER}" opacity=".8">face.match  0.98</text>
<circle cx="{fx+2}" cy="{fy+fh+34}" r="5" fill="{SAGE}"><animate attributeName="r" values="5;8;5" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.4;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="{fx+16}" y="{fy+fh+38}" class="mono" font-size="12" fill="{INK}">Open to SDE &amp; AI/ML roles</text>
</svg>'''
    open(f"{OUT}/header.svg","w").write(svg)

def banner(name, title, note):
    W,H=900,70
    tw=len(title)*15.5+30
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}">
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="{PAPER}" stroke="{LINE}" stroke-width="1.5"/>
{corners(16,12,tw,H-24,l=10,sw=2)}
<text x="{16+15}" y="{H/2+9}" font-family="{SERIF}" font-size="26" fill="{INK}">{title}</text>
<line x1="{16+tw+18}" y1="{H/2}" x2="{W-40-len(note)*7.3}" y2="{H/2}" stroke="{SAGE}" stroke-opacity=".45" stroke-dasharray="2 5"/>
<text x="{W-24}" y="{H/2+4.5}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{MUTED}">{note}</text>
</svg>'''
    open(f"{OUT}/{name}.svg","w").write(svg)

def stack():
    groups=[("Languages",['JavaScript (ES6+)','Python','Java','SQL','Dart','HTML5','CSS3']),
      ("Frontend & mobile",['React','Next.js','Vite','Flutter','Responsive UI','Design systems']),
      ("Backend & data",['Node.js','Express.js','REST APIs','Supabase','PostgreSQL','MySQL','MongoDB','Firebase']),
      ("Cloud & DevOps",['Hostinger VPS','AWS Rekognition','Cloudflare R2','Microsoft Azure','Git & GitHub','Linux CLI','Razorpay API']),
      ("AI & ML",['face-api.js','TensorFlow','PyTorch','Keras','Scikit-learn','OpenCV','YOLO','NumPy','Pandas']),
      ("Robotics & hardware",['eSSL biometrics','ROS','Deep SORT','Raspberry Pi','Arduino','Sensor interfacing'])]
    W=900; x0=210; right=W-28; cw=7.25; ch=26; gap=8
    rows=""; y=34
    for gi,(g,items) in enumerate(groups):
        x=x0; ytop=y
        chips=""
        for it in items:
            w=len(it)*cw+22
            if x+w>right: x=x0; y+=ch+gap
            chips+=f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{ch}" rx="4" fill="{CHIP}"/><text x="{x+11:.1f}" y="{y+17}" font-family="{MONO}" font-size="12" fill="{INK}">{it.replace("&","&amp;")}</text>'
            x+=w+gap
        rows+=f'<text x="36" y="{ytop+18}" font-family="{SERIF}" font-size="16" fill="{SAGE}">{g.replace("&","&amp;")}</text>'+chips
        y+=ch+gap
        if gi<len(groups)-1:
            rows+=f'<line x1="36" y1="{y+6}" x2="{W-28}" y2="{y+6}" stroke="{LINE}"/>'; y+=20
    H=y+22
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Tech stack">
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{PAPER}" stroke="{LINE}" stroke-width="1.5"/>
{rows}
</svg>'''
    open(f"{OUT}/stack.svg","w").write(svg)

def footer():
    W,H=900,96
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Open to full-time roles">
<style>@media (prefers-reduced-motion:reduce){{animate{{display:none}}}}</style>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{DSAGE}"/>
{corners(14,12,W-28,H-24,l=14,sw=2)}
<circle cx="46" cy="{H/2}" r="6" fill="{AMBER}"><animate attributeName="opacity" values="1;.25;1" dur="1.8s" repeatCount="indefinite"/></circle>
<text x="66" y="{H/2-4}" font-family="{SERIF}" font-size="21" fill="{PAPER}">Open to full-time SDE, full-stack and AI/ML roles.</text>
<text x="66" y="{H/2+18}" font-family="{MONO}" font-size="12" fill="{PAPER}" opacity=".7">Bangalore, Chennai or remote  ·  winsriram962@gmail.com</text>
</svg>'''
    open(f"{OUT}/footer.svg","w").write(svg)

header()
banner("sec-experience","Experience","3 roles, 2025 → now")
banner("sec-projects","Selected work","6 projects")
banner("sec-stack","Stack","6 groups, 43 tools")
banner("sec-activity","Activity","rebuilt daily from the GitHub API")
stack(); footer()
print("ok")
