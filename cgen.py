from semantica import *

def codeGen(tree, file):
    fw = FileWriter(file) 
    fw.openFile()
    table = tabla(tree, False)
    compileCode(tree, table, fw)



class FileWriter(object):
    def __init__(self, file):
        self.file = file

    def openFile(self):
        self.f = open(self.file, "w+")

    def closeFile(self):
        self.f.close()
    
    def write(self, text):
        self.f.write(text)

def compileCode(node, table, fw):
    if node[0] is 'declaration_list':
        for child in node[1:]:
            compileCode(child, table, fw)
    
    elif node[0] is 'variable_declaration':    
        varType  = node[1]          
        varId   = node[2]
        return 

    elif node[0] is 'function_declaration':    
        returns  = node[1]          
        functionID   = node[2]
        if node[3] != 'void':
            params = node[3][1:]
        else:
            params = 'void'
    elif node[0] is 'number':
     

    elif node[0] is 'var':


    elif node[0] is 'function_call':
       

    elif node[0] in ['==', '!=', '<=', '<', '>=', '>', '+', '-', '*', '/', '=']:
       

    elif node[0] is 'iteration_stmt':
       

    elif node[0] is 'selection_stmt':
       

    elif node[0] is 'return_stmt':
        

    else:
        for child in node[1:]:
            if type(child) is list:
                build_table(child, table, returns)

        
       