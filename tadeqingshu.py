__author__ = '31351'


#!/usr/bin/env python
# encoding: utf-8
import urllib2
from bs4 import BeautifulSoup
def url_open(url):
    # url = urllib.quote(url)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

url = 'http://ctf4.shiyanbar.com/crypto/4/'
with open("D:\\soup.txt",'wb') as f:
    f.write(str(url_open(url)))


eval(function(p,a,c,k,e,d){
    e=function(c){
        return(c<a?"":e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))
    };
    if(!''.replace(/^/,String)){
        while(c--)
            d[e(c)]=k[c]||e(c);
            k=[function(e){return d[e]}];
            e=function(){return'\\w+'};
            c=1;
    };
    while(c--)
        if(k[c])
            p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);
            return p;
}
            ('<!--v p(){6 8=h.o.e.n;6 2="q==";6 a=\'t.s?e=\';6 d=j.r;6 k=\'\';6 g=2.9(m,4*4)+2.9(l,5*5)+2.9(0,1)+2.b(7,1)+2.b(z,1)+2.b(B,1)+2.9(3+3,7);8=d.b(d.f(\'?\')+1);a=a.9(0,a.f(\'?\')+1)+\'A=\';w(i=0;i<8.y;i++){x(8.c(i)==g.c(i)){h.u(8.c(i))}}j=a+8}-->'
            ,38,38,
            '||cry||||var||pass|substring|addr|substr|charAt|locatie|passwd|indexOf|pass2|document||location|out|24|15|value|form|zhegejiamiyidiandoubuku|Rm9yM0re354v5E4FUg5FasDboooo|href|php|soroki|write|function|for|if|Len|11|l0vau|13'.split('|'),0,{}))