

user_input_detail = '''Function to request user input, customizng the title of the pop up window,
and the prompt on the window itself, returning the value entered.'''

update_id_detail = ''' Function to request user input details on update details.'''

dict_functions = {'user_input':user_input_detail,
                  'update_id':update_id_detail}


def list_functions(extended=False):
    if extended == True:
        for key, value in dict_functions.items():
            print(key + '\n')
            print(value + '\n')
    else:
        for key, value in dict_functions.items():
            print(key)

def user_input(pop_up_title, pop_up_prompt):
    ''' Function to request user input, customizing the title of the pop up window,
    and the prompt on the window itself, returning the value entered. 
    
    pop_up_title: Pop up window title.
    pop_up_prompt: Pop up window prompt that shows up. \n
    '''

    import tkinter as tk
    from tkinter import simpledialog
    
    root = tk.Tk()
    root.withdraw()
    
    ask_user_input = simpledialog.askstring(title=pop_up_title, prompt=pop_up_prompt)
    
    return ask_user_input


def update_id(periodo_req = True, semestre_req = True, generación_req = True, carpeta_req = True, version_req = True):
    ''' Function to request user input details on update details.  
        Solicita el periodo, semestre, generación, y carpeta.
        Para cancelar se solicite un valor camibar el parametro x_req = False.
        
        Donde x, puedes ser: periodo, semestre, generación o carpeta
        
        version 1.0
    '''
    dict_id_actualización = {}

    if periodo_req == True:
        periodo = user_input(pop_up_title='Periodo o ciclo de actualización',
                             pop_up_prompt='''Favor de indicar el ciclo o periodo de actualización. \nEjemplo:\n Fin de 3er Periodo''')
        dict_id_actualización['periodo'] = periodo
    else:
        pass
    
    if version_req == True:
        version = user_input(pop_up_title='Version de actualización',
                             pop_up_prompt='''Favor de indicar la version del codigo de esta actualización. \nEjemplo:\n 5.1''')
        dict_id_actualización['version'] = version
    else:
        pass

    if semestre_req == True:
        semestre_req = user_input(pop_up_title='Semestre de actualización',
                                  pop_up_prompt='''Favor de indicar el semestre o periodo de actualización. \nEjemplo:\n   AD20''')
        dict_id_actualización['semestre'] = semestre
    else:
        pass

    if generación_req == True:    
        generación = user_input(pop_up_title='Generación actualizada',
                                pop_up_prompt='''Favor de indicar la generación para la cual se realiza la actualización. \nEjemplo:\n   PINAD20''')
        dict_id_actualización['generación'] = generación
    else:
        pass
    
    if carpeta_req == True:
        carpeta = user_input(pop_up_title='Nombre de carpeta',
                             pop_up_prompt='''Favor de indicar el nombre de la carpeta donde se almacena \nla información de la actualización de la generación ''' + generación + '\nen la cual se realiza la actualización. \n\nEjemplo:\n   20201204 Fin P3 semestre AD20\n''')
        dict_id_actualización['carpeta'] = carpeta
    else:
        pass
    return dict_id_actualización

def notificacion(file_name, resultado, new_file=False):
    global nombre_carpeta, notificador_version
    """
    notificacion(file_name, resultado)
    """
    if new_file == True:
        consecutivo_notificador(notificador_version)
    else:
        pass
    
    file = open(nombre_carpeta + '/' + notificador_version,"a")
    msg_comp = file_name + resultado + '\n'
    file.write(msg_comp)
    file.close()  

def consecutivo_notificador(notificador, fecha = run_date):
    global nombre_carpeta, notificador_version
    archivos_inicio = os.listdir(nombre_carpeta)
    version = int(os.path.splitext(notificador)[0][-2:])
    if notificador in archivos_inicio:
        if version >= 10:
            j = version + 1
            notificador_version = os.path.splitext(notificador)[0][:-2] + str(j) + '.txt'
            consecutivo_notificador(notificador_version)
        else:
            j = version + 1
            notificador_version = os.path.splitext(notificador)[0][:-2] + '0' + str(j) + '.txt'
            consecutivo_notificador(notificador_version)
    else:
        notificador_version = notificador_version
    return notificador_version

def escribir_consecutivo(base, nombre_archivo):
    if nombre_archivo in os.listdir(nombre_carpeta):
        print('Ya existe, cambie la version')
        pass
    else:
        base.to_excel(nombre_carpeta + '/' + nombre_archivo, index=False)
        print('Se escribio la base ' + str(nombre_archivo))

def escribir_imagen(nombre_archivo, tipo):
    if nombre_archivo in os.listdir(nombre_carpeta):
        print('Ya existe esta version de imagen, cambie la version para guardar el archivo.')
        pass
    else:
        if tipo == 'plt':
            plt.savefig(nombre_carpeta + '/' + nombre_imagen, bbox_inches='tight', dpi=800)
            print('Se guardo la imagen ' + str(nombre_archivo))
        elif tipo == 'sns':
            sns_plot = sns.heatmap(df_ft_imp, vmin=0.025, vmax=df_ft_imp.max().max(), cmap="viridis")
            sns_plot.figure.savefig(nombre_carpeta + '/' + nombre_archivo, bbox_inches='tight', dpi=800)
            print('Se guardo la imagen ' + str(nombre_archivo))
        else:
            print('Defina el tipo de imagen')