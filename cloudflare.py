import requests

def main():
    word = "cloudflare"
    url = requests.get("www.cloudflare.com/es-es/")
    cabeceras = dict(url.headers)
    verify = false 
    for c in cabeceras:
        if word in cabeceras[c].lower():
            verify = True
                 break
        if verify == True:
            print("cloudflare presente"
            else:
                print(" el sitio no esta presente")

            if _name_=='_name':
                try:
                    main()
                    exceptKeyboarInterrupt:
                    exit()          