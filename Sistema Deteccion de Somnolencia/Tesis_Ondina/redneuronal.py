from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection

def crearRN():
    #Se crea la red neuronal
    n = FeedForwardNetwork()

    #Se declaran las laminas de entrada, las laminas escondidas y las de salida de la red neuronal
    inLayer = LinearLayer(4096)
    hiddenLayer = SigmoidLayer(3)
    outLayer = LinearLayer(1)

    #Se agregan los layers a la red neuronal
    n.addInputModule(inLayer)
    n.addModule(hiddenLayer)
    n.addOutputModule(outLayer)

    #Se declaran las conexiones de los nodos
    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)

    #Se establecen las conexiones en los layers de la red neuronal
    n.addConnection(in_to_hidden)
    n.addConnection(hidden_to_out)

    #Red neuronal lista para usar
    n.sortModules()

    return n

def crearRN1():
    #Se crea la red neuronal
    n = FeedForwardNetwork()

    #Se declaran las laminas de entrada, las laminas escondidas y las de salida de la red neuronal
    inLayer = LinearLayer(12288)
    hiddenLayer = SigmoidLayer(3)
    outLayer = LinearLayer(1)

    #Se agregan los layers a la red neuronal
    n.addInputModule(inLayer)
    n.addModule(hiddenLayer)
    n.addOutputModule(outLayer)

    #Se declaran las conexiones de los nodos
    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)

    #Se establecen las conexiones en los layers de la red neuronal
    n.addConnection(in_to_hidden)
    n.addConnection(hidden_to_out)

    #Red neuronal lista para usar
    n.sortModules()

    return n


def estimularRN(rn,matriz):
    """Se estimula la red neuronal, es decir, se ingresan los datos a ser procesados, en este caso
       es la imagen recortada de las areas que se desea estudiar"""
    if matriz == None:
        return None
    else:
        return rn.activate(matriz)

