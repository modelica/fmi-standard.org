import os

src = r'E:\Development\fmi-standard.org\jekyll\_posts'
dst = r'E:\Development\fmi-standard.org\content\news'

for filename in os.listdir(src):
    f = os.path.join(src, filename)

    s = filename.split('-')

    if not os.path.isfile(f):
        continue

    alias = f'/news/{s[0]}/{s[1]}/{s[2]}/{filename[11:-3]}.html'

    print(f)

    with open(f, 'r') as ff:
        lines = ff.readlines()

    with open(os.path.join(dst, filename), 'w') as ff:
        for line in lines:
            if line.startswith(('categories:', 'layout:')):
                continue
            ff.write(line)
            if line.startswith('title:'):
                ff.write(f'date: {filename[:10]}\n')
                ff.write(f'aliases: [{alias}]\n')

          
