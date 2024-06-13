"Carlos Murillo Aguilar"
import random
import math
"Clases y funciones"
class Nodo:
    def __init__(self, i):
        self.idn=i              # Crear objeto nodo, conformado solo por
                                #  su identificador numérico
class Arista:
    def __init__(self, a, b):
        self.arista=[Nodo(a),Nodo(b)]# Crear objeto arista, conformado por una 
                                     #  lista de dos nodos
def Color():    
    r = random.randrange(0, 254, 23)  # Función para generar colores aleatorios
    g = random.randrange(0, 254, 23)
    b = random.randrange(0, 254, 23)    
    return '"#{:02x}{:02x}{:02x}"'.format(r, g, b)

class Grafo:
    def __init__(self):            # Crear objeto grafo, conformado por una 
        self.nodos=[]              #  lista de los identificadores de cada nodo
        self.aristas=[]            #  y una lista de parejas de identificadores
                                   #  de cada nodo en cada arista
    def agregarNodo(self, n):
        if n not in self.nodos:
            nodo=Nodo(n)
            self.nodos.append(nodo.idn)
            
    def agregarArista(self, e1, e2):
        if e1 in self.nodos and e2 in self.nodos and [e1, e2] not in self.aristas and [e2, e1] not in self.aristas:
            aristaIds=Arista(e1, e2)
            self.aristas.append([aristaIds.arista[0].idn,  aristaIds.arista[1].idn])
            # self.aristas.append([aristaIds.arista[1].idn,  aristaIds.arista[0].idn])
    
    def generar_archivo(self, tipo_de_grafo, T, exp_aristas):         #Se define el nombre del archivo
        if tipo_de_grafo==1:
            s=open("Grafo de Malla.gv","w")
        elif tipo_de_grafo==2:
            s=open("Grafo de Erdös y Rényi.gv","w")
        elif tipo_de_grafo==3:
            s=open("Grafo de Gilbert.gv","w")
        elif tipo_de_grafo==4:
            s=open("Grafo Geográfico Simple.gv","w")
        elif tipo_de_grafo==5:
            s=open("Grafo Barabási-Albert.gv","w")
        elif tipo_de_grafo==6:
            s=open("Grafo Dorogovtsev-Mendes.gv","w")
        elif tipo_de_grafo==7:
            s=open("Grafo BFS.gv","w")
        elif tipo_de_grafo==8:
            s=open("Grafo DFS-R.gv","w")
        elif tipo_de_grafo==9:
            s=open("Grafo DFS-I.gv","w")
        elif tipo_de_grafo==10:
            s=open("Grafo Dijkstra.gv","w")
        elif tipo_de_grafo==11:
            s=open("Grafo Kruskal-D.gv","w")
        elif tipo_de_grafo==12:
            s=open("Grafo Kruskal-I.gv","w")
        elif tipo_de_grafo==13:
            s=open("Grafo Prim.gv","w")
        
        s.write("digraph sample {\n")
        
        if tipo_de_grafo == 7:           # Para cada tipo de árbol se aplica un coloreado diferente
            for l in range(len(T)):
                c=Color()
                for n in T[l]:
                    w=(str(n) + " [color=" + str(c) + "];\n")
                    # print(w)
                    s.write(w)          # Para el árbol BFS se colorea cada capa y se eliminan
                                         #  las aristas que unan nodos de la misma capa
        if tipo_de_grafo == 8:
            c=[]
            b=[]
            self.color_R(T, c, b)
            print (c)                   # Para el árbol DFSR se coloréan las ramas n 
            print (b)                   #  dependiendo de que turno de elección fueron durante
            for bif in range(len(b)):   #  la búsqueda
                for r in b[bif]:
                    w=(str(r) + " [color=" + str(c[bif]) + "];\n")
                    s.write(w)
                    
        if tipo_de_grafo == 9:
            c=[]
            b=[]
            self.color_I(T, c, b)       # Para el árbol DFSI se colorean también las ramas,
            print (c)                   #  sin embargo, dado el algorítmo de búsqueda, 
            print (b)                   #  se colorean las ramas desde la bifurcación original
            col=[]                      #  hasta que una nueva se encuentre
            col_list=[]
            for bif in range(len(b)):
                w=(str(b[bif]) + " [color=" + str(c[bif]) + "];\n")
                s.write(w)
                col_list.append([b[bif], c[bif]])
            for n in range(len(T)):
                for bif in range(len(b)):
                    if T[n][0] == b[bif] and T[n][1] not in b:
                        w=(str(T[n][1]) + " [color=" + str(c[bif]) + "];\n")
                        s.write(w)
                        col_list.append([T[n][1], c[bif]])
                        
                    elif T[n][0] not in b and T[n][1] not in b \
                                          and T[n][1] not in col:
                        for clr in range(len(col_list)):
                            if T[n][0]==col_list[clr][0]:
                                w=(str(T[n][1]) + " [color=" + str(col_list[clr][1]) + "];\n")
                                s.write(w)
                                col.append(T[n][1])
                                col_list.append([T[n][1], col_list[clr][1]])
                
        if tipo_de_grafo == 10:
            print(T)
            for i in range(len(T)):
                r=T[i][0]
                r2=T[i][1]
                w=(str(r) + ' [label="'+ str(r) +'(' + str(r2) + ')"];\n')
                s.write(w)
            
        if tipo_de_grafo in range (7):
            print(self.aristas)
            for p in range(len(self.aristas)): # Escritura de cada arista para
                e1=str(self.aristas[p][0])     #   los generadores de grafos
                e2=str(self.aristas[p][1])
                flecha=" -> "
                puntocoma=';\n'
                w=e1+flecha+e2+puntocoma
                s.write(w)
                
        if tipo_de_grafo == 7:
            for p in range(len(self.aristas)):
                if self.aristas[p] in exp_aristas:
                    a=0
                    for l in range (len(T)):
                        if self.aristas[p][0] in T[l] and self.aristas[p][1] in T[l]:
                            a=1
                    if a==0:
                        e1=str(self.aristas[p][0])  # Para los árboles, se añade la etiqueta
                        e2=str(self.aristas[p][1])  #  que mantiene de color negro la arista
                        flecha=" -> "
                        puntocoma='[color="black"];\n'            
                        w=e1+flecha+e2+puntocoma
                        s.write(w)
            
        elif tipo_de_grafo >= 8:
            # print(self.aristas)
            # print(exp_aristas)
            for p in range(len(self.aristas)):
                if self.aristas[p] in exp_aristas:
                    e1=str(self.aristas[p][0])
                    e2=str(self.aristas[p][1])
                    flecha=" -> "
                    puntocoma='[color="black"];\n'            
                    w=e1+flecha+e2+puntocoma
                    # print(w)
                    s.write(w)
            
        for i in range(len(self.nodos)):    # Se escribe cada nodo que no se encuentra en una arista
            b=False
            while b==False:
                for j in range(len(self.aristas)):
                    if self.nodos[i] in self.aristas[j]:
                        b=True
                if b==False:
                    # print(self.nodos[i])
                    ns=str(self.nodos[i])
                    w2=str(ns + puntocoma)
                    s.write(w2)
                b=True 
        
        s.write("}")        # Se finaliza y cierra el archivo del grafo
        s.close()
    
    def color_R(self, T, c, b):         # Función para determinar la cantidad de 
        for r in range(len(T)):         #  colores necesaria para el árbol DFSR
            if len(T) > len(c):
                c.append(Color())
                b.append([])
            if type(T[r]) is list:
                b[r].append(T[r][0])
                self.color_R(T[r], c, b)
        return c, b
    
    def color_I(self, T, c, b):         # Función para determinar la cantidad de
        # print (T)                     #  colores necesaria para el árbol DFSI
        c_exp_ar=[]
        for r in range(len(T)):
            for rr in range(len(T)):
                if T[rr][0] == T[r][0] and T[rr] != T[r] and T[r][0] not in b and T[rr] not in c_exp_ar:
                    b.append(T[r][0])
                    c_exp_ar.append(T[rr])
        for r in range(len(b)):
            c.append(Color())
        return c, b
    
    def BFS(self, s,T,exp,exp_aristas):
        T.append([s])
        exp.append(s)                             # Generación del árbol BFS
        i=0                                       #  El nodo fuente (s) se asigna a la lista de la 
        w=1                                       #  capa 0, mientras que todos los nodos de las 
        while w==1:                               #  áristas en las que participe el nodo s, quedan
            T.append([])                          #  registrados en la capa 1. Análogamente los nodos 
            for j in range(len(T[i])):            #  que toquen la capa anterior, se registran en una nueva capa
                for k in range (len(self.aristas)):
                    if T[i][j] in self.aristas[k] and self.aristas[k][0] not in exp and self.aristas[k][0] not in T[i+1]:
                        T[i+1].append(self.aristas[k][0])
                        exp.append(self.aristas[k][0])
                        exp_aristas.append(self.aristas[k])
                    if T[i][j] in self.aristas[k] and self.aristas[k][1] not in exp and self.aristas[k][1] not in T[i+1]:
                        T[i+1].append(self.aristas[k][1])
                        exp.append(self.aristas[k][1])
                        exp_aristas.append(self.aristas[k])
            if T[i+1]==[]:
                w=0
            i+=1
        # print("Cantidad de capas: " + str(len(T)-1))
        return T
    
    def DFSR(self, s, T, exp, exp_aristas):                           # Generación del arbol DFS-Recursivo
        R=[s]                                                         #  El primer nodo que toque al nodo fuente 
        T.append(R)                                                   #  llamara nuevamente a esta misma función, 
        exp.append(s)                                                 #  pasando a convertirse en el nuevo nodo fuente.
        for a in range(len(self.aristas)):                            #  Así, se continua avanzando sobre una linea de
            if s in self.aristas[a] and self.aristas[a][0] not in exp:#  aristas, y cada vez que se termine una
                exp_aristas.append(self.aristas[a])                   #  trayectoria continua, la función terminará y 
                self.DFSR(self.aristas[a][0], R, exp, exp_aristas)    #  permitirá buscar trayectorias alternas al nodo 
            if s in self.aristas[a] and self.aristas[a][1] not in exp:#  en tuno.
                exp_aristas.append(self.aristas[a])
                self.DFSR(self.aristas[a][1], R, exp, exp_aristas)        
    
    def DFSI(self, s, T, exp, exp_aristas, stack):
        stack.append(s)    # Generación del árbol DFS-Iterativo:
        r=s                #  Iniciando desde el nodo fuente, se añadirá cada nodo explorado a una lista, de modo que al
        i=1                #  terminar una trayectoria, se irán eliminando los últimos elementos de dicha lista hasta
        while i==1:        #  encontrar una trayectoria alterna en alguno de los nodos. Las trayectorias ignorarán las
            # print(stack) #  aristas con nodos en la lista de pendientes.
            for a in range(len(self.aristas)):
                if r in self.aristas[a] and self.aristas[a] not in exp_aristas:
                    if (self.aristas[a][0] in stack and self.aristas[a][1] in stack)\
                        or (self.aristas[a][0] in exp) or (self.aristas[a][1] in exp):
                        True
                    else:
                        exp_aristas.append(self.aristas[a])
                        if self.aristas[a][1]==r and self.aristas[a][0] not in stack:
                            stack.append(self.aristas[a][0])
                        elif self.aristas[a][0]==r and self.aristas[a][1] not in stack:
                            stack.append(self.aristas[a][1])
                        a=0
                        r=stack[-1]
            exp.append(r)
            stack.remove(stack[-1])
            a=0            
            if len(stack)==0:
                i=0
            else:
                r=stack[-1]
        T.extend(exp_aristas)

    def Dijkstra(self, s,sum_values,exp,exp_aristas,values):
        print(self.aristas)
        for i in range (len(self.aristas)):
            values.append(random.randrange(1, 21))       
        print(values)
        minimum=[]
        minimum_aristas=[]
        vet_aristas=[]
        exp_values=[]
        exp.append(s)
        a=1
        while a==1:
            # print(exp)
            for n in exp:
                for i in range(len(self.aristas)):
                    if n in self.aristas[i]\
                    and self.aristas[i] not in minimum_aristas\
                    and self.aristas[i] not in exp_aristas\
                    and self.aristas[i] not in vet_aristas\
                    and self.aristas[i][1] != n:
                        minimum_aristas.append(self.aristas[i])
                        minimum.append(values[i])
            # print(minimum_aristas)
            # print(minimum)
            if len(minimum) > 0:
                min_value = min(minimum)
                v0=minimum_aristas[minimum.index(min_value)][0]
                # print(v0)
                v1=minimum_aristas[minimum.index(min_value)][1]
                # print(v1)
                if v0 not in exp or v1 not in exp:
                    exp_aristas.append(minimum_aristas[minimum.index(min_value)])
                    exp_values.append(min_value)
                else:
                    vet_aristas.append(minimum_aristas[minimum.index(min_value)])
                if v0 not in exp and v1 in exp:
                    exp.append(v0)
                elif v1 not in exp and v0 in exp:
                    exp.append(v1)
            else:
                a=0
            minimum.clear()
            minimum_aristas.clear()
        print(exp_aristas)
        print(exp_values)
        sum_values.append([s,0])
        def suma(ind,n0,vi):
            for n in reversed(exp_aristas[:ind]):
                if n[1] == n0:
                    vi += exp_values[exp_aristas.index(n)]
                    # exp_sum.append(n)
                    suma(ind-1,n[0],vi)
            return vi
        for i in reversed(exp_aristas):
            ind=len(exp_aristas)
            vi=exp_values[exp_aristas.index(i)]
            distancia = suma(ind,i[0],vi)
            sum_values.append([i[1], distancia])
        # print(sum_values)
    def KruskalD(self,exp,exp_aristas,values,valores):
        ksum=0
        # print(self.aristas)
        k_aristas=self.aristas.copy()
        # for i in range(len(k_aristas)):
        #     values.append(random.randrange(1, 21))
        values.extend(valores[0:len(k_aristas)])
        # print(values)
        delete=[]
        for i in range (len(values)):
            a=False
            b=False
            minimum=min(values)
            min_ndx=values.index(minimum)
            min_ar=k_aristas[min_ndx]
            e0=k_aristas[min_ndx][0]
            e1=k_aristas[min_ndx][1]
            for j in exp:
                if e0 in j or e1 in j:
                    a=True
            if a==False:
                exp_aristas.append(min_ar)
                exp.append([])
                exp[-1].append(e0)
                exp[-1].append(e1)
                ksum += minimum
            else:
                for k in exp:
                    if e0 in k and e1 in k:
                        b=True
                if b==False:
                    exp.append([])
                    for l in exp:
                        if (e0 in l and e1 not in l) or (e1 in l and e0 not in l):
                            if e0 in l:
                                l.append(e1)
                            elif e1 in l:
                                l.append(e0)
                            # nl.extend(l)
                            exp[-1].extend(l)
                            delete.append(l)
                            # exp.remove(exp[l])
                    # exp.append(nl.copy())
                    for m in delete:
                        exp.remove(m)
                    delete.clear()
                    exp_aristas.append(min_ar)
                    ksum += minimum
            values.remove(minimum)
            k_aristas.remove(min_ar)
            # print(exp)
            # print(exp_aristas)
            # print(ksum)
        # print(exp)
        print(exp_aristas,"\n")
        print("El valor del MST es: ", ksum,"\n")
    
    def KruskalI(self,exp,exp_aristas,values,valores):
        # print(self.aristas)
        T=[]
        exp_BFS=[]
        exp_ar_BFS=[]        
        ksum=0
        copy_aristas=self.aristas.copy()
        exp_aristas.extend(self.aristas)
        # v=[11, 12, 20, 17, 17, 12, 19, 5, 19, 13, 8, 11, 19, 12, 1, 2, 19, 15, 4, 10, 12, 13, 8, 15, 12, 5, 11, 5, 5, 2, 10, 8, 14, 5, 18, 14, 1, 14, 5, 7, 18, 3, 13, 20, 3, 20, 1, 2, 3, 7, 2, 8, 11, 14, 17, 4, 15]
        # for i in range (len(self.aristas)):
        #     values.append(random.randrange(1, 21))
        values.extend(valores[0:len(copy_aristas)])
        # values.extend(v)
        for j in values:
            ksum += j
        # print(ksum)
        for k in self.aristas:
            exp.extend(k)
        # print(exp)
        # print(values)
        for i in range(len(values)):
            conect=False
            maximum=max(values)
            max_ndx=values.index(maximum)
            max_ar=exp_aristas[max_ndx]
            # print("\n",max_ar,",",maximum)
            e0=exp_aristas[max_ndx][0]
            e1=exp_aristas[max_ndx][1]
            cuenta0=exp.count(e0)
            cuenta1=exp.count(e1)
            if cuenta0>1 or cuenta1>1:
                if cuenta0>1 and cuenta1>1:
                    exp.remove(e0)
                    exp.remove(e1)
                    self.aristas.remove(max_ar)
                    self.BFS(e0, T, exp_BFS, exp_ar_BFS)
                    # print(T,"\n")
                    for b in range(len(T)):
                        if e1 in T[b]:
                            conect=True
                    if conect==False:
                        self.aristas.append(max_ar)
                    else:
                        ksum -=maximum
                    T.clear()
                    exp_BFS.clear()
                    exp_ar_BFS.clear()
                else:
                    if cuenta0>1:
                        exp.remove(e0)
                    else:
                        exp.remove(e1)
            # print(exp)
            values.remove(maximum)
            exp_aristas.remove(max_ar)
            # print("\n",self.aristas)
        # print("\n",exp)
        print(self.aristas)
        print("\nEl valor del MST es: ", ksum,"\n")
        exp_aristas.extend(copy_aristas)
        
    def Prim(self,s,sum_values,exp,exp_aristas,values,valores):
        ksum=0
        # print(self.aristas)
        k_aristas=self.aristas.copy()
        # for i in range(len(k_aristas)):
        #     values.append(random.randrange(1, 21))
        values.extend(valores[0:len(k_aristas)])
        # print(values)
        vecinos=[]
        vecinos_val=[]
        exp.append(s)        
        for i in range(len(k_aristas)):
            if (k_aristas[i][0] in exp and k_aristas[i][1] not in exp)\
            or (k_aristas[i][1] in exp and k_aristas[i][0] not in exp):
                vecinos.append(k_aristas[i])
                vecinos_val.append(values[i])
                minimum=min(vecinos_val)
                min_ndx=vecinos_val.index(minimum)
                min_ar=vecinos[min_ndx]
                e0=vecinos[min_ndx][0]
                e1=vecinos[min_ndx][1]
                if e0 not in exp:
                    exp.append(e0)
                if e1 not in exp:
                    exp.append(e1)
                exp_aristas.append(min_ar)
                ksum +=minimum
                vecinos.clear()
                vecinos_val.clear()
        print(exp_aristas)
        print("\nEl valor del MST es: ", ksum,"\n")

"Grafo de Malla"
def malla(i, j, dirigido=False): # i columnas, j filas
    g=Grafo()
    T=[]
    exp_aristas=[]
    n=1
    m=[]
    for vi in range (i):
        r=[]
        for vj in range (j):
            r.append(n)
            g.agregarNodo(n)
            n+=1
        m.append(r)
    # print(m)
    
    for vi in range (i):
        for vj in range (j):            
            nij=m[vi][vj]            
            if vi<(i-1):
                g.agregarArista(nij, m[vi+1][vj])
            if vj<(j-1):
                g.agregarArista(nij, m[vi][vj+1])
    g.generar_archivo(1,T,exp_aristas)

"Grafo de Erdös y Rényi"
def eyR(n,a,dirigido=False): #n nodos, a aristas
    g=Grafo()
    r=[]
    aristas=[]
    T=[]
    exp_aristas=[]
    for i in range (n):
        g.agregarNodo(i+1)
        r.append(i+1)    
    
    for i in range (a+1):
        # print (r)
        n1=random.choice(r)        
        n2=random.choice(r)
        if [n1, n2] not in aristas and [n2, n1] not in aristas and n1!=n2:
            g.agregarArista(n1, n2)
            aristas.append([n1, n2])
        else:
            i=i-1
    # print(aristas)
    g.generar_archivo(2,T,exp_aristas)
    
"Grafo de Gilbert"
def gilbert(n, p, dirigido=False):
    g=Grafo()
    r=[]
    aristas=[]
    T=[]
    exp_aristas=[]
    for i in range (n):
        g.agregarNodo(i+1)
        r.append(i+1)    
    
    for i in r:
        for j in r:
            prob=random.random()
            if prob<=(p/200) and [i, j] not in aristas \
                             and [j, i] not in aristas and i!=j:
                g.agregarArista(i, j)
                aristas.append([i, j])
    # print(aristas)
    g.generar_archivo(3,T,exp_aristas)
    
"Grafo Geográfico Simple"
def simple(n, r, dirigido=False):
    g=Grafo()
    T=[]
    exp_aristas=[]
    nodos=[]
    coords=[]
    aristas=[]
    box=n*4
    for i in range (n):
        g.agregarNodo(i+1)
        nodos.append(i+1)
        x=random.randrange(-box,box)
        y=random.randrange(-box,box)
        coords.append([x, y])
    print(coords)
    for i in (nodos):
        for j in (nodos):            
            pd=math.sqrt((coords[j-1][0]-coords[i-1][0])**2+(coords[j-1][1]-coords[i-1][1])**2)
            if pd<=r and [i, j] not in aristas and [j, i] not in aristas and i!=j:
                g.agregarArista(i, j)
                aristas.append([i, j])
    # print(aristas)
    g.generar_archivo(4,T,exp_aristas)
    
"Grafo Barabási-Albert"
def byA(n, a, dirigido=False):
    g=Grafo()
    T=[]
    exp_aristas=[]
    nod_vert=[]
    nodos=[]
    aristas=[]
    phi=(1+math.sqrt(5))/2
    for i in range (n):
        g.agregarNodo(i+1)
        nodos.append(i+1)
        nod_vert.append(0)
        for j in range (len(nodos)):
            prob=random.random()
            if prob<=(1/(phi**(0.5*nod_vert[j]))) and nod_vert[j]<=a \
                                            and nod_vert[i]<=a \
                                            and [i, j] not in aristas \
                                            and [j, i] not in aristas and i!=j:
                g.agregarArista(i, j)
                aristas.append([i, j])
                nod_vert[j]+=1
                nod_vert[i]+=1
    # print(nod_vert)
    g.generar_archivo(5,T,exp_aristas)
    
"Grafo Dorogovtsev-Mendes"
def dyM(n, dirigido=False):
    g=Grafo()
    T=[]
    exp_aristas=[]
    nodos=[1, 2, 3]
    for i in range(len(nodos)):
        g.agregarNodo(i+1)
    aristas=[[1,2], [2,3], [1,3]]
    for i in range(len(aristas)):
        g.agregarArista(aristas[i][0], aristas[i][1])    
    for i in range(4, n+1):        
        g.agregarNodo(i)
        nodos.append(i)
        a=random.choice(aristas)
        if [a[0], i] not in aristas and [i ,a[0]] not in aristas and \
           [a[1], i] not in aristas and [i ,a[1]] not in aristas and \
           i!=a[0] and i!=a[1]:
            g.agregarArista(a[0], i)
            g.agregarArista(a[1], i)
            aristas.append([a[0], i])
            aristas.append([a[1], i])
    g.generar_archivo(6,T,exp_aristas)

"Grafos de búsqueda"
def search(tipo):
    s=open("grafo.gv","r")
    lectura=[]
    aristas=[]
    g=Grafo()
    rL=s.readlines()
    for i in range(1, len(rL)-1):
        if "->" in rL[i]:
            lectura.append(rL[i][0:-2])        
            aristas.append(lectura[i-1].split(" -> "))
            e1=int(aristas[i-1][0])
            e2=int(aristas[i-1][1])
            aristas[i-1][0]=e1
            aristas[i-1][1]=e2
            g.agregarNodo(e1)
            g.agregarNodo(e2)
            g.agregarArista(e1, e2)
        else:
            lectura.append(rL[i][0:-2])
            aristas.append(lectura[i-1])
            e1=int(aristas[i-1])
            g.agregarNodo(e1)
    g.nodos.sort()
    bco=["BFS", "DFSR", "DFSI", "Dijkstra", "Prim"]
    if tipo in bco:
        s=int(input("-Elegir nodo fuente-\nNodos disponibles: "+str(g.nodos[0])+"-"+str(g.nodos[-1])+"\n--> "))
    T=[]
    exp=[]
    exp_aristas=[]
    stack=[]
    values=[]
    sum_values=[]
    valores=[21, 9, 7, 11, 20, 8, 2, 15, 8, 20, 5, 12, 14, 2, 17, 12, 15, 8, 17, 18, 1, 5, 11, 14, 16, 5, 21, 6, 12, 5, 1, 12, 18, 3, 9, 9, 14, 5, 16, 3, 7, 8, 16, 15, 3, 12, 8, 12, 14, 15, 20, 9, 9, 9, 11, 21, 4, 12, 17, 14, 9, 20, 6, 19, 19, 18, 8, 13, 18, 20, 15, 16, 6, 3, 8, 4, 20, 19, 18, 18, 4, 7, 21, 4, 1, 5, 16, 19, 5, 7, 5, 10, 3, 5, 7, 17, 9, 5, 20, 2, 14, 8, 2, 9, 11, 12, 2, 4, 18, 18, 7, 19, 20, 15, 10, 9, 1, 6, 2, 1, 18, 14, 20, 5, 3, 12, 13, 14, 1, 9, 5, 7, 1, 7, 18, 5, 13, 10, 6, 5, 21, 11, 17, 15, 9, 7, 11, 5, 4, 6, 15, 3, 11, 21, 8, 8, 21, 4, 9, 12, 17, 9, 14, 8, 4, 6, 20, 2, 12, 8, 18, 19, 5, 19, 4, 20, 17, 2, 1, 9, 8, 1, 21, 5, 8, 17, 2, 14, 20, 4, 13, 12, 12, 13, 14, 12, 5, 10, 10, 17, 3, 17, 8, 4, 3, 7, 2, 7, 14, 7, 19, 17, 7, 13, 8, 3, 18, 20, 6, 5, 5, 7, 16, 13, 20, 9, 14, 17, 7, 9, 15, 7, 17, 14, 6, 9, 7, 1, 9, 10, 8, 16, 20, 11, 5, 19, 17, 14, 1, 2, 12, 11, 15, 8, 20, 13, 17, 12, 8, 6, 3, 19, 11, 8, 1, 2, 13, 3, 12, 7, 3, 11, 20, 2, 2, 8, 16, 13, 9, 12, 7, 13, 2, 19, 8, 4, 4, 10, 19, 11, 4, 9, 3, 13, 17, 13, 4, 2, 12, 20, 21, 6, 12, 6, 2, 20, 9, 2, 5, 19, 3, 7, 7, 3, 9, 12, 12, 21, 16, 4, 5, 10, 16, 15, 17, 11, 12, 11, 19, 21, 7, 17, 21, 10, 21, 16, 1, 13, 14, 20, 15, 19, 14, 12, 5, 1, 5, 18, 14, 17, 9, 3, 2, 14, 3, 3, 6, 12, 13, 1, 16, 3, 13, 11, 7, 14, 21, 21, 12, 17, 10, 6, 4, 17, 14, 8, 10, 14, 15, 8, 15, 6, 4, 4, 20, 17, 21, 10, 7, 18, 20, 14, 7, 12, 20, 7, 14, 4, 3, 10, 8, 9, 19, 9, 18, 18, 10, 10, 13, 17, 7, 12, 6, 17, 4, 1, 17, 18, 17, 6, 5, 5, 5, 10, 3, 1, 15, 3, 7, 16, 9, 5, 19, 20, 13, 21, 4, 18, 4, 20, 1, 1, 1, 14, 13, 2, 8, 5, 13, 8, 6, 14, 15, 1, 17, 9, 21, 21, 15, 13, 11, 14, 9, 13, 15, 14, 17, 8, 2, 9, 4, 21, 11, 6, 13, 12, 15, 16, 18, 9, 20, 6, 7, 14, 20, 11, 20, 3, 10, 19, 8, 17, 14, 15, 14, 11, 17, 1, 7, 1, 8, 10, 2, 4, 5, 15, 6, 16, 18, 10, 8, 21, 3, 9, 3, 10, 2, 1, 17, 11, 13, 14, 17, 8, 13, 12, 1, 8, 13, 16, 19, 13, 5, 2, 14, 15, 4, 19, 8, 19, 21, 15, 21, 16, 21, 1, 3, 3, 6, 2, 17, 8, 19, 16, 15, 12, 14, 12, 10, 20, 21, 17, 6, 14, 14, 18, 17, 14, 7, 10, 1, 19, 6, 19, 10, 20, 20, 2, 3, 11, 16, 5, 13, 2, 13, 11, 21, 18, 9, 17, 15, 11, 15, 1, 18, 5, 11, 16, 12, 9, 18, 3, 21, 20, 12, 11, 2, 12, 9, 17, 4, 13, 18, 3, 21, 5, 15, 21, 14, 18, 1, 2, 13, 11, 11, 2, 3, 14, 11, 15, 20, 17, 1, 9, 5, 2, 16, 5, 5, 21, 1, 17, 1, 17, 12, 20, 13, 3, 3, 1, 19, 15, 10, 15, 1, 8, 11, 21, 13, 11, 2, 3, 18, 1, 3, 8, 10, 13, 16, 11, 19, 19, 15, 16, 14, 16, 8, 16, 10, 16, 18, 15, 11, 17, 18, 8, 21, 17, 15, 3, 7, 2, 17, 8, 2, 1, 6, 17, 8, 3, 18, 16, 1, 2, 20, 19, 16, 7, 4, 17, 16, 17, 5, 16, 21, 15, 15, 15, 10, 20, 13, 17, 1, 2, 11, 17, 12, 12, 21, 19, 12, 21, 16, 21, 13, 12, 3, 5, 2, 16, 3, 18, 6, 11, 14, 2, 9, 3, 17, 20, 17, 4, 5, 11, 2, 10, 9, 11, 20, 14, 6, 6, 19, 9, 10, 18, 6, 10, 15, 6, 12, 15, 17, 15, 17, 3, 11, 14, 20, 5, 15, 15, 21, 1, 12, 14, 6, 3, 19, 12, 17, 11, 20, 10, 12, 18, 13, 8, 17, 8, 6, 8, 18, 1, 7, 17, 1, 8, 12, 8, 16, 14, 15, 4, 17, 20, 18, 9, 13, 12, 14, 6, 9, 3, 19, 11, 10, 5, 7, 14, 12, 8, 13, 3, 12, 7, 21, 7, 19, 4, 11, 19, 21, 3, 3, 3, 21, 1, 20, 15, 14, 6, 9, 15, 8, 1, 7, 5, 13, 20, 4, 11, 14, 17, 9, 21, 19, 19, 10, 9, 8, 12, 11, 4, 1, 12, 8, 17, 21, 17, 3, 11, 5, 20, 21, 19, 9, 17, 7, 3, 9, 20, 21, 21, 10, 18, 10, 10, 10, 5, 6, 14, 6, 3, 21, 3, 20, 18, 3, 19, 9, 4, 7, 14, 10, 15, 21, 9, 6, 19, 3, 17, 2, 13, 2, 21, 20, 18, 17, 13, 19, 21, 18, 20, 13, 10, 12, 18, 14, 7, 5, 18, 11, 20, 18, 17, 15, 1, 12, 7, 2, 8, 1, 20, 15, 19, 18, 1, 15, 14, 15, 15, 6, 7, 8, 16, 8, 18, 9, 7, 12, 6, 4, 1, 15, 19, 9, 5, 6, 1, 5, 3, 7, 4, 20, 13, 12, 16, 16, 13, 4, 12, 9, 21, 8, 12, 1, 4, 18, 20, 10, 13, 2, 10, 12, 1, 18, 13, 21, 1, 11, 20, 13, 11, 21, 5, 11, 18, 21, 10, 11, 9, 14, 7, 7, 15, 5, 17, 19, 5, 9, 5, 13, 3, 4, 17, 12, 16, 7, 20, 20, 7, 8, 11, 9, 18, 20, 8, 20, 7, 4, 2, 20, 16, 14, 2, 18, 3, 9, 20, 8, 5, 14, 4, 15, 10, 19, 15, 10, 12, 6, 15, 9, 3, 15, 21, 7, 10, 19, 4, 2, 19, 10, 20, 4, 21, 20, 12, 2, 15, 7, 18, 4, 21, 17, 19, 20, 17, 17, 15, 2, 20, 9, 6, 10, 4, 15, 1, 15, 1, 9, 6, 11, 18, 17, 20, 3, 10, 11, 13, 8, 8, 20, 1, 11, 18, 1, 6, 4, 4, 6, 18, 9, 11, 2, 17, 16, 6, 16, 7, 3, 17, 14, 5, 14, 19, 7, 10, 11, 13, 15, 14, 9, 5, 18, 14, 21, 12, 14, 1, 15, 6, 9, 16, 19, 20, 8, 14, 20, 20, 8, 14, 18, 13, 4, 3, 6, 15, 4, 4, 4, 6, 20, 3, 7, 14, 16, 2, 17, 3, 4, 1, 9, 19, 2, 15, 2, 9, 14, 4, 7, 19, 15, 9, 14, 7, 4, 12, 15, 15, 7, 1, 17, 14, 18, 3, 12, 18, 5, 6, 21, 21, 9, 8, 6, 3, 4, 3, 2, 3, 7, 3, 5, 19, 15, 8, 1, 10, 5, 21, 6, 6, 8, 8, 15, 1, 11, 11, 11, 11, 19, 6, 8, 9, 5, 7, 5, 12, 17, 1, 16, 13, 20, 1, 10, 2, 2, 1, 21, 5, 8, 19, 1, 7, 13, 2, 18, 7, 13, 9, 8, 20, 7, 4, 10, 1, 6, 2, 13, 1, 1, 19, 1, 21, 12, 4, 9, 16, 6, 6, 1, 10, 11, 9, 16, 5, 12, 14, 16, 12, 11, 11, 16, 2, 3, 3, 2, 13, 6, 15, 15, 16, 12, 15, 13, 20, 13, 17, 14, 5, 8, 3, 11, 21, 18, 2, 13, 15, 2, 12, 1, 20, 14, 1, 19, 20, 11, 8, 7, 3, 10, 16, 5, 6, 8, 3, 13, 6, 8, 12, 14, 6, 3, 3, 3, 2, 13, 5, 3, 14, 8, 2, 18, 11, 15, 17, 8, 8, 7, 12, 14, 9, 21, 15, 20, 4, 2, 1, 16, 6, 2, 7, 15, 8, 5, 21, 15, 1, 18, 19, 3, 11, 15, 15, 3, 10, 12, 7, 6, 17, 2, 13, 11, 17, 9, 12, 21, 5, 1, 16, 11, 14, 2, 18, 6, 1, 20, 21, 19, 17, 9, 17, 15, 21, 9, 5, 6, 11, 9, 10, 20, 20, 1, 12, 7, 2, 8, 16, 4, 21, 12, 18, 7, 9, 7, 3, 7, 21, 4, 9, 10, 9, 12, 8, 21, 1, 15, 6, 3, 2, 7, 19, 19, 7, 12, 19, 16, 8, 9, 12, 1, 19, 7, 21, 4, 21, 1, 16, 21, 12, 19, 21, 1, 2, 9, 2, 12, 19, 4, 13, 16, 6, 3, 13, 11, 6, 21, 9, 17, 4, 5, 13, 7, 1, 13, 15, 19, 1, 21, 4, 18, 19, 21, 17, 15, 4, 13, 2, 19, 6, 18, 16, 18, 1, 13, 13, 7, 13, 13, 9, 18, 20, 13, 7, 17, 7, 10, 21, 6, 15, 20, 18, 3, 1, 18, 9, 17, 6, 8, 8, 5, 7, 18, 15, 1, 16, 9, 2, 14, 13, 6, 15, 18, 2, 9, 1, 20, 19, 8, 6, 4, 6, 13, 20, 14, 2, 12, 12, 1, 3, 21, 6, 7, 19, 20, 15, 20, 10, 21, 14, 17, 11, 21, 9, 2, 11, 21, 16, 8, 6, 18, 8, 3, 18, 12, 12, 5, 16, 7, 21, 21, 11, 1, 17, 21, 17, 21, 1, 6, 4, 3, 16, 17, 11, 1, 5, 8, 16, 10, 1, 2, 2, 9, 5, 8, 21, 10, 13, 1, 20, 4, 15, 1, 3, 5, 18, 10, 18, 16, 14, 7, 15, 6, 13, 14, 5, 12, 12, 10, 19, 9, 9, 4, 7, 8, 7, 13, 11, 19, 2, 9, 20, 8, 3, 3, 18, 17, 7, 5, 7, 20, 6, 8, 11, 1, 18, 3, 11, 19, 20, 12, 9, 11, 4, 16, 7, 8, 14, 7, 4, 7, 10, 13, 15, 19, 4, 9, 14, 14, 8, 8, 12, 1, 17, 10, 14, 8, 9, 1, 2, 16, 17, 5, 15, 5, 5, 4, 20, 20, 2, 17, 2, 4, 15, 14, 10, 14, 3, 1, 17, 11, 18, 5, 19, 8, 18, 14, 4, 20, 17, 6, 3, 21, 3, 9, 12, 17, 9, 13, 15, 14, 5, 17, 20, 18, 12, 2, 4, 12, 17, 14, 2, 8, 11, 14, 10, 14, 13, 19, 18, 20, 3, 21, 8, 15, 3, 8, 15, 20, 3, 19, 4, 8, 16, 4, 4, 13, 19, 13, 20, 20, 4, 6, 20, 7, 7, 17, 6, 16, 9, 17, 18, 20, 1, 7, 17, 12, 13, 7, 6, 3, 4, 9, 4, 3, 7, 13, 20, 9, 17, 3, 21, 3, 7, 10, 9, 15, 7, 15, 10, 5, 4, 1, 2, 5, 14, 3, 16, 5, 14, 15, 6, 16, 12, 1, 21, 11, 9, 15, 8, 18, 4, 5, 2, 15, 18, 21, 1, 4, 15, 4, 21, 5, 4, 20, 1, 6, 6, 20, 7, 2, 5, 10, 17, 20, 12, 5, 19, 18, 8, 10, 17, 18, 4, 15, 17, 7, 10, 13, 12, 4, 11, 13, 8, 15, 16, 6, 9, 16, 12, 15, 5, 4, 13, 7, 8, 6, 7, 5, 4, 1, 4, 14, 13, 1, 12, 10, 21, 7, 11, 15, 6, 7, 4, 14, 2, 4, 18, 15, 6, 19, 16, 16, 12, 9, 7, 12, 14, 16, 1, 1, 3, 16, 9, 8, 20, 4, 9, 12, 3, 15, 18, 14, 18, 15, 2, 1, 4, 4, 1, 21, 21, 9, 14, 3, 13, 7, 16, 15, 16, 7, 11, 16, 7, 5, 4, 1, 15, 11, 19, 16, 15, 18, 10, 12, 15, 16, 6, 12, 2, 16, 4, 4, 18, 8, 2, 21, 4, 9, 10, 12, 19, 4, 9, 3, 15, 5, 8, 10, 19, 7, 6, 14, 8, 7, 7, 13, 12, 9, 19, 2, 14, 11, 15, 11, 17, 14, 5, 18, 20, 11, 21, 1, 11, 1, 4, 1, 18, 12, 20, 17, 17, 20, 19, 2, 4, 6, 6, 1, 11, 16, 3, 11, 18, 11, 5, 20, 21, 6, 1, 17, 20, 21, 2, 7, 17, 12, 3, 2, 18, 18]
    if tipo=="BFS":
        g.BFS(s,T,exp,exp_aristas)
        tipo_de_grafo=7
    elif tipo=="DFSR":
        g.DFSR(s,T,exp,exp_aristas)
        tipo_de_grafo=8
    elif tipo=="DFSI":
        g.DFSI(s,T,exp,exp_aristas,stack)
        tipo_de_grafo=9
    elif tipo=="Dijkstra":
        g.Dijkstra(s,sum_values,exp,exp_aristas,values)
        tipo_de_grafo=10
    elif tipo=="KruskalD":
        g.KruskalD(exp,exp_aristas,values,valores)
        tipo_de_grafo=11
    elif tipo=="KruskalI":
        g.KruskalI(exp,exp_aristas,values,valores)
        tipo_de_grafo=12
    elif tipo=="Prim":
        g.Prim(s,sum_values,exp,exp_aristas,values,valores)
        tipo_de_grafo=13
    # print(T)
    # print(exp_aristas)
    if tipo=="Dijkstra":
        g.generar_archivo(tipo_de_grafo, sum_values, exp_aristas)
    else:
        g.generar_archivo(tipo_de_grafo, T, exp_aristas)
    

# malla(5,6) # (5,6):30, (10,10):100, (20,25):500  columnas, filas
# eyR(30,29) # nodos, aristas
# gilbert(127,15) # nodos, porcentaje de probabilidad
# simple(500,309) # nodos, radio
# byA(30,5) #nodos, aristas máximas por nodo
# dyM(500) #nodos
BFS="BFS"    # Selección del tipo de árbol de búsqueda
DFSR="DFSR"
DFSI="DFSI"

Dijkstra="Dijkstra"

KruskalD="KruskalD"
KruskalI="KruskalI"
Prim="Prim"

# search(KruskalD)
# search(KruskalI)
search(Prim)