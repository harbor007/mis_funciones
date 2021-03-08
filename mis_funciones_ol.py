

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