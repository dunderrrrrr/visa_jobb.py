import json
import sys
import requests
from settings import settings, options
from optparse import OptionParser

def get_lans(laen):
    geturl = settings['url'] + "/platsannonser/soklista/lan"
    r = requests.request("GET", geturl, headers=settings['headers'])
    if laen:
        for lan in r.json()['soklista']['sokdata']:
            if lan['namn'] == laen:
                return(lan)
    else:
        return (r.json())

def fetch_kom(id):
    geturl = settings['url'] + "/platsannonser/soklista/kommuner?lanid={}".format(id)
    r = requests.request("GET", geturl, headers=settings['headers'])
    for kommun in r.json()['soklista']['sokdata']:
        if kommun['namn'] != 'Ospecificerad arbetsort':
            kommuner.append(kommun['namn'])

def get_kom(kom):
    if kom == 'all':
        for lans in get_lans(None)['soklista']['sokdata']:
            fetch_kom(lans['id'])
    else:
        for lans in get_lans(None)['soklista']['sokdata']:
            geturl = settings['url'] + "/platsannonser/soklista/kommuner?lanid={}".format(lans['id'])
            r = requests.request("GET", geturl, headers=settings['headers'])
            for kommun in r.json()['soklista']['sokdata']:
                if kommun['namn'] == kom:
                    return(kommun)

def get_totals():
    lans = get_lans(None)
    slist = lans['soklista']
    r = {
        "totals": slist['totalt_antal_platsannonser'],
        "free": slist['totalt_antal_ledigajobb']
    }
    return(r)

if __name__ == '__main__':
    #opions -k --kommun
    if options.kom:
        if options.kom == 'all':
            kommuner = []
            get_kom('all')
            for kommun in kommuner:
                print(kommun)
        else:
            try:
                data = get_kom(options.kom)
                print(data['namn'], "(id: {})".format(data['id']))
                print('Antal platsannonser: {}'.format(data['antal_platsannonser']))
                print('Antal ledia jobb: {}'.format(data['antal_ledigajobb']))
            except:
                print("Kommunen du angav ({}) kunde inte hittas.".format(options.kom))

    #opions -t --total
    if options.total is not None:
        print("Totalt antal ledia jobb: {} \nTotalt antal platsannonser: {}".format(get_totals()['free'], get_totals()['totals']))

    #opions -l --lan
    if options.lan:
        if options.lan == 'all':
            for lan in get_lans(None)['soklista']['sokdata']:
                print(lan['namn'])
        else:
            try:
                data = get_lans(options.lan)
                print(data['namn'], "(id: {})".format(data['id']))
                print('Antal platsannonser: {}'.format(data['antal_platsannonser']))
                print('Antal ledia jobb: {}'.format(data['antal_ledigajobb']))
            except:
                print("Länet du angav ({}) kunde inte hittas.".format(options.lan))
