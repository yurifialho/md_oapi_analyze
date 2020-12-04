from prance import ResolvingParser, ValidationError
import json, os
dataFolder = "dados"
fileJSONContent = []
count = 0
for filePath in os.listdir(dataFolder):
    try:
        parser = ResolvingParser(os.path.join(dataFolder,filePath),backend = 'openapi-spec-validator')
        fileJSONContent.append(parser.json())
        count += 1
    except ValidationError:
        print(f"{filePath} droped format invalid")
    
    if count == 5:
        break

print(json.loads(fileJSONContent[0])['info']['title'])
