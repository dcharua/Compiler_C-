
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CLOSEBRACE CLOSEBRACKET CLOSEPAR COMMA DIV ELSE ENDFILE EQ GREATER GREATEREQ ID IF INT LESSER LESSEREQ MINUS MULT NOTEQ NUM OPENBRACE OPENBRACKET OPENPAR PLUS RETURN SEMICOLON VOID WHILEprogram : declaration_list ENDFILEdeclaration_list : declaration_list declarationdeclaration_list : declarationdeclaration : fun_declarationdeclaration : var_declarationvar_declaration : type_specifier ID OPENBRACKET NUM CLOSEBRACKET SEMICOLONvar_declaration : type_specifier ID SEMICOLONtype_specifier : INT \n  | VOIDfun_declaration : type_specifier ID OPENPAR params CLOSEPAR compound_stmtparams : param_list\n  | VOIDparam_list : param_list COMMA paramparam_list : paramparam : type_specifier IDparam : type_specifier ID OPENBRACKET CLOSEBRACKETcompound_stmt : OPENBRACE local_declarations statement_list CLOSEBRACElocal_declarations : local_declarations var_declarationlocal_declarations :statement_list : statement_list statementstatement_list :statement : compound_stmt\n  | expression_stmt\n  | selection_stmt\n  | iteration_stmt\n  | return_stmtexpression_stmt : expression SEMICOLON\n  | SEMICOLONselection_stmt : IF OPENPAR expression CLOSEPAR statementselection_stmt : IF OPENPAR expression CLOSEPAR statement ELSE statementiteration_stmt : WHILE OPENPAR expression CLOSEPAR statementreturn_stmt : RETURN SEMICOLONreturn_stmt : RETURN expression SEMICOLONexpression : var ASSIGN expressionexpression : simple_expressionsimple_expression : additive_expression relop additive_expressionsimple_expression : additive_expressionrelop : LESSER\n  | LESSEREQ\n  | GREATER\n  | GREATEREQ\n  | EQ\n  | NOTEQadditive_expression : additive_expression addop termadditive_expression : termaddop : PLUS\n  | MINUSterm : term mulop factorterm : factormulop : MULT\n  | DIVfactor : varfactor : callfactor : NUMfactor : OPENPAR expression CLOSEPARcall : ID OPENPAR args CLOSEPARargs : arg_listargs :arg_list : arg_list COMMA expressionarg_list : expressionvar : IDvar : ID OPENBRACKET expression CLOSEBRACKET'
    
_lr_action_items = {'INT':([0,2,3,4,5,10,12,14,23,26,27,29,31,33,35,],[7,7,-3,-4,-5,-2,7,-7,7,-10,-19,-6,7,-18,-17,]),'VOID':([0,2,3,4,5,10,12,14,23,26,27,29,31,33,35,],[8,8,-3,-4,-5,-2,18,-7,8,-10,-19,-6,8,-18,-17,]),'$end':([1,9,],[0,-1,]),'ENDFILE':([2,3,4,5,10,14,26,29,35,],[9,-3,-4,-5,-2,-7,-10,-6,-17,]),'ID':([6,7,8,14,15,18,27,29,31,32,33,34,35,36,37,38,39,40,41,43,45,47,57,58,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,92,93,96,97,98,100,101,],[11,-8,-9,-7,21,-9,-19,-6,-21,50,-18,56,-17,-20,-22,-23,-24,-25,-26,-28,50,50,-27,50,50,-32,50,50,50,50,50,-38,-39,-40,-41,-42,-43,-46,-47,50,-50,-51,-33,50,50,50,-29,-31,50,-30,]),'OPENPAR':([11,14,27,29,31,32,33,35,36,37,38,39,40,41,43,44,45,46,47,50,57,58,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,92,93,96,97,98,100,101,],[12,-7,-19,-6,-21,45,-18,-17,-20,-22,-23,-24,-25,-26,-28,58,45,60,45,65,-27,45,45,-32,45,45,45,45,45,-38,-39,-40,-41,-42,-43,-46,-47,45,-50,-51,-33,45,45,45,-29,-31,45,-30,]),'OPENBRACKET':([11,21,50,56,],[13,25,64,13,]),'SEMICOLON':([11,14,24,27,29,31,32,33,35,36,37,38,39,40,41,42,43,47,48,49,50,51,52,53,54,55,56,57,61,62,80,82,83,88,89,90,91,92,93,94,95,97,98,100,101,],[14,-7,29,-19,-6,-21,43,-18,-17,-20,-22,-23,-24,-25,-26,57,-28,61,-52,-35,-61,-37,-45,-49,-53,-54,14,-27,-32,82,-55,-33,-34,-36,-52,-44,-48,43,43,-62,-56,-29,-31,43,-30,]),'NUM':([13,14,27,29,31,32,33,35,36,37,38,39,40,41,43,45,47,57,58,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,92,93,96,97,98,100,101,],[20,-7,-19,-6,-21,55,-18,-17,-20,-22,-23,-24,-25,-26,-28,55,55,-27,55,55,-32,55,55,55,55,55,-38,-39,-40,-41,-42,-43,-46,-47,55,-50,-51,-33,55,55,55,-29,-31,55,-30,]),'CLOSEBRACE':([14,27,29,31,32,33,35,36,37,38,39,40,41,43,57,61,82,97,98,101,],[-7,-19,-6,-21,35,-18,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,-29,-31,-30,]),'OPENBRACE':([14,22,27,29,31,32,33,35,36,37,38,39,40,41,43,57,61,82,92,93,97,98,100,101,],[-7,27,-19,-6,-21,27,-18,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,27,27,-29,-31,27,-30,]),'IF':([14,27,29,31,32,33,35,36,37,38,39,40,41,43,57,61,82,92,93,97,98,100,101,],[-7,-19,-6,-21,44,-18,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,44,44,-29,-31,44,-30,]),'WHILE':([14,27,29,31,32,33,35,36,37,38,39,40,41,43,57,61,82,92,93,97,98,100,101,],[-7,-19,-6,-21,46,-18,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,46,46,-29,-31,46,-30,]),'RETURN':([14,27,29,31,32,33,35,36,37,38,39,40,41,43,57,61,82,92,93,97,98,100,101,],[-7,-19,-6,-21,47,-18,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,47,47,-29,-31,47,-30,]),'CLOSEPAR':([16,17,18,19,21,28,30,48,49,50,51,52,53,54,55,59,65,79,80,81,83,85,86,87,88,89,90,91,94,95,99,],[22,-11,-12,-14,-15,-13,-16,-52,-35,-61,-37,-45,-49,-53,-54,80,-58,92,-55,93,-34,95,-57,-60,-36,-52,-44,-48,-62,-56,-59,]),'COMMA':([17,19,21,28,30,48,49,50,51,52,53,54,55,80,83,86,87,88,89,90,91,94,95,99,],[23,-14,-15,-13,-16,-52,-35,-61,-37,-45,-49,-53,-54,-55,-34,96,-60,-36,-52,-44,-48,-62,-56,-59,]),'CLOSEBRACKET':([20,25,48,49,50,51,52,53,54,55,80,83,84,88,89,90,91,94,95,],[24,30,-52,-35,-61,-37,-45,-49,-53,-54,-55,-34,94,-36,-52,-44,-48,-62,-56,]),'ELSE':([35,37,38,39,40,41,43,57,61,82,97,98,101,],[-17,-22,-23,-24,-25,-26,-28,-27,-32,-33,100,-31,-30,]),'ASSIGN':([48,50,94,],[63,-61,-62,]),'MULT':([48,50,52,53,54,55,80,89,90,91,94,95,],[-52,-61,77,-49,-53,-54,-55,-52,77,-48,-62,-56,]),'DIV':([48,50,52,53,54,55,80,89,90,91,94,95,],[-52,-61,78,-49,-53,-54,-55,-52,78,-48,-62,-56,]),'LESSER':([48,50,51,52,53,54,55,80,89,90,91,94,95,],[-52,-61,68,-45,-49,-53,-54,-55,-52,-44,-48,-62,-56,]),'LESSEREQ':([48,50,51,52,53,54,55,80,89,90,91,94,95,],[-52,-61,69,-45,-49,-53,-54,-55,-52,-44,-48,-62,-56,]),'GREATER':([48,50,51,52,53,54,55,80,89,90,91,94,95,],[-52,-61,70,-45,-49,-53,-54,-55,-52,-44,-48,-62,-56,]),'GREATEREQ':([48,50,51,52,53,54,55,80,89,90,91,94,95,],[-52,-61,71,-45,-49,-53,-54,-55,-52,-44,-48,-62,-56,]),'EQ':([48,50,51,52,53,54,55,80,89,90,91,94,95,],[-52,-61,72,-45,-49,-53,-54,-55,-52,-44,-48,-62,-56,]),'NOTEQ':([48,50,51,52,53,54,55,80,89,90,91,94,95,],[-52,-61,73,-45,-49,-53,-54,-55,-52,-44,-48,-62,-56,]),'PLUS':([48,50,51,52,53,54,55,80,88,89,90,91,94,95,],[-52,-61,74,-45,-49,-53,-54,-55,74,-52,-44,-48,-62,-56,]),'MINUS':([48,50,51,52,53,54,55,80,88,89,90,91,94,95,],[-52,-61,75,-45,-49,-53,-54,-55,75,-52,-44,-48,-62,-56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,10,]),'fun_declaration':([0,2,],[4,4,]),'var_declaration':([0,2,31,],[5,5,33,]),'type_specifier':([0,2,12,23,31,],[6,6,15,15,34,]),'params':([12,],[16,]),'param_list':([12,],[17,]),'param':([12,23,],[19,28,]),'compound_stmt':([22,32,92,93,100,],[26,37,37,37,37,]),'local_declarations':([27,],[31,]),'statement_list':([31,],[32,]),'statement':([32,92,93,100,],[36,97,98,101,]),'expression_stmt':([32,92,93,100,],[38,38,38,38,]),'selection_stmt':([32,92,93,100,],[39,39,39,39,]),'iteration_stmt':([32,92,93,100,],[40,40,40,40,]),'return_stmt':([32,92,93,100,],[41,41,41,41,]),'expression':([32,45,47,58,60,63,64,65,92,93,96,100,],[42,59,62,79,81,83,84,87,42,42,99,42,]),'var':([32,45,47,58,60,63,64,65,66,67,76,92,93,96,100,],[48,48,48,48,48,48,48,48,89,89,89,48,48,48,48,]),'simple_expression':([32,45,47,58,60,63,64,65,92,93,96,100,],[49,49,49,49,49,49,49,49,49,49,49,49,]),'additive_expression':([32,45,47,58,60,63,64,65,66,92,93,96,100,],[51,51,51,51,51,51,51,51,88,51,51,51,51,]),'term':([32,45,47,58,60,63,64,65,66,67,92,93,96,100,],[52,52,52,52,52,52,52,52,52,90,52,52,52,52,]),'factor':([32,45,47,58,60,63,64,65,66,67,76,92,93,96,100,],[53,53,53,53,53,53,53,53,53,53,91,53,53,53,53,]),'call':([32,45,47,58,60,63,64,65,66,67,76,92,93,96,100,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'relop':([51,],[66,]),'addop':([51,88,],[67,67,]),'mulop':([52,90,],[76,76,]),'args':([65,],[85,]),'arg_list':([65,],[86,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list ENDFILE','program',2,'p_program','Parser.py',12),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','Parser.py',18),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list2','Parser.py',30),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','Parser.py',36),
  ('declaration -> var_declaration','declaration',1,'p_declaration2','Parser.py',40),
  ('var_declaration -> type_specifier ID OPENBRACKET NUM CLOSEBRACKET SEMICOLON','var_declaration',6,'p_var_declaration','Parser.py',46),
  ('var_declaration -> type_specifier ID SEMICOLON','var_declaration',3,'p_var_declaration2','Parser.py',50),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','Parser.py',56),
  ('type_specifier -> VOID','type_specifier',1,'p_type_specifier','Parser.py',57),
  ('fun_declaration -> type_specifier ID OPENPAR params CLOSEPAR compound_stmt','fun_declaration',6,'p_fun_declaration','Parser.py',63),
  ('params -> param_list','params',1,'p_params','Parser.py',69),
  ('params -> VOID','params',1,'p_params','Parser.py',70),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','Parser.py',76),
  ('param_list -> param','param_list',1,'p_param_list2','Parser.py',88),
  ('param -> type_specifier ID','param',2,'p_param','Parser.py',94),
  ('param -> type_specifier ID OPENBRACKET CLOSEBRACKET','param',4,'p_param2','Parser.py',98),
  ('compound_stmt -> OPENBRACE local_declarations statement_list CLOSEBRACE','compound_stmt',4,'p_compound_stmt','Parser.py',104),
  ('local_declarations -> local_declarations var_declaration','local_declarations',2,'p_local_declarations','Parser.py',110),
  ('local_declarations -> <empty>','local_declarations',0,'p_local_declarations2','Parser.py',119),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','Parser.py',125),
  ('statement_list -> <empty>','statement_list',0,'p_statement_list2','Parser.py',135),
  ('statement -> compound_stmt','statement',1,'p_statement','Parser.py',141),
  ('statement -> expression_stmt','statement',1,'p_statement','Parser.py',142),
  ('statement -> selection_stmt','statement',1,'p_statement','Parser.py',143),
  ('statement -> iteration_stmt','statement',1,'p_statement','Parser.py',144),
  ('statement -> return_stmt','statement',1,'p_statement','Parser.py',145),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt','Parser.py',152),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt','Parser.py',153),
  ('selection_stmt -> IF OPENPAR expression CLOSEPAR statement','selection_stmt',5,'p_selection_stmt','Parser.py',160),
  ('selection_stmt -> IF OPENPAR expression CLOSEPAR statement ELSE statement','selection_stmt',7,'p_selection_stmt2','Parser.py',164),
  ('iteration_stmt -> WHILE OPENPAR expression CLOSEPAR statement','iteration_stmt',5,'p_iteration_stmt','Parser.py',170),
  ('return_stmt -> RETURN SEMICOLON','return_stmt',2,'p_return_stmt','Parser.py',176),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt2','Parser.py',180),
  ('expression -> var ASSIGN expression','expression',3,'p_expression','Parser.py',187),
  ('expression -> simple_expression','expression',1,'p_expression2','Parser.py',199),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression','Parser.py',205),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression2','Parser.py',209),
  ('relop -> LESSER','relop',1,'p_relop','Parser.py',215),
  ('relop -> LESSEREQ','relop',1,'p_relop','Parser.py',216),
  ('relop -> GREATER','relop',1,'p_relop','Parser.py',217),
  ('relop -> GREATEREQ','relop',1,'p_relop','Parser.py',218),
  ('relop -> EQ','relop',1,'p_relop','Parser.py',219),
  ('relop -> NOTEQ','relop',1,'p_relop','Parser.py',220),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression','Parser.py',226),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression2','Parser.py',230),
  ('addop -> PLUS','addop',1,'p_addop','Parser.py',236),
  ('addop -> MINUS','addop',1,'p_addop','Parser.py',237),
  ('term -> term mulop factor','term',3,'p_term','Parser.py',243),
  ('term -> factor','term',1,'p_term2','Parser.py',249),
  ('mulop -> MULT','mulop',1,'p_mulop','Parser.py',253),
  ('mulop -> DIV','mulop',1,'p_mulop','Parser.py',254),
  ('factor -> var','factor',1,'p_factor','Parser.py',260),
  ('factor -> call','factor',1,'p_factor2','Parser.py',264),
  ('factor -> NUM','factor',1,'p_factor3','Parser.py',268),
  ('factor -> OPENPAR expression CLOSEPAR','factor',3,'p_factor4','Parser.py',272),
  ('call -> ID OPENPAR args CLOSEPAR','call',4,'p_call','Parser.py',278),
  ('args -> arg_list','args',1,'p_args','Parser.py',286),
  ('args -> <empty>','args',0,'p_args2','Parser.py',290),
  ('arg_list -> arg_list COMMA expression','arg_list',3,'p_arg_list','Parser.py',294),
  ('arg_list -> expression','arg_list',1,'p_arg_list2','Parser.py',306),
  ('var -> ID','var',1,'p_var','Parser.py',310),
  ('var -> ID OPENBRACKET expression CLOSEBRACKET','var',4,'p_var2','Parser.py',314),
]
