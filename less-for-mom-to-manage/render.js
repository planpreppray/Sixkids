const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/AI-Day-Audit.html', {waitUntil:'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: 'Less-for-Mom-to-Manage-AI-Day-Audit.pdf', preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
