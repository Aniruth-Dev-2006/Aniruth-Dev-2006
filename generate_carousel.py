import urllib.request

url = "https://skillicons.dev/icons?i=py,java,js,c,cpp,mysql,mongodb,tensorflow,sklearn,react,nextjs,nodejs,fastapi,docker,aws,html,css,tailwind,linux"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req).read().decode('utf-8')

# Extract inner SVG content
inner_svg = response[response.find('<svg'):]
inner_content = inner_svg[inner_svg.find('>')+1 : inner_svg.rfind('</svg>')]

# Fix IDs in the duplicated content so they don't conflict (skillicons uses things like id="react-dark")
dup_content = inner_content.replace('id="', 'id="dup_').replace('url(#', 'url(#dup_')

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 80" width="800" height="80">
  <rect width="100%" height="100%" fill="#0d1117" rx="10" />
  <g>
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-1216 0" dur="20s" repeatCount="indefinite"/>
    <svg x="0" y="16" width="1216" height="48">
      {inner_content}
    </svg>
    <svg x="1216" y="16" width="1216" height="48">
      {dup_content}
    </svg>
  </g>
</svg>
"""

with open("assets/tech-carousel.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Successfully generated tech-carousel.svg!")
