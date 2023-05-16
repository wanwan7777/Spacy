import spacy
import matplotlib.pyplot as plt
import numpy as np

nlp = spacy.load("en_core_web_sm")
doc = nlp("SAN FRANCISCO (Reuters) - Apple Inc has acquired social media search and analytics startup Topsy, an unusual purchase for a hardware-focused company that has made few forays into social networking. Apple confirmed the acquisition but would not say why it bought the company, which specializes in analyzing Twitter data and providing insights into current sentiment on a variety of topics. The Wall Street Journal, which reported the news earlier, cited people familiar with the deal as saying Apple paid over $200 million (£122.2 million). Apple buys smaller technology companies from time to time, and we generally do not discuss our purpose or plans, spokeswoman Kristin Huguet said. Topsy did not respond to requests for comment. The iPad and iPhone maker often does what it calls bolt-on acquisitions, small deals to acquire technology that then gets integrated into existing or future products. Many of its acquisitions in recent years have been angled toward improving hardware. This year, it paid a reported $350 million for Israeli 3D chip developer PrimeSense Ltd, perceived as an effort to incorporate gesture technology into its devices. And in 2008, it paid a reported $280 million for a semiconductor designer that eventually yielded the current line of processors that power the iPhone and iPad. Apple’s main effort in social media has revolved around Ping, a music-centred social sharing network that was at one point integrated into its iTunes app. The service, which lets users post music tracks they liked to a news feed, didn’t catch on and was shut down. But the California gadget maker has been increasingly making it easier for people to share photos, videos and news through its devices and directly to social networks such as Facebook and Twitter. It also operates iTunes Radio, an online streaming music service that competes with Pandora and could benefit from Topsy’s data on consumer sentiment. Apple closed 0.9 percent lower on Monday and was holding steady in after-hours trading. Why? Speculation on Apple’s motives ran the gamut on Monday, but some industry experts thought it likely that the company which continually tries to enhance its iPhones, iPads and Macintosh computers in the face of ever-strengthening competition from the likes of Samsung Electronics is looking to beef up customer-facing software. From an usage perspective, they can use it for the app store and iTunes, said Gartner analyst Carolina Milanesi, who added that Topsy could be used, for instance, to better serve app recommendations to users. With apps, it is really difficult to find good recommendations, she said. It’s much harder to see what people use and why. Apple also bought app-search tool Chomp last year, with the objective of sprucing up its online apps store, still one of the largest in the mobile industry along with Google Inc’s Play for Android devices. San Francisco-based Topsy is one Twitter’s partners, enjoying direct access to the messaging service’s billions of tweets over several years and has indexed all them to make them readily and rapidly searchable. The startup has received funding from BlueRun Ventures, Ignition Partners, the Founders Fund and Scott Banister.")
gpe = 0
org = 0
product = 0
money = 0
person = 0
date = 0
norp = 0
cardinal = 0
percent = 0
nocounter = 0

for ent in doc.ents:
    if ent.label_ == 'GPE':
        print(ent.text)
        gpe += 1
    elif ent.label_ == 'ORG':
        print(ent.text)
        org += 1
    elif ent.label_ == 'PRODUCT':
        print(ent.text)
        product += 1
    elif ent.label_ == 'MONEY':
        print(ent.text)
        money += 1
    elif ent.label_ == 'PERSON':
        print(ent.text)
        person += 1
    elif ent.label_ == 'DATE':
        print(ent.text)
        date += 1
    elif ent.label_ == 'NORP':
        print(ent.text)
        norp += 1
    elif ent.label_ == 'CARDINAL':
        print(ent.text)
        cardinal += 1
    elif ent.label_ == 'PERCENT':
        print(ent.text)
        percent += 1
    elif ent.label_ == 'RANDOM':
        print(ent.text)
        nocounter += 1

    
print(f'Gpe:{gpe} Org:{org} Product:{product} Money:{money} Person:{person} Date:{date} Norp:{norp} Cardinal:{cardinal} Percent:{percent}')

data = np.array([gpe, org, product, money, person, date, norp, cardinal, percent])

labels = ['Geopolitical Entity'.format(gpe),'Organiations'.format(org), 'Product'.format(product),'Money Value'.format(money), 'Person'.format(person), 'Date'.format(data),'Nationalities or religious or political groups'.format(norp),'Cardinal'.format(cardinal),'Percent'.format(percent)]

plt.title("Apple buys startup Topsy; gets rich Twitter data-Rachel")
plt.pie(data, labels = labels, autopct='%1.1f%%')
plt.show()