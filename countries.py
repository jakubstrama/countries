import json

def getFile():
    with open('input.json', 'r') as myfile:
        return json.load(myfile)
  
def saveFile(data, name):
    with open(name + '.json', 'w') as myfile:
        json.dump(data, myfile, ensure_ascii=False)


def main():
    data = getFile()
    countries = []
    langMain = dict()

    for country in data:
        ctr = dict()
        ctr['official'] = country.get('translations').get('deu').get('official')
        ctr['common'] = country.get('translations').get('deu').get('common')
        ctr['code'] = country.get('cca2')
        countries.append(ctr)


        lang = dict()
        lang['de'] = country.get('translations').get('deu').get('common')
        lang['fr'] = country.get('translations').get('fra').get('common')
        lang['en'] = country.get('name').get('common')
        if country.get('translations').get('spa'):
            lang['sp'] = country.get('translations').get('spa').get('common')
        if country.get('translations').get('ita'):
            lang['it'] = country.get('translations').get('ita').get('common')
        langMain[country.get('cca2').lower()] = lang


    saveFile(countries, 'countries')
    saveFile(langMain, 'languages')

if  __name__ =='__main__':main()