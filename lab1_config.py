##################################
# Laboratory Server configuration #
##################################

laboratory_assigned_experiments = {
        'exp1:dummy@Dummy experiments' : {
                'coord_address' : 'experiment1:laboratory1@core_host',
                'checkers' : ()
            },
        'exp1:Prueba@Laboratorio de Prueba' : {
                'coord_address' : 'prueba:laboratory1@core_host',
                'checkers' : (), #Aqui se ponen cosas que hay que estar validando para asegurarse de que esta funcionando, como que la camara esta conectada y cosas asi mirar final del step2 de remote lab deployment 
                'api'      : '2',
            },
    }
