import profile as p

def tiempo():
    """Muestra el tiempo que tarda en culminarse cada uno de los modulos, estas estadisticas son utilizadas
       en las pruebas para una posible refactorizacion del codigo en caso de haber retrasos significativos en
       el procesamiento."""

    p.run('main')
    p.run('procesarImagen')
    p.run('deteccionFacial')
    p.run('deteccionFacial')
    p.run('deteccionOjos')

