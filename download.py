import wget
import json

json_file_path = "/home/edupooch/projects/libras/acessibilidade.json"
base_url = "http://www.acessibilidadebrasil.org.br/libras_3/public/media/palavras/videos/"
with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

for content in contents:
    print(content['video'])
    wget.download(base_url + content["video"])