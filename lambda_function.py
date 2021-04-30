import re

def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    uri = request['uri']

    if re.match('.+/$', uri):
        request['uri'] = uri + "index.html"
        return request

    elif re.match('(.+)/index.html', uri):
        prefix_path = re.search('(.+)/index.html', uri)
        response = {
            'status': '301',
            'statusDescription': 'Found',
            'headers': {
                'location': [{
                    'key': 'Location',
                    'value': prefix_path[1] + '/'
                }]
            }
        }
        return response

    elif re.search('\/[^\/\.]+$', uri):
        response = {
            'status': '301',
            'statusDescription': 'Found',
            'headers': {
                'location': [{
                    'key': 'Location',
                    'value': uri + '/'
                }]
            }
        }
        return response

    else:
        return request
