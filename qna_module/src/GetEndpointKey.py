########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
from Content import Content
from ConfigLoader import ConfigLoader
from BuildConfig import BuildConfig


class GetEndpoint(object):

    """ Obtiene el endpoint key para el config.yml """

    def __init__(self, content):
        self.content = content
        self.config = ConfigLoader(self.content)
        self.qna1key = self.config.get_section('qna1key')


    def get_endpoint(self):        
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': self.qna1key,
        }
        params = urllib.parse.urlencode({
        })
        try:
            conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("GET", "/qnamaker/v4.0/endpointkeys?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            data = Content().pretty_print_json(data)
            endpoint = data['primaryEndpointKey']
            write_conf = BuildConfig(self.content)
            write_conf.update('answer','endpointKey', endpoint)
            print("endpointKey: ",endpoint)
            print("Archivo config.yml actualizado.")
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('content', help='Contenido para crear la base de datos', default=False)
    args = parser.parse_args()

    GetEndpoint(args.content).get_endpoint()