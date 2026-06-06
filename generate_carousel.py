import urllib.request
import base64

icons = [
    "py", "java", "js", "c", "cpp", "mysql", "mongodb", "tensorflow",
    "sklearn", "react", "nextjs", "nodejs", "fastapi", "docker", "aws",
    "html", "css", "tailwind", "linux"
]

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 80" width="800" height="80">
  <rect width="100%" height="100%" fill="#0d1117" rx="10" />
  <g>
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-1216 0" dur="20s" repeatCount="indefinite"/>
"""

x_offset = 0
b64_cache = []

# Fetch and base64 encode each icon
for icon in icons:
    url = f"https://skillicons.dev/icons?i={icon}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    
    # Base64 encode the SVG response
    b64_data = base64.b64encode(response).decode('utf-8')
    b64_cache.append(b64_data)
    
    # Add to SVG content
    svg_content += f'    <image x="{x_offset}" y="16" width="48" height="48" href="data:image/svg+xml;base64,{b64_data}" />\n'
    x_offset += 64

# Duplicate for infinite scroll
x_offset = 1216
for b64_data in b64_cache:
    svg_content += f'    <image x="{x_offset}" y="16" width="48" height="48" href="data:image/svg+xml;base64,{b64_data}" />\n'
    x_offset += 64

svg_content += """  </g>
</svg>"""

with open("assets/tech-carousel.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Successfully generated tech-carousel.svg with Base64 images!")
