import json
import urllib3
def lambda_handler(event, context):
    http = urllib3.PoolManager()
    API_URL = "https://ifconfig.me/"
    response = http.request("GET", API_URL)
    print(response.data)
    return {
        'statusCode': 200,
        'body': json.dumps('Ip Enviado para o Arquivo de LOG AWS')
    }
