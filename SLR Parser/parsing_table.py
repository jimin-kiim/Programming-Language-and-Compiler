parsing_table = [
    {'vtype':'s2', 'VDECL':1 },
    {'vtype':'s6', 'class': 's7', '$':'r3', 'CODE':3, 'VDECL':1, 'FDECL':4, 'CDECL':5},
    {'id':'s8','ASSIGN':9},
    {'$':'acc'},
    {'vtype':'s6', 'class':'s7', '$':'r3', 'CODE':10, 'VDECL':1, 'FDECL':4,'CDECL':5},
    {'vtype':'s6', 'class':'s7', '$':'r3', 'CODE':11, 'VDECL':1, 'FDECL':4,'CDECL':5},
    {'id':'s12', 'ASSIGN':9},
    {'id':'s13'},
    {'semi':'s14', 'assign':'s15'},
    {'semi':'s16'},
    {'$':'r1'},
    {'$':'r2'},
    {'semi':'s14', 'assign':'s15', 'lparen':'s17'},
    {'lbrace':'s18'}, 
    {'vtype':'r4', 'id':'r4', 'rbrace':'r4', 'if':'r4', 'while':'r4', 'return':'r4', 'class':'r4', '$':'r4'},
    {'id':'s25', 'literal':'s21', 'character':'s22', 'boolstr':'s23', 'lparen':'s24', 'num':'s26', 'RHS':19, 'EXPR':20},
    {'vtype':'r5', 'id':'r5','rbrace':'r5', 'if':'r5', 'while':'r5', 'return':'r5', 'class':'r5', '$':'r5'},
    {'vtype':'s28', 'rparen':'r18', 'ARG':27},
    {'vtype':'s6', 'rbrace':'r35', 'VDECL':30, 'FDECL':31, 'ODECL':29},
    {'semi':'r6'},
    {'semi':'r7'},
    {'semi':'r8'},
    {'semi':'r9'},
    {'semi':'r10'},
    {'id':'s25','lparen':'s24', 'num':'s26', 'EXPR':32},
    {'semi':'r14', 'addsub':'r14', 'rparen':'r14', 'multdiv':'r14'},
    {'semi':'r15', 'addsub':'r15', 'rparen':'r15', 'multdiv':'r15'},
    {'rparen':'s33'},
    {'id':'s34'},
    {'rbrace':'s35'},
    {'vtype':'s6', 'rbrace':'r35', 'CODE':30, 'FDECL':31, 'ODECL':36},
    {'vtype':'s6', 'rbrace':'r35', 'CODE':30, 'FDECL':31, 'ODECL':37},
    {'addsub':'s38', 'rparen':'s40', 'multdiv':'s39'},
    {'lbrace':'s41'},
    {'rparen':'r20', 'comma':'s43', 'MOREARGS':42},
    {'vtype':'r32', 'class':'r32', '$':'r32'},
    {'rbrace':'s33'},
    {'rbrace':'s34'},
    {'id':'s25', 'lparen':'s24', 'num':'s26', 'EXPR':44},
    {'id':'s25', 'lparen':'s24', 'num':'s26', 'EXPR':45},
    {'semi':'r13', 'addsub':'r13','rparen':'r13', 'multdiv':'r13'},
    {'vtype':'s2', 'id':'s52', 'rbrace':'r22', 'if':'s50', 'while':'s51', 'return':'r22', 'VDECL':48, 'ASSIGN':49, 'BLOCK':46, 'STMT':47},
    {'addsub':'r17'},
    {'vtype':'s53'},
    {'addsub':'s54'},
    {'addsub':'s55'},
    {'return':'s57', 'RETURN':56},
    {'vtype':'s2', 'id':'s52', 'rbrace':'r22', 'if':'s50', 'while':'s51', 'return':'r22', 'VDECL':48, 'ASSIGN':49, 'BLOCK':58, 'STMT':47},
    {'vtype':'s23', 'id':'s23', 'rbrace':'r23', 'if':'s23', 'while':'s23', 'return':'r23'},
    {'semi':'s59'},
    {'lparen':'s60'},
    {'lparen':'s61'},
    {'assign':'s15'},
    {'id':'s62'},
    {'semi':'r11', 'addsub':'r11', 'rparen':'r11', 'multdiv':'r11'},
    {'semi':'r12', 'addsub':'r12', 'rparen':'r12', 'multdiv':'r12'},
    {'rbrace':'s63'},
    {'id':'s25', 'literal':'s21', 'character':'s22', 'boolstr':'s23', 'lparen':'s24', 'num':'s26', 'RHS':64, 'EXPR':20},
    {'rbrace':'r21', 'return':'r21'},
    {'vtype':'r24', 'id':'r24', 'rbrace':'r24', 'if':'r24', 'while':'r24', 'return':'r24'},
    {'boolstr':'s67', 'lparen':'s66', 'COND':65},
    {'boolstr':'s67', 'lparen':'s66', 'COND':68},
    {'rparen':'r20', 'comma':'s43', 'MOREARGS':69},
    {'vtype':'r16', 'rbrace':'r16', 'class':'r16', '$':'r16'},
    {'semi':'s70'},
    {'rparen':'s71'},
    {'boolstr':'s67', 'lparen':'s66', 'COND':72},
    {'rparen':'r28', 'comp':'r28'},
    {'rparen':'s73'},
    {'rparen':'r19'},
    {'rbrace':'r31'},
    {'lbrace':'s74'},
    {'comp':'s75'},
    {'lbrace':'s76'},
    {'vtype':'s2', 'id':'s52', 'rbrace':'r22', 'if':'s50', 'while':'s51', 'return':'r22', 'VDECL':48, 'ASSIGN':49, 'BLOCK':77, 'STMT':47},
    {'boolstr':'s67', 'lparen':'s66', 'COND':78},
    {'vtype':'s2', 'id':'s52', 'rbrace':'r22', 'if':'s50', 'while':'s51', 'return':'r22', 'VDECL':48, 'ASSIGN':49, 'BLOCK':79, 'STMT':47},
    {'rbrace':'s80'},
    {'rparen':'s81'},
    {'rbrace':'s82'},
    {'vtype':'r30', 'id':'r30', 'rbrace':'r30', 'if':'r30', 'while':'r30', 'else':'s84', 'return':'r30', 'ELSE':83},
    {'rparen':'r27', 'comp':'r27'},
    {'vtype':'r26', 'id':'r26', 'rbrace':'r26', 'if':'r26', 'while':'r26', 'return':'r26'},
    {'vtype':'r25', 'id':'r25', 'rbrace':'r25', 'if':'r25', 'while':'r25', 'return':'r25'},
    {'lbrace':'s85'},
    {'vtype':'s2', 'id':'s52', 'rbrace':'r22', 'if':'s50', 'while':'s51', 'return':'r22', 'VDECL':48, 'ASSIGN':49, 'BLOCK':86, 'STMT':47},
    {'rbrace':'s87'},
    {'vtype':'r29', 'id':'r29', 'rbrace':'r29', 'if':'r29', 'while':'r29', 'return':'r29'}
]