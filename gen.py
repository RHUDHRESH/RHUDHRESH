"""Generate the RR-26 datasheet-style SVGs for the GitHub profile README.

Run:  uv run --no-project python gen.py      (writes ./assets/*.svg)
Each asset comes in a light and a dark variant; the README picks one with <picture>.
"""
from pathlib import Path
from textwrap import wrap
from xml.sax.saxutils import escape as x

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

THEMES = {
    "light": dict(bg="#FFFFFF", paper="#F5F6F3", ink="#15191B", muted="#5A6266", rule="#D5D9D6",
                  copper="#A9561F", copper_soft="#F3E4D8", mask="#1E5B45", mask_soft="#DCEBE3"),
    "dark": dict(bg="#0D1117", paper="#11171A", ink="#E7EBE8", muted="#9AA4A0", rule="#2B3533",
                 copper="#E0915A", copper_soft="#2E2016", mask="#6FC59E", mask_soft="#173328"),
}
SANS = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
DISPLAY = "'Segoe UI Black', 'Arial Black', 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, 'SFMono-Regular', Consolas, 'Liberation Mono', monospace"
MOTION_OFF = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def header(t):
    W, H = 1200, 340
    pins = [("P1", "ABB Accelerator Hackathon 2026", "3rd", "of 1,600+ teams · ₹1,00,000"),
            ("P2", "SEMICON India 2026 finale", "Top 5", "Applied Materials · New Delhi"),
            ("P3", "Competition builds in 2026", "19", "SIH · KONE · Mitsubishi · Freshworks")]
    rows = []
    for i, (n, k, v, sub) in enumerate(pins):
        y = 92 + i * 66
        rows.append(f'''
  <g class="pin" style="animation-delay:{0.25 + i * 0.15:.2f}s">
    <text x="808" y="{y}" class="mono" font-size="11" fill="{t['muted']}">{n}</text>
    <text x="838" y="{y}" font-family="{SANS}" font-size="14.5" fill="{t['ink']}">{x(k)}</text>
    <text x="838" y="{y + 19}" class="mono" font-size="11.5" fill="{t['muted']}">{x(sub)}</text>
    <text x="1162" y="{y + 10}" text-anchor="end" font-family="{DISPLAY}" font-weight="900" font-size="30" fill="{t['copper'] if i == 0 else t['ink']}">{x(v)}</text>
    {'' if i == 2 else f'<line x1="808" y1="{y + 38}" x2="1162" y2="{y + 38}" stroke="{t["rule"]}" stroke-dasharray="3 4"/>'}
  </g>''')
    trace = "M0 312 H210 L238 290 H520 L548 312 H760 L784 300 H1200"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Rhudhresh R — builder datasheet">
<style>
  .mono{{font-family:{MONO};letter-spacing:.06em}}
  .trace{{stroke-dasharray:1400;stroke-dashoffset:1400;animation:draw 2.4s ease-out .2s forwards}}
  .pin{{opacity:0;animation:fade .6s ease-out forwards}}
  .dot{{animation:blink 2.2s ease-in-out infinite}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  @keyframes fade{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
  @keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
  {MOTION_OFF}
  @media (prefers-reduced-motion: reduce){{.trace{{stroke-dashoffset:0}}.pin{{opacity:1}}}}
</style>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" fill="{t['bg']}" stroke="{t['rule']}"/>
<rect x="1" y="1" width="{W - 2}" height="34" fill="{t['paper']}"/>
<line x1="0" y1="35" x2="{W}" y2="35" stroke="{t['rule']}"/>
<text x="28" y="23" class="mono" font-size="12" fill="{t['muted']}"><tspan fill="{t['ink']}" font-weight="700">RR-26</tspan>  ·  BUILDER DATASHEET</text>
<text x="{W - 28}" y="23" text-anchor="end" class="mono" font-size="12" fill="{t['muted']}">REV 2026-11  ·  CHENNAI, IN  ·  github.com/RHUDHRESH</text>

<text x="28" y="78" class="mono" font-size="12" fill="{t['muted']}">FINAL-YEAR EEE · SAVEETHA ENGINEERING COLLEGE</text>
<text x="24" y="170" font-family="{DISPLAY}" font-weight="900" font-size="88" letter-spacing="-1.5" fill="{t['ink']}">Rhudhresh R<tspan fill="{t['copper']}" class="dot">.</tspan></text>
<text x="28" y="214" font-family="{SANS}" font-weight="600" font-size="25" fill="{t['ink']}">AI agents and engineering tools that show their work.</text>
<text x="28" y="246" font-family="{SANS}" font-size="16" fill="{t['muted']}">Agents that act under rules · physics-first models · evidence a judge can rerun.</text>

<line x1="784" y1="52" x2="784" y2="262" stroke="{t['rule']}"/>
{''.join(rows)}

<path class="trace" d="{trace}" fill="none" stroke="{t['copper']}" stroke-width="2.5"/>
<g fill="{t['bg']}" stroke="{t['copper']}" stroke-width="2.5">
  <circle cx="238" cy="290" r="5"/><circle cx="548" cy="312" r="5"/><circle cx="784" cy="300" r="5"/>
</g>
<circle r="4.5" fill="{t['copper']}">
  <animateMotion dur="5s" begin="2.6s" repeatCount="indefinite" path="{trace}"/>
</circle>
</svg>'''


CARDS = [
    ("contextrail", "ContextRail", "Freshworks Great Agent Hackathon", False,
     "One spoken sentence becomes a Freshservice ticket, a policy-checked plan, a Slack approval and an audit record.",
     "Sarvam voice EN · HI · TA  ·  live tickets #123–#128"),
    ("LatticeRank", "LatticeRank", "SEMICON India 2026 · Top 5", True,
     "Finds a 1 nm/px wafer reference inside a 10 nm/px SEM search image, on CPU only, for Applied Materials' Drift-Sense.",
     "Grand finale · Yashobhoomi, New Delhi"),
    ("FlowLens", "FlowLens", "KONE Elevate'26 · PS13", False,
     "Elevator fault isolation: finds the first causal deviation, ranks root causes with contradictions, abstains when unsure.",
     "evidence-first RCA · non-actuating next test"),
    ("Plantlens", "PlantLens", "Arduino Physical AI Challenge", False,
     "Read-only retrofit for factory machines: passive RS485, physics fingerprints and causal-graph fault explanations.",
     "runs on Arduino UNO Q · offline"),
    ("kasam", "KASAM", "iQOO Hackathon 2026", False,
     "The video that swears it's real. The screen writes a light code into a selfie video; a cut breaks its timing.",
     "live demo · rhudhresh.github.io/kasam"),
    ("range-2.0", "Range 2.0", "Indian EVs", False,
     "Will your EV make it? Physics traction, India-specific AC load and a learned residual, with conformal intervals.",
     "cars + two-wheelers · “why this number” waterfall"),
]


def card(t, name, chip, win, desc, proof):
    W, H = 580, 190
    lines = wrap(desc, 68)[:3]
    body = "".join(f'<text x="28" y="{86 + i * 21}" font-family="{SANS}" font-size="14.5" fill="{t["ink"]}">{x(l)}</text>' for i, l in enumerate(lines))
    chip_w = 14 + len(chip) * 7.1
    chip_fill, chip_ink = (t["mask_soft"], t["mask"]) if win else (t["paper"], t["muted"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{x(name)}: {x(desc)}">
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" fill="{t['bg']}" stroke="{t['copper'] if win else t['rule']}"/>
<rect x="1" y="1" width="4" height="{H - 2}" fill="{t['copper']}"/>
<text x="28" y="46" font-family="{DISPLAY}" font-weight="900" font-size="24" fill="{t['ink']}">{x(name)}</text>
<rect x="{W - 22 - chip_w}" y="27" width="{chip_w}" height="24" fill="{chip_fill}" stroke="{t['rule'] if not win else chip_fill}"/>
<text x="{W - 22 - chip_w / 2}" y="43" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{chip_ink}">{x(chip)}</text>
{body}
<rect x="22" y="{H - 42}" width="{W - 44}" height="26" fill="{t['copper_soft']}"/>
<text x="32" y="{H - 25}" font-family="{MONO}" font-size="12" fill="{t['ink']}">{x(proof)}</text>
</svg>'''


STACK = [("Languages", "Python · TypeScript · Rust · C++ · Verilog"),
         ("Agents & AI", "Claude · Groq · Sarvam · LangGraph · Ollama"),
         ("Backend", "FastAPI · Django Ninja · Axum · MCP"),
         ("Frontend", "React 19 · Next.js · Vite · WASM"),
         ("Data & infra", "Postgres/pgvector · Qdrant · FalkorDB · Docker · AWS · Vercel"),
         ("Hardware", "Arduino UNO Q · RS485 · KiCad · ngspice · Altium")]


def stack(t):
    W, row = 1200, 40
    H = 52 + row * len(STACK)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Tech stack">',
           f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" fill="{t["bg"]}" stroke="{t["rule"]}"/>',
           f'<rect x="1" y="1" width="{W - 2}" height="34" fill="{t["paper"]}"/>',
           f'<text x="28" y="23" font-family="{MONO}" font-size="12" letter-spacing=".06em" fill="{t["muted"]}">ELECTRICAL CHARACTERISTICS  ·  STACK BY LAYER</text>']
    for i, (k, v) in enumerate(STACK):
        y = 35 + row * i
        out.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{t["rule"]}"/>')
        out.append(f'<text x="28" y="{y + 26}" font-family="{MONO}" font-size="12.5" letter-spacing=".05em" fill="{t["copper"]}">{x(k.upper())}</text>')
        out.append(f'<text x="250" y="{y + 26}" font-family="{SANS}" font-size="16" fill="{t["ink"]}">{x(v)}</text>')
    out.append("</svg>")
    return "\n".join(out)


for mode, t in THEMES.items():
    (OUT / f"header-{mode}.svg").write_text(header(t), encoding="utf-8")
    (OUT / f"stack-{mode}.svg").write_text(stack(t), encoding="utf-8")
    for slug, name, chip, win, desc, proof in CARDS:
        (OUT / f"card-{slug.lower()}-{mode}.svg").write_text(card(t, name, chip, win, desc, proof), encoding="utf-8")
print("wrote", len(list(OUT.glob("*.svg"))), "svgs to", OUT)
