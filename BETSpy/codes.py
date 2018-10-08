

def connection():
    return()


    
def BETSsearch():
    return()
    
def getSeriesBacen(x = None, strat = '', to = '',save = ''):
    
    if(x is None):
        return('Need to specify at least one series.')
    
        
    if (start == ""):
        data_init = '01/01/1980'
    else:
        data_init = start
          
    if (to == ""):
        data_end = datetime.datetime.now()
        data_end = data_end.strftime("%d/%m/%Y")
    else:
        data_end = to
          
    inputs = [str(x)]
    tamanho = range(len(inputs))
    serie = "serie_" + inputs 
        
    for i in tamanho:
        try:
           k = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.' + str(inputs[i]) +  '/dados?formato=csv&dataInicial=' + str(data_init) + '&dataFinal=' + str(data_end)
           r = requests.get(k)
           aux = r.raw
           
         
        
        
             
        DF <- data.frame(do.call(cbind, strsplit(aux2, "\r\n", fixed=TRUE)))
        names(DF) <- "mist"
        DF$mist   <- as.character(DF$mist)
        DF$mist   <- gsub(x = DF$mist,pattern = '"',replacement = "")
        DF$data   <- gsub(x = DF$mist,pattern = ";.*",replacement = "")
        DF$valor  <- gsub(x = DF$mist,pattern = ".*;",replacement = "")
        DF$valor  <- gsub(x = DF$valor,pattern = ",",replacement = ".")
        DF <- DF[-1,-1]
         })}
         assign(serie[i], DF)
         rm(DF, texto)
          
        
          lista = list()
          ls_df = ls()[grepl('data.frame', sapply(ls(), function(x) class(get(x))))]
          for ( obj in ls_df ) { lista[obj]=list(get(obj))}

    
    return()


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

