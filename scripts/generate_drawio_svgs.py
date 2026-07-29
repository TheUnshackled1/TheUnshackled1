import html
from pathlib import Path

DIAGRAMS_DIR = Path(__file__).parent.parent / "diagrams"
DIAGRAMS_DIR.mkdir(exist_ok=True)

def create_drawio_svg(filename: str, width: int, height: int, title: str, xml_content: str, svg_elements: str) -> Path:
    escaped_xml = html.escape(xml_content)
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="{width}px" height="{height}px" viewBox="-0.5 -0.5 {width} {height}" content="&lt;mxfile host=&quot;app.diagrams.net&quot;&gt;&lt;diagram name=&quot;{title}&quot;&gt;{escaped_xml}&lt;/diagram&gt;&lt;/mxfile&gt;">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&amp;display=swap');
      text {{ font-family: 'Inter', sans-serif; }}
    </style>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="100%" stop-color="#161b22" />
    </linearGradient>
    <linearGradient id="card-blue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1f6feb" />
      <stop offset="100%" stop-color="#1158c7" />
    </linearGradient>
    <linearGradient id="card-green" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636" />
      <stop offset="100%" stop-color="#196c2e" />
    </linearGradient>
    <linearGradient id="card-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8957e5" />
      <stop offset="100%" stop-color="#6e40c9" />
    </linearGradient>
    <linearGradient id="card-orange" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d29922" />
      <stop offset="100%" stop-color="#bb8009" />
    </linearGradient>
    <filter id="drop-shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="100%" height="100%" rx="12" fill="url(#bg-grad)" stroke="#30363d" stroke-width="1.5"/>

  {svg_elements}
</svg>"""

    filepath = DIAGRAMS_DIR / filename
    filepath.write_text(svg, encoding="utf-8")
    return filepath


# --- 1. CODE OF CONDUCT DIAGRAM ---
coc_xml = """<mxGraphModel dx="1000" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="800" pageHeight="500">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="Incident Occurs" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1f6feb;strokeColor=#388bfd;fontColor=#ffffff;fontWeight=bold;" vertex="1" parent="1">
      <mxGeometry x="40" y="40" width="160" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="Report to jtcoronel.chmsu@gmail.com" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#238636;strokeColor=#2ea043;fontColor=#ffffff;fontWeight=bold;" vertex="1" parent="1">
      <mxGeometry x="250" y="40" width="260" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="Review &amp; Investigation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#8957e5;strokeColor=#a371f7;fontColor=#ffffff;fontWeight=bold;" vertex="1" parent="1">
      <mxGeometry x="560" y="40" width="180" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="Impact Assessment" style="rhombus;whiteSpace=wrap;html=1;fillColor=#d29922;strokeColor=#e3b341;fontColor=#ffffff;fontWeight=bold;" vertex="1" parent="1">
      <mxGeometry x="560" y="140" width="180" height="80" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>"""

coc_svg = """
  <g filter="url(#drop-shadow)">
    <!-- Header Title -->
    <text x="30" y="38" fill="#58a6ff" font-size="16" font-weight="600">Code of Conduct — Incident Resolution Workflow</text>

    <!-- Node 1 -->
    <rect x="30" y="60" width="160" height="45" rx="8" fill="url(#card-blue)" stroke="#58a6ff" stroke-width="1.5"/>
    <text x="110" y="87" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle">Incident Occurs</text>

    <!-- Arrow 1 -->
    <path d="M 190 82.5 L 230 82.5" stroke="#8b949e" stroke-width="2" marker-end="url(#arrow)"/>
    <polygon points="236,82.5 226,77.5 226,87.5" fill="#8b949e"/>

    <!-- Node 2 -->
    <rect x="236" y="60" width="270" height="45" rx="8" fill="url(#card-green)" stroke="#39d353" stroke-width="1.5"/>
    <text x="371" y="87" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle">Report to Maintainer</text>

    <!-- Arrow 2 -->
    <path d="M 506 82.5 L 546 82.5" stroke="#8b949e" stroke-width="2"/>
    <polygon points="552,82.5 542,77.5 542,87.5" fill="#8b949e"/>

    <!-- Node 3 -->
    <rect x="552" y="60" width="190" height="45" rx="8" fill="url(#card-purple)" stroke="#d2a8ff" stroke-width="1.5"/>
    <text x="647" y="87" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle">Review &amp; Assessment</text>

    <!-- Arrow 3 (down) -->
    <path d="M 647 105 L 647 145" stroke="#8b949e" stroke-width="2"/>
    <polygon points="647,151 642,141 652,141" fill="#8b949e"/>

    <!-- Resolution Levels -->
    <rect x="30" y="160" width="165" height="50" rx="8" fill="#161b22" stroke="#388bfd" stroke-width="1.5"/>
    <text x="112" y="182" fill="#58a6ff" font-size="12" font-weight="600" text-anchor="middle">Level 1: Correction</text>
    <text x="112" y="198" fill="#8b949e" font-size="11" text-anchor="middle">Private Warning</text>

    <rect x="215" y="160" width="165" height="50" rx="8" fill="#161b22" stroke="#e3b341" stroke-width="1.5"/>
    <text x="297" y="182" fill="#e3b341" font-size="12" font-weight="600" text-anchor="middle">Level 2: Warning</text>
    <text x="297" y="198" fill="#8b949e" font-size="11" text-anchor="middle">Interaction Limit</text>

    <rect x="400" y="160" width="165" height="50" rx="8" fill="#161b22" stroke="#f78166" stroke-width="1.5"/>
    <text x="482" y="182" fill="#f78166" font-size="12" font-weight="600" text-anchor="middle">Level 3: Temp Ban</text>
    <text x="482" y="198" fill="#8b949e" font-size="11" text-anchor="middle">Timed Exclusion</text>

    <rect x="585" y="160" width="165" height="50" rx="8" fill="#161b22" stroke="#ff7b72" stroke-width="1.5"/>
    <text x="667" y="182" fill="#ff7b72" font-size="12" font-weight="600" text-anchor="middle">Level 4: Perm Ban</text>
    <text x="667" y="198" fill="#8b949e" font-size="11" text-anchor="middle">Permanent Removal</text>
  </g>
"""

create_drawio_svg("code-of-conduct.drawio.svg", 780, 235, "Code of Conduct Workflow", coc_xml, coc_svg)


# --- 2. CONTRIBUTING DIAGRAM ---
contrib_xml = """<mxGraphModel dx="1000" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="800" pageHeight="300">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
  </root>
</mxGraphModel>"""

contrib_svg = """
  <g filter="url(#drop-shadow)">
    <text x="30" y="38" fill="#58a6ff" font-size="16" font-weight="600">Contribution Lifecycle</text>

    <!-- Row 1 -->
    <rect x="30" y="60" width="130" height="42" rx="8" fill="url(#card-blue)" stroke="#58a6ff" stroke-width="1.5"/>
    <text x="95" y="85" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">1. Fork Repo</text>

    <path d="M 160 81 L 185 81" stroke="#8b949e" stroke-width="2"/>
    <polygon points="191,81 181,76 181,86" fill="#8b949e"/>

    <rect x="191" y="60" width="130" height="42" rx="8" fill="url(#card-blue)" stroke="#58a6ff" stroke-width="1.5"/>
    <text x="256" y="85" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">2. Branch</text>

    <path d="M 321 81 L 346 81" stroke="#8b949e" stroke-width="2"/>
    <polygon points="352,81 342,76 342,86" fill="#8b949e"/>

    <rect x="352" y="60" width="130" height="42" rx="8" fill="url(#card-purple)" stroke="#d2a8ff" stroke-width="1.5"/>
    <text x="417" y="85" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">3. Implement</text>

    <path d="M 482 81 L 507 81" stroke="#8b949e" stroke-width="2"/>
    <polygon points="513,81 503,76 503,86" fill="#8b949e"/>

    <rect x="513" y="60" width="130" height="42" rx="8" fill="url(#card-purple)" stroke="#d2a8ff" stroke-width="1.5"/>
    <text x="578" y="85" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">4. Test Code</text>

    <!-- Row 2 -->
    <rect x="191" y="135" width="130" height="42" rx="8" fill="url(#card-orange)" stroke="#e3b341" stroke-width="1.5"/>
    <text x="256" y="160" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">5. Commit &amp; Push</text>

    <path d="M 321 156 L 346 156" stroke="#8b949e" stroke-width="2"/>
    <polygon points="352,156 342,151 342,161" fill="#8b949e"/>

    <rect x="352" y="135" width="130" height="42" rx="8" fill="url(#card-orange)" stroke="#e3b341" stroke-width="1.5"/>
    <text x="417" y="160" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">6. Open PR</text>

    <path d="M 482 156 L 507 156" stroke="#8b949e" stroke-width="2"/>
    <polygon points="513,156 503,151 503,161" fill="#8b949e"/>

    <rect x="513" y="135" width="130" height="42" rx="8" fill="url(#card-green)" stroke="#39d353" stroke-width="1.5"/>
    <text x="578" y="160" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">7. Review &amp; Merge</text>

    <!-- Link Row 1 to Row 2 -->
    <path d="M 578 102 L 578 118 L 256 118 L 256 135" stroke="#8b949e" stroke-width="2" fill="none"/>
    <polygon points="256,135 251,125 261,125" fill="#8b949e"/>
  </g>
"""

create_drawio_svg("contributing.drawio.svg", 675, 205, "Contribution Lifecycle", contrib_xml, contrib_svg)


# --- 3. LICENSE DIAGRAM ---
license_xml = """<mxGraphModel dx="1000" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="800" pageHeight="300">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
  </root>
</mxGraphModel>"""

license_svg = """
  <g filter="url(#drop-shadow)">
    <text x="30" y="38" fill="#58a6ff" font-size="16" font-weight="600">MIT License Permissions &amp; Terms</text>

    <!-- Root -->
    <rect x="30" y="60" width="150" height="120" rx="8" fill="url(#card-blue)" stroke="#58a6ff" stroke-width="1.5"/>
    <text x="105" y="115" fill="#ffffff" font-size="14" font-weight="600" text-anchor="middle">MIT License</text>

    <!-- Column 1: Permissions -->
    <rect x="220" y="60" width="160" height="35" rx="6" fill="#161b22" stroke="#39d353" stroke-width="1.5"/>
    <text x="300" y="82" fill="#39d353" font-size="12" font-weight="600" text-anchor="middle">Permissions</text>
    <text x="300" y="112" fill="#c9d1d9" font-size="11" text-anchor="middle">• Commercial Use</text>
    <text x="300" y="128" fill="#c9d1d9" font-size="11" text-anchor="middle">• Modification &amp; Distribution</text>
    <text x="300" y="144" fill="#c9d1d9" font-size="11" text-anchor="middle">• Private Use</text>

    <!-- Column 2: Conditions -->
    <rect x="410" y="60" width="160" height="35" rx="6" fill="#161b22" stroke="#e3b341" stroke-width="1.5"/>
    <text x="490" y="82" fill="#e3b341" font-size="12" font-weight="600" text-anchor="middle">Conditions</text>
    <text x="490" y="112" fill="#c9d1d9" font-size="11" text-anchor="middle">• Include Copyright Notice</text>
    <text x="490" y="128" fill="#c9d1d9" font-size="11" text-anchor="middle">• Include License Notice</text>

    <!-- Column 3: Limitations -->
    <rect x="600" y="60" width="160" height="35" rx="6" fill="#161b22" stroke="#f78166" stroke-width="1.5"/>
    <text x="680" y="82" fill="#f78166" font-size="12" font-weight="600" text-anchor="middle">Limitations</text>
    <text x="680" y="112" fill="#c9d1d9" font-size="11" text-anchor="middle">• No Warranty</text>
    <text x="680" y="128" fill="#c9d1d9" font-size="11" text-anchor="middle">• No Author Liability</text>

    <!-- Connectors -->
    <path d="M 180 120 L 220 77" stroke="#8b949e" stroke-width="1.5"/>
    <path d="M 180 120 L 410 77" stroke="#8b949e" stroke-width="1.5"/>
    <path d="M 180 120 L 600 77" stroke="#8b949e" stroke-width="1.5"/>
  </g>
"""

create_drawio_svg("license.drawio.svg", 790, 200, "MIT License Structure", license_xml, license_svg)


# --- 4. SECURITY DIAGRAM ---
security_xml = """<mxGraphModel dx="1000" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="800" pageHeight="300">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
  </root>
</mxGraphModel>"""

security_svg = """
  <g filter="url(#drop-shadow)">
    <text x="30" y="38" fill="#58a6ff" font-size="16" font-weight="600">Security Vulnerability Response Flow</text>

    <rect x="30" y="60" width="160" height="45" rx="8" fill="url(#card-orange)" stroke="#e3b341" stroke-width="1.5"/>
    <text x="110" y="87" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">Vulnerability Identified</text>

    <path d="M 190 82.5 L 220 82.5" stroke="#8b949e" stroke-width="2"/>
    <polygon points="226,82.5 216,77.5 216,87.5" fill="#8b949e"/>

    <rect x="226" y="60" width="220" height="45" rx="8" fill="url(#card-blue)" stroke="#58a6ff" stroke-width="1.5"/>
    <text x="336" y="87" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">Email Maintainer Privately</text>

    <path d="M 446 82.5 L 476 82.5" stroke="#8b949e" stroke-width="2"/>
    <polygon points="482,82.5 472,77.5 472,87.5" fill="#8b949e"/>

    <rect x="482" y="60" width="170" height="45" rx="8" fill="url(#card-purple)" stroke="#d2a8ff" stroke-width="1.5"/>
    <text x="567" y="87" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">Triage &amp; Patch</text>

    <path d="M 652 82.5 L 682 82.5" stroke="#8b949e" stroke-width="2"/>
    <polygon points="688,82.5 678,77.5 678,87.5" fill="#8b949e"/>

    <rect x="688" y="60" width="150" height="45" rx="8" fill="url(#card-green)" stroke="#39d353" stroke-width="1.5"/>
    <text x="763" y="87" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">Public Release</text>
  </g>
"""

create_drawio_svg("security.drawio.svg", 870, 140, "Security Response Flow", security_xml, security_svg)
print("All 4 Draw.io SVGs generated successfully!")
