with open('docs/index.html_') as f1, open('docs/index.html','w') as o1:
    content = f1.read()
    content = content.replace('href=https://shiki-sato.github.io/about/favicon-32x32.png', 'href="https://shiki-sato.github.io/about/favicon-32x32.png"').replace('href=https://shiki-sato.github.io/about/favicon-16x16.png', 'href="https://shiki-sato.github.io/about/favicon-16x16.png"').replace('href=https://shiki-sato.github.io/about/site.webmanifest', 'href="https://shiki-sato.github.io/about/site.webmanifest"').replace('href=https://shiki-sato.github.io/about/safari-pinned-tab.svg color="#5bbad5"', 'href="https://shiki-sato.github.io/about/safari-pinned-tab.svg" color="#5bbad5"')
    content = content.replace('href=https://shiki-sato.github.io/about/css/normalize.css', 'href="https://shiki-sato.github.io/about/css/normalize.css"').replace('href=https://shiki-sato.github.io/about/css/main.css', 'href="https://shiki-sato.github.io/about/css/main.css"')
    o1.write(content)
