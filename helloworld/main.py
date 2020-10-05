def hello_world(request):
    if request.method == 'OPTIONS':
        #Resolvendo o problema de CORS
        headers = {
            'Access-Control-Allow-Origin':'*', # especifique o dom'inio para restringir ou use * para todos.
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600' # cache temporario para o header de 1 hora
        }
        return '', 204, headers
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    request_args = request.args
    request_json = request.get_json(silent=True) # sem jason send null => "silent = True"
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'world'
        lastname = ''
    return f'Hello {name} {lastname}', 200, headers