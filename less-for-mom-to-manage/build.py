import html, re
t = open('AI-Day-Audit-Prompt.txt').read().rstrip('\n')
out=[]
for line in t.split('\n'):
    e = html.escape(line, quote=False)
    if re.match(r'^STEP \d', line): e = f'<span class="ph">{e}</span>'
    out.append(e)
s = open('template.html').read().replace('{{PROMPT}}', '\n'.join(out))
open('AI-Day-Audit.html','w').write(s)
