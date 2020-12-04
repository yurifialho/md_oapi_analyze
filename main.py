import requests, json
from pathvalidate import sanitize_filename
from logger import Logger
class Main:

    def __init__(self):
        self.logger = Logger.getLogger(__name__)
        self.baseSwaggerHubUrl = "https://api.swaggerhub.com/specs"
        self.page = 0
        self.regPerPage = 100
        self.doConnect = True

    def run(self):
        self.bringListApi()

    def getSwaggerUrl(self, properties):

        for prop in properties:
            if prop['type'] == 'Swagger':
                return prop['url']

    def bringListApi(self):
        count = 10000
        self.logger.debug('Trying retreave some informations from Swagger Hub')
        while self.doConnect:
            res = requests.get(f'{self.baseSwaggerHubUrl}?specType=API&limit={self.regPerPage}&state=PUBLISHED&page={self.page}&sort=NAME&order=DESC')
            if res.status_code == 200:
                self.logger.debug('Retrived information from Swagger Hub')
                apiInfo = res.json()
                totalReg = apiInfo['totalCount']
                apis = apiInfo['apis']
                for api in apis:
                    if count <= -1:
                        count += 1
                    else:
                        apiName = sanitize_filename(api['name'])
                        urlSwagger = self.getSwaggerUrl(api['properties'])
                        self.logger.info(f"{apiName} -> {urlSwagger}")
                        swagger = requests.get(urlSwagger).json()
                        with open(f'dados/{count}-{apiName}.json','w', encoding="utf-8") as f:
                            print(swagger, file=f)
                        count += 1
                if count < totalReg:
                    self.page+=1
                    self.doConnect = True
                else:
                    self.doConnect = False






main = Main()
main.run()