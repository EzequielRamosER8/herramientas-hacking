import dns.resolver
from os import path
#nombre del programa brutesubdominio
def main():
  if path.exists('subdominios.txt'):
      wordlist = open('subdominios.txt','r')
      wordlist = wordlist.read().split('\n')
      lista = []
      for s in wordlist:
          try:
              a = dns.resolver.query('{}.google.com'.format(s),'A')
              list.append('{}.google.com'.format(s))
          except:
              pass
              if len(lista) > 0:
                  print('numero de subdominios posibles:{}'.format((len(lista)))
                  for e in lista:
                       print(e)
                  else:
                      print('no se encontraron subdominios')
                  else:
                      print('no existe el archivo')

                      if __name__=='__name__':
                          try:
                              main()
                              except KeyboardInterrupt:
                                  exit()    
