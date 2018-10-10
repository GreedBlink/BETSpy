

def connection():
    try:
        conn = mysql.connector.connect(host ='',
                                       database='',
                                       user = '',
                                       password='')
        if conn.is_connected():
    except Error as e:
        print(e)
    finally:    
        conn.close()
            
    return()


    
def BETSsearch(description='*',src,periodicity,unit,code,start,lang='en'):
    conn = connection()
    
    if(lang == 'en'):
        tb = 'metadata_en'
    else:
        tb = 'metada_pt'
        
    if(description == '*'):
        return(print('No search parameters. Please set the values of one or more parameters'))
    return()
    
def getSeriesBacen(x = None, start = '', to = '',save = ''):
    
    if(x is None):
        return('Need to specify at least one series.')
    
        
    if(start == ""):
        data_init = '01/01/1980'
    else:
        data_init = start
          
    if(to == ""):
        data_end = datetime.datetime.now()
        data_end = data_end.strftime("%d/%m/%Y")
    else:
        data_end = to
          
    inputs = list(str(x))
    tamanho = range(len(inputs))
    serie = 'series_' + str(inputs)
    dict_ts =  {}   
    for i in tamanho:
        try:
           k = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.' + str(inputs[i]) +  '/dados?formato=json&dataInicial=' + str(data_init) + '&dataFinal=' + str(data_end)   
           r = requests.get(k)
        except: 
            time.sleep(2)
            k = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.' + str(inputs[i]) +  '/dados?formato=json&dataInicial=' + str(data_init) + '&dataFinal=' + str(data_end)   
            r = requests.get(k)
        dados = pd.read_json(r.content)
        dict_ts.update({str(serie): dados})
    return(dict_ts)


def getSeries(code, start = '', to = '', df = False, frequency = None):
    return()

def BETSget(code, start = '', to = '', df = False, frequency = None):
    n = len(code)
    f = len(start)
    t = len(to)
    
    if(n > 1):
        ts = []
        nms = []
        
        if(f == 1 and t == 1):
            for i in range(n):
              ts[i] =   getSeries()
    return()

