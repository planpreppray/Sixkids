import html, re
t = open('AI-Day-Audit-Prompt.txt').read().rstrip('\n')
out=[]
for chunk in t.split('\n\n'):
    lines=[]
    for line in chunk.split('\n'):
        e = html.escape(line, quote=False)
        if re.match(r'^STEP \d', line): e = f'<span class="ph">{e}</span>'
        lines.append(e)
    out.append('<div class="blk">' + '\n'.join(lines) + '</div>')
import urllib.parse
q = urllib.parse.quote(t, safe='')
s = open('template.html').read().replace('{{PROMPT}}', ''.join(out))
s = s.replace('{{GPT}}', 'https://chatgpt.com/?q=' + q).replace('{{CLAUDE}}', 'https://claude.ai/new?q=' + q)
open('AI-Day-Audit.html','w').write(s)
