import urllib.request
import base64

icons_skill = [
    "py", "java", "js", "c", "cpp", "mysql", "mongodb", "tensorflow",
    "sklearn", "react", "nextjs", "nodejs", "fastapi", "docker", "aws",
    "html", "css", "tailwind", "linux", "supabase"
]

icons_simple = [
    ("langchain", "#ffffff"),
    ("langgraph", "#ffffff"),
    ("n8n", "#ea3a3d")
]

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 80" width="800" height="80">
  <rect width="100%" height="100%" fill="#0d1117" rx="10" />
  <g>
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-1472 0" dur="25s" repeatCount="indefinite"/>
"""

x_offset = 0
b64_cache = []

for icon in icons_skill:
    url = f"https://skillicons.dev/icons?i={icon}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    b64_data = base64.b64encode(response).decode('utf-8')
    b64_cache.append(b64_data)

for icon, color in icons_simple:
    url = f"https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{icon}.svg"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response_str = urllib.request.urlopen(req).read().decode('utf-8')
    
    path_start = response_str.find('<path')
    path_data = response_str[path_start:response_str.rfind('</svg>')]
    
    custom_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
      <rect width="256" height="256" fill="#242938" rx="60"/>
      <g transform="scale(6.4) translate(8, 8)">
         <g fill="{color}">
            {path_data}
         </g>
      </g>
    </svg>'''
    
    b64_data = base64.b64encode(custom_svg.encode('utf-8')).decode('utf-8')
    b64_cache.append(b64_data)

for b64_data in b64_cache:
    svg_content += f'    <image x="{x_offset}" y="16" width="48" height="48" href="data:image/svg+xml;base64,{b64_data}" />\n'
    x_offset += 64

x_offset = 1472
for b64_data in b64_cache:
    svg_content += f'    <image x="{x_offset}" y="16" width="48" height="48" href="data:image/svg+xml;base64,{b64_data}" />\n'
    x_offset += 64

svg_content += """  </g>
</svg>"""

with open("assets/tech-carousel.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Successfully generated tech-carousel.svg with mixed icons!")
