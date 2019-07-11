#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
from six.moves.urllib import parse
import requests
from lxml import html
import re


# In[107]:


final_report = []
final_score = 0


# In[114]:


url = 'google.com'
a1 = url.split(':')


# row 15 HTTPS test

result = {
            'name':'https_test',
            'message':'',
            'marks':''
        }

if a1[0] == 'https' or a1[0] == 'http':
    if a1[0] != 'https':
        a1[0] = 'https'
        a2 = a1.insert(1,':')
        print(a1)
        web = ''.join(a1)
        print("This is web  ",web)
        
        try:
            r = requests.get(web)
            result['message'] = 'Félicitations. Votre site les données transitants par votre site sont sécurisées avec un certificat SSL'
            result['marks'] = 4
        except:
            result['message'] = '''
            Votre site ne dispose pas de certificat SSL. Les données qui y transitent peuvent donc être récupérés par des parties malveillantes. Google donne une grande importance à la sécurité des visiteurs.
            '''
            result['marks'] = 0
            print("HTTPS didn't worked")
            
else:
    try:
        url = 'https://'+url
        r = requests.get(url)
        result['message'] = 'Félicitations. Votre site les données transitants par votre site sont sécurisées avec un certificat SSL'
        result['marks'] = 4
        
        
    except:
        url = 'http://'+url
        r = requests.get(url)
        result['message'] = '''
            Votre site ne dispose pas de certificat SSL. Les données qui y transitent peuvent donc être récupérés par des parties malveillantes. Google donne une grande importance à la sécurité des visiteurs.
            '''
        result['marks'] = 0
        
final_report.append(result)
final_score = final_score + result['marks']

soup = BeautifulSoup(r.text, "lxml")


# In[115]:


final_report


# In[ ]:





# In[55]:


# This is for row 1 (title)
try:
    title_ln =  len(soup.find('title').text)
    if title_ln < 70:
        result = {
            'name':'title',
            'message':'Félicitations votre site dispose d’un titre avec un nombre de caractères optimale soit moins de 70 caractères',
            'title_length': title_ln,
            'marks':5
        }
        final_score = final_score + 5
        final_report.append(result)
    elif title_ln > 70:
        result = {
            'name':'title',
            'message':'Votre titre est trop long, le nombre de caractères optimal est de 70 caractères, essayez de le raccourcir',
            'title_length': title_ln,
            'marks':2
        }
        final_score = final_score + 2
        final_report.append(result)
except:
    result = {
        'name':'title',
        'message':'Votre site ne dispose pas de balise meta title. La balise <title> correspond au titre de votre page web. Il s’agit d’un champ essentiel à ne pas négliger dans le cadre d’une bonne stratégie d’optimisation du référencement naturel puisqu’elle est l’un des critères les plus importants pour les moteurs de recherche (Google, Bing...)',
        'title_length': 0,
        'marks':0
    }
    final_score = final_score + 0
    final_report.append(result)


# In[56]:


# This is for row 2 (meta @description)
name = 'meta_description'
length_var_name = 'meta_desc_len'
try:
    meta_tag  = soup.find("meta", {"name" : "description"})
    desc_text_ln = len(meta_tag['content'])
    title_ln = int(desc_text_ln)
   
    
    if title_ln < 150:
        result = {
            'name':name,
            'message':'Votre méta-description est trop courte, le nombre de caractère optimale doit être entre 150 et 250 caractères.',
            length_var_name: desc_text_ln,
            'marks':1
        }
        final_score = final_score + result['marks']
        final_report.append(result)
        print('try worked1')
    elif title_ln > 150 and title_ln < 250:
        result = {
            'name':name,
            'message':'Félicitations votre site dispose d’une méta-description avec un nombre de caractère optimal entre 150 et 155 caractères',
            length_var_name: desc_text_ln,
            'marks':3
        }
        final_score = final_score + result['marks']
        final_report.append(result) 
        print('try worked2')
        
    elif title_ln > 250 :
        result = {
            'name':name,
            'message':' Votre méta-description est trop longue, essayez de la raccourcir, le nombre optimal est entre 150 et 250 caractères, le reste risque d’être tronqué sur l’affichage du résultat sur les moteurs de recherche.',
            length_var_name: desc_text_ln,
            'marks':2
        }
        final_score = final_score + result['marks']
        final_report.append(result)
        print('try worked3')
except:
    result1 = {
        'name':name,
        'message':'Votre site ne dispose pas de méta-description, La balise meta description manque sur votre page. Vous devez inclure cette balise afin de fournir une brève description de votre page pouvant être utilisée par les moteurs de recherche. Des méta-descriptions bien écrites et attrayantes peuvent également aider les taux de clics sur votre site dans les résultats de moteur de recherche',
        length_var_name: 0,
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[57]:


# This is for row 3 (meta @keywords)
name = 'meta_keywords'
length_var_name = 'meta_key_len'
try:
    meta_tag  = soup.find("meta", {"name" : "keywords"})
    desc_text_ln = len(meta_tag['content'])
    title_ln = int(desc_text_ln)
   
    
    if title_ln:
        result = {
            'name':name,
            'message':'Bravo vous avez spécifié des meta keywords . Vos mots-clés principaux doivent apparaître dans vos méta-tags pour vous aider à identifier le sujet de votre page Web dans les moteurs de recherche.',
            length_var_name: desc_text_ln,
            'marks':1
        }
        final_score = final_score + result['marks']
        final_report.append(result)
        print('try worked1')
except:
    result1 = {
        'name':name,
        'message':'Vos mots-clés principaux doivent apparaître dans vos méta-tags pour vous aider à identifier le sujet de votre page Web dans les moteurs de recherche.',
        length_var_name: 0,
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[58]:


# This is for row 4 (meta @robots)
name = 'meta_robots'
length_var_name = 'meta_robots_len'
try:
    meta_tag  = soup.find("meta", {"name" : "robots"})
    desc_text_ln = len(meta_tag['content'])
    title_ln = int(desc_text_ln)
    
    if title_ln:
        result = {
            'name':name,
            'message':"Votre site dispose d'un fichier robots.txt",
            length_var_name: desc_text_ln,
            'marks':4
        }
        final_score = final_score + result['marks']
        final_report.append(result)
        print('try worked1')
except:
    result1 = {
        'name':name,
        'message':'''
                    Votre site n’a pas de robot.txt
                    Le robots.txt est un fichier texte utilisant un format précis qui permet à un Webmaster de contrôler quelles zones de son site un robot d'indexation est autorisé à analyser. Ce fichier texte sera disponible à une URL bien précise pour un site donné, par exemple http://www.monsite.com/robots.txt
                    Pour bien comprendre à quoi sert un robots.txt, il faut comprendre la manière dont fonctionnent les robots d'indexation des moteurs de recherche (appelés aussi Web spiders, Web crawlers ou Bots) tels que Google, Yahoo ou Bing. Voici leurs actions lorsqu'ils analysent un site tel que www.monsite.com : ils commencent par télécharger et analyser le fichier http://www.monsite.com/robots.txt.
        ''',
        length_var_name: 0,
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[59]:


# This is for row 5 (html lang)
name = 'html_lang'
length_var_name = 'html_lang'
try:
    meta_tag  = soup.find("html", {"lang" : True})
    lang_text = meta_tag['lang']
    

    result = {
        'name':name,
        'message':"Félicitations. Vous avez spécifié une langue à votre page.",
        length_var_name: lang_text,
        'marks':3
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    print('try worked1')
except:
    result1 = {
        'name':name,
        'message':'''
        Vous devriez spécifier une langue pour votre site, les moteurs de recherches ne comprennent pas quand un site dispose de plusieurs langues par exemple ayant des mots techniques en anglais et un contenu texte en français. Il faut donc bien spécifier la langue.
        ''',
        length_var_name: 0,
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[60]:


# This is for row 6 (sitemap)
url = url.strip()
sitemap_url =  url+'/sitemap.xml'
code = requests.get(sitemap_url).status_code

name = 'sitemap'

if code == 200:
    result = {
        'name':name,
        'message':"Félicitations, votre site dispose d’un fichier sitemap",
        'marks':2
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    
else:
    result = {
        'name':name,
        'message':"Votre site Web ne dispose pas d'un fichier sitemap. Les sitemaps peuvent aider les robots à indexer votre contenu de manière plus complète et plus rapide. ",
        'marks':0
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    


# In[61]:


# This is for row 7 (google Analytics)
searched_word = 'google-analytics'

name = 'google_analytics'
if searched_word in str(soup):
    print("Google analytics found")
    result = {
        'name':name,
        'message':"Félicitations, votre site dispose de l'outil Google Analytics",
        'marks':2
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    
else:
    result = {
        'name':name,
        'message':"Votre site ne dispose pas de l'outil Google Analytics.",
        'marks':0
    }
    final_score = final_score + result['marks']
    final_report.append(result)


# In[62]:


# This is for row 8 (page_cache)
name = 'page_cache'
length_var_name = 'page_cache_desc'
try:
    meta_tag  = soup.find("meta", {"http-equiv" : "Cache-control"})
    lang_text = meta_tag['content']
    

    result = {
        'name':name,
        'message':"Vous avez activé le cache sur votre page, c'est très bien.",
        length_var_name: lang_text,
        'marks':3
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    print('try worked1')
except:
    result1 = {
        'name':name,
        'message':"Vous n'avez pas activé la mise en cache sur vos pages. La mise en cache permet un chargement plus rapide des pages.",
        length_var_name: 0,
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[63]:


# API_KEY = AIzaSyD_RLUOcTN1JAq8PL8zJ79X6-kmHIDy_uM
# This is for row 9 (Google safe browsing api)


from gglsbl import SafeBrowsingList
api_key = 'AIzaSyCVylpWnsOwzUoeTGg7akZRod-4YbhXoPU'
sbl = SafeBrowsingList(api_key)
bl = sbl.lookup_url(url)

name = 'google_safe_browsing'
if bl is None:
    print("Website is safe")
    result = {
        'name':name,
        'message':"Votre site est considéré comme sécurisé.",
        'marks':2
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    
else:
    result = {
        'name':name,
        'message':"Votre site n'est pas considéré comme sécurisé. Google et les autres moteurs de recherche prennent en compte le niveau de sécurité de votre site pour garantir la sécurité des visiteurs.",
        'marks':0,
        'threats':bl
    }
    final_score = final_score + result['marks']
    final_report.append(result)


# In[64]:


# This is for row 10 (responsive website test)
name = 'responsive_test'
length_var_name = 'responsive_test_desc'
try:
    meta_tag  = soup.find("meta", {"name" : "viewport"})
    lang_text = meta_tag['content']
    

    result = {
        'name':name,
        'message':"Félicitations. Votre site est responsive.",
        length_var_name: lang_text,
        'marks':4
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    print('try worked1')
except:
    result1 = {
        'name':name,
        'message':'''
        Nous n'avons pas détécté que votre site internet était responsive, soit adapté au mobile. Google prend énormément en compte ce critère pour un bon référencement.
        ''',
        length_var_name: 0,
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[65]:


# Html page size


# In[66]:


# # mobile_friendliness_test

# data = {
#   "url": url,
#   "requestScreenshot": True,
# }
# r1 = requests.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key=AIzaSyDExRwe7TNEgHa_JLogOVjccqWNVoaH-EQ',data)
# r1.text
# import json
# a = json.loads(r1.text)
# imgstring = a['screenshot']['data']
# # import base64
# # imgdata = base64.b64decode(imgstring)
# # filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
# # with open(filename, 'wb') as f:
# #     f.write(imgdata)

# name = 'mobile_friendliness_test'

# if a['mobileFriendliness'] is 'MOBILE_FRIENDLY':
#     print("Website is mobile friendly")
#     result = {
#         'name':name,
#         'message':"Félicitations. Votre site est Mobile friendly.",
#         'result': a['mobileFriendliness'],
#         'img_string':imgstring,
#         'marks':4
#     }
#     final_score = final_score + result['marks']
#     final_report.append(result)
    
# else:
#     result = {
#         'name':name,
#         'message':"Votre site n'est pas optimisé pour le mobile. Les moteurs de recherches donnent une très grande importance à la compatibilité mobile.",
#         'marks':0,
#         'result': a['mobileFriendliness'],
#         'img_string':imgstring
#     }
#     final_score = final_score + result['marks']
#     final_report.append(result)

# #     #  "mobileFriendlyIssues": [
# # #   {
# # #    "rule": "TAP_TARGETS_TOO_CLOSE"
# # #   },
# # #   {
# # #    "rule": "USE_LEGIBLE_FONT_SIZES"
# # #   },
# # #   {
# # #    "rule": "CONFIGURE_VIEWPORT"
# # #   }
# # #  ],


# In[ ]:





# In[47]:


# google page speed
r2 = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}?key=AIzaSyAXf3ILJpeIs1nfDvvmLk0MsQDsuIsG5gM'.format(url))
b = json.loads(r2.text)
# final_report.append({
#     "google_page_speed_data":b
# })


# In[ ]:





# In[67]:


# This is for row 13 (img alt attribute)
name = 'img_alt'
img_tags  = soup.findAll("img")

no_alt = []
empty_alt = []
alt_ok = []
empty_check = []

name = "img_alt"


for img_tag in img_tags:
    if not img_tag['alt']:
        empty_alt.append(img_tag['src'])
        
    elif img_tag['alt'] is None:
        no_alt.append(img_tag['src'])
        
    else:
        alt_ok.append(img_tag['src'])
        
total_alt_num = len(empty_alt)+len(alt_ok)

img_alt_result = {
    'name':name,
    'message':'',
    'marks': '',
    'no_alt':no_alt,
    'empty_altm':empty_alt
}

if len(img_tags) == len(alt_ok):
    img_alt_result['message'] = 'Félicitations. Toutes vos images disposent de balises alt attributs'
    img_alt_result['marks'] = 3
    print("every image tag contains alt and all have values")
    
elif empty_alt and len(img_tags) == total_alt_num :
    img_alt_result['message'] = 'Certaines de vos images manquent de balises alt attributs. Voir la liste complète'
    img_alt_result['marks'] = 1
    print("Every img have alt tag but some have empty alt")
    
elif len(img_tags) == len(no_alt):
    img_alt_result['message'] = "Aucune de vos images n'a de balises alt attributs, elles sont essentielles pour permettre aux moteurs de recherche de comprendre ce que représente votre image."
    img_alt_result['marks'] = 0
    print("No images have alt tag")
    
if no_alt:
    print("Some images have no  alt tag")
    

final_score = final_score + img_alt_result['marks']
final_report.append(img_alt_result)


# In[75]:


# This is for row 14 (favicon test)
name = 'favicon_test'
length_var_name = 'favicon_link'

favicon_list = []
link_tags  = soup.findAll("link") 
for link in link_tags:
    if "favicon" in link['href']:
        favicon_list.append(link['href'])
if favicon_list:

    result = {
        'name':name,
        'message':"Félicitations. Votre site dispose d'une favicon.",
        length_var_name: favicon_list,
        'marks':1
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    print('if worked1')
else:
    result1 = {
        'name':name,
        'message':"Votre site ne dispose pas de favicon. La favicon est la petite icone qui apparait en haut du navigateur à côté du titre de votre site. Au delà de l'aspect SEO, elle permet de donner une identité visuelle à votre site.",
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('else worked')


# In[98]:


# This is for strong tag test
name = 'strong_tag'
length_var_name = 'strong_text'
try:
    strong_tags  = soup.findAll("strong")
    
    if strong_tags:
        result = {
            'name':name,
            'message':'Félicitations. Vous avez spécifié des balises strong dans votre texte',
            length_var_name: strong_tags,
            'marks':2
        }
    else:
        result = {
        'name':name,
        'message':" Vous n'avez spécifié aucune balise strong dans votre texte. Les balises strong permettent aux moteurs de recherche de savoir quel contenu est intéressant et pertinent dans votre texte.",
        'marks':0
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    print('try worked1')
except:
    result1 = {
        'name':name,
        'message':" Vous n'avez spécifié aucune balise strong dans votre texte. Les balises strong permettent aux moteurs de recherche de savoir quel contenu est intéressant et pertinent dans votre texte.",
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[119]:


# This is for Microdata test (itemscope , itemtype)
name = 'micro_data_test'
try:
    soup.find(True,{'itemscope':True}) or soup.find(True,{'itemtype':True})

    result = {
        'name':name,
        'message':"Félicitations. Votre site utilise des Microdonnées Schema.org",
        'marks':3
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    print('try worked1')
except:
    result1 = {
        'name':name,
        'message':'''
         Vos visiteurs aiment les beadcrumbs, mais Google aussi. Les beadcrumbs donnent à Google un autre moyen de comprendre la structure de votre site Web. Toutefois, comme indiqué précédemment, Google peut également utiliser vos beadcrumbs dans les résultats de recherche, ce qui rend votre résultat beaucoup plus attrayant pour les utilisateurs.
         ''',
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[125]:


# This is for AMP Version
name = 'amp_html_test'
try:
    tag = soup.find('link',{'rel':"amphtml"})

    result = {
        'name':name,
        'message':" Félicitations. Votre site dispose d'une version AMP",
        'amp_html_link':tag['href'],
        'marks': 3
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    print('try worked1')
except:
    result1 = {
        'name':name,
        'message':'''L’objectif est que les pages AMP s’affichent presque de façon instantannée, c’est-à-dire généralement 90% plus rapidement que d’habitude.
Grâce à cette grande vitesse, l’expérience utilisateur sur mobile se trouve largement améliorée, ce qui d’après des études fait chuter le taux de rebo
''',
        'marks':0
    }
    final_score = final_score + result1['marks']
    final_report.append(result1)
    print('except worked')


# In[127]:


# This is for Breadcrumps
searched_word = 'breadcrumb'

name = 'breadcrumb'
if searched_word in str(soup).lower():
    print("Breadcrum found")
    result = {
        'name':name,
        'message':"Félicitations, votre site dispose de l'outil Google Analytics",
        'marks':2
    }
    final_score = final_score + result['marks']
    final_report.append(result)
    
else:
    result = {
        'name':name,
        'message':"Vos url sont composées de plus de 5 dossiers, veuillez en diminuer le nombre",
        'marks':0
    }
    final_score = final_score + result['marks']
    final_report.append(result)


# In[128]:


final_report


# In[ ]:




