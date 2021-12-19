import requests
import xml.etree.ElementTree as ET
import multiprocessing


class UrlAgrigator:
    def __init__(self, url):
        self.urls = []
        self.GetLink(url)

    def GetHtml(self, link):
        # c = 0
        locUrl = []
        try:
            html_data = requests.get(link)
            myroot = ET.fromstring(html_data.text)
            for child in myroot:
                if 'loc' in child[0].tag:
                    if child[0].text.find('tags') == -1:
                        locUrl.append(child[0].text)
            # print(locUrl)
        except Exception as e:
            print(e)
        return locUrl

    def GetLink(self, url):
        count = 0

        try:
            xml_data = requests.get(url)
            if xml_data.status_code == 200:
                myroot = ET.fromstring(xml_data.text)
                for child in myroot:
                    if 'loc' in child[0].tag:
                        locUrls = self.GetHtml(child[0].text)
                        for i_u in locUrls:
                            self.urls.append(i_u)
            else:
                raise ConnectionRefusedError('[%s]: HtttpError: %d' % (url, xml_data.status_code))
            # print('[%s]: HtttpError: %d'%(url,xml_data.status_code))
            print(count)
        except ConnectionRefusedError as e:
            print(e)

        except Exception as e:
            print(e)
        return self.urls
