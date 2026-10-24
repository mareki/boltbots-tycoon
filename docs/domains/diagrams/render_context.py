"""BoltBots domain context view v1; Python standard library, no network or packages.
Run: python3 docs/domains/diagrams/render_context.py
This draws documentation only. It does not build or run the product.
"""
from pathlib import Path
import json
from html import escape
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent

def render(source):
    width, height = source['size']
    output = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
              '<title>BoltBots Tycoon — fachliche Kontextansicht, Revision 1</title>',
              '<desc>Ein Kontext für Fabrikfortschritt mit zwei internen Konsistenzgrenzen. Client, Roblox-Identität und dauerhafter Speicher sind externe Nachbarn.</desc>',
              '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" fill="#37536d"/></marker></defs>',
              f'<rect width="{width}" height="{height}" fill="#f7fafc"/>']
    identities = set()
    for box in source['boxes']:
        assert box['id'] not in identities
        identities.add(box['id'])
        x, y, w, h = box['bounds']
        assert 0 <= x < x+w <= width and 0 <= y < y+h <= height
        fill = '#e6f6fa' if box.get('context') else '#ffffff'
        output.append(f'<g id="{escape(box["id"])}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#37536d" stroke-width="2"/>')
        for index, line in enumerate(box['lines']):
            size = 16 if index == 0 else 14
            assert len(line) * size * 0.58 <= w-28, (box['id'], line)
            ty = y+28+index*25
            assert ty < y+h-10
            weight = 'bold' if index == 0 else 'normal'
            output.append(f'<text x="{x+14}" y="{ty}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="#152d43">{escape(line)}</text>')
        output.append('</g>')
    for edge in source['edges']:
        assert edge['from'] in identities and edge['to'] in identities
        x1,y1,x2,y2 = edge['line']
        assert all(0 <= x <= width for x in (x1,x2)) and all(0 <= y <= height for y in (y1,y2))
        start = ' marker-start="url(#arrow)"' if edge['both'] else ''
        output.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#37536d" stroke-width="2" marker-end="url(#arrow)"{start}/>')
    for note in source['notes']:
        x,y = note['position']
        assert x >= 0 and y >= 14 and y <= height and x + len(note['text'])*7.6 <= width
        output.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="13" fill="#37536d">{escape(note["text"])}</text>')
    output.append('</svg>')
    result = '\n'.join(output)+'\n'
    ET.fromstring(result)
    return result

if __name__ == '__main__':
    source = json.loads((HERE/'context-map.json').read_text())
    result = render(source)
    assert result == render(source)
    (HERE/'context-map.svg').write_text(result)
    print('SVG generated; XML, unique IDs, endpoint references and declared bounds valid.')
