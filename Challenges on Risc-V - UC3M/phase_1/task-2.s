
#
# Creator (https://creatorsim.github.io/creator/)
#


SinMatrix:
addi sp, sp, -28
	sw s0, 24(sp)
    sw s1, 20(sp)
    sw s2, 16(sp)
    sw s3, 12(sp)
    sw s4, 8(sp)
    sw s5, 4(sp)
    sw ra, 0(sp)

# def SinMatrix(MatrixA:a0, MatrixB:a1, N:a2, a2M:a3):
#Muevo los argumentos a registros para la funcion
	mv s0 a0 # Matrix A
    mv s1 a1 # MatrixB
    mv s2 a2 # N filas
    mv s3 a3 # M Columnas
	li s4 0  # i = 0
    li s5 0  # j = 0

#     while i < N:
#         j = 0
#         while j < M:
#             B[i][j] = sin(A[i][j])
#             j += 1
#         i += 1

       
bucle_m1:  beq  s4, s2, fin_bm1 #     while i < N:
						  #         j = 0
						  #         while j < M:
bucle_m2: beq  s5, s3, fin_bm2
#   B[i][j] = sin(A[i][j])

        flw  fa0, 0(s0)  # Cargo el valor de matrixA en fa0 parametro de la funcion sin
        
        jal ra sin
        
        fsw  fa0, 0(s1)  #Meto el valor de la matrixA ya calculado en la misma direcciÃÂÃÂ³n de A en B
        
        addi s0, s0, 4    # AÃÂÃÂ±ado 4 columnas para la siguiente direcciÃÂÃÂ³n
        addi s1, s1, 4	  # AÃÂÃÂ±ado 4 columnas para la siguiente direccion
        
        addi s5, s5, 1    #j += 1
        beq  s5, s5, bucle_m2

fin_bm2:addi s4, s4, 1 #i += 1
        add  s5, zero, zero # Pongo a 0 la j
        beq  s4, s4, bucle_m1
fin_bm1:
			lw ra, 0(sp)
            lw s5, 4(sp)
            lw s4, 8(sp)
            lw s3, 12(sp)
            lw s2, 16(sp)
            lw s1, 20(sp)
            lw s0, 24(sp)
            addi sp, sp, 28
        # return
        jr ra
        
        
sin:
	addi sp, sp, -36
	sw s0, 32(sp)
    sw s1, 28(sp)
    fsw fs2, 24(sp)
    sw s3, 20(sp)
    sw s4, 16(sp)
    fsw fs4, 12(sp)
    fsw fs5, 8(sp)
    fsw fs6, 4(sp)
    sw ra, 0(sp)
    
    jal ra simplificador   # Llamamos al simplificador (parametro ya en fa0), en este caso no especificamos que operamos con el seno, puesto que no hay coseno
    
    li s0 0 # Contador de iteraciones del sumatorio en s0
    li s1 7 # Limite del sumatorio en s1
    fcvt.s.w fs6 s0 # Cargamos un 0 (float) en fs6 (donde se ira haciendo el sumatorio)
    
    fmv.s fs2 fa0 # Guardamos el numero del que buscamos el seno (x) en fs2 
    
    
    sumatorio_seno: bge s0 s1 fin_seno 
    	
        li t0 2
        mul s3 s0 t0 
        addi s3 s3 1 # exponente en s3 (2*n + 1)
        
        mv a0 s3 # Exponente en a0 (parametro) para hacer su factorial ( Denominador = Exponente! )
        jal ra factorial 
        				 # Denominador en a0
        mv s4 a0		 # Denominador en s4
        fmv.s fa0 fs2    # x en fa0 (parametro)
        mv a1 s3		 # exponente en a1 (parametro)
        jal ra exponente
        				# numerador (sin signo) en fa0
        fmv.s fs5 fa0	# numerador (sin signo) en fs5
        
        li t1 2			
        rem t3 s0 t1	# Vemos si el numero de iteracion es par o impar (para ver el signo del numerador -> 1^n)
        beq t3 zero seno_positivo 
        
        fneg.s fs5 fs5	# Cambiamos signo si es impar
        
        seno_positivo: 	# Numerador (con signo) en fs5
        
        fcvt.s.w fs4 s4 # Pasamos a float el denominador para poder dividir al numerador
        
        fdiv.s ft0 fs5 fs4 # Dividimos
        fadd.s fs6 fs6 ft0 # Sumamos en fs6 (resultado)
        addi s0 s0 1 # Anadimos 1 al contador de iteraciones
        
        j sumatorio_seno
        
  fin_seno: 
  			fmv.s fa0 fs6 # Movemos a fa0 el resultado
            
            lw ra, 0(sp)
            flw fs6, 4(sp)
            flw fs5, 8(sp)
            flw fs4, 12(sp)
            lw s4, 16(sp)
            lw s3, 20(sp)
            flw fs2, 24(sp)
            lw s1, 28(sp)
            lw,s0 32(sp)
            addi sp, sp, 36
			
            jr ra

factorial:
# 	def factorial(x:int) -> int:
#     result = 1 ( result = t0)
		  li t0 1	
#     i = 1 (i = t1)
		  li t1 1	
#     while i <= x:
  b_1_fact: bgt t1 a0 fin_fact   
  #         result = result * i
            mul t0 t0 t1
  #         i += 1
            addi t1 t1 1
            beq t1 t1 b_1_fact # vuelvo arriba del bucle
   
  #     return result
  fin_fact: mv a0 t0 # paso resultado a0
  			jr ra # fin de factorial
    	    
              
exponente:
	
    # a0 base (float)
    # a1 exponente (entero)
    
	li t0 1
	fcvt.s.w ft0 t0 # Escribo un 1.0 en float
    li t1 0
    
    
    bucle_exp: bge t1 a1 fin_exp
    
    	fmul.s ft0 ft0 fa0
        addi t1 t1 1
        beq t1 t1 bucle_exp
    
    fin_exp: 
    		fmv.s fa0 ft0 
            jr ra
            
simplificador:
	
    # En este caso, no contemplamos que haya que simplificar un coseno, asi que no recibimos el parametro con el tipo de operacion
		
	addi sp, sp, -16
	fsw fs0, 12(sp)
    fsw fs1, 8(sp)
    fsw fs2, 4(sp)
    sw ra, 0(sp)
	
    li t0 0x40490FDB # Pi en hexadecimal
    fmv.w.x fs0 t0 # pi en coma flotante en fs0
    li t2 2
    li t3 0
    fcvt.s.w ft0 t0 # Convertimos a floats para operar
    fcvt.s.w ft1 t1
    fcvt.s.w ft2 t2
    fcvt.s.w ft3 t3 # 0 en ft3 (float)
    fdiv.s fs1 fs0 ft2 # Pi/2 en fs1
    
    fmv.s fs2 fa0 # Numero a simplificar en fs2
    fabs.s ft0 fs2 # Valor absoluto de fs2 en ft0
    flt.s t0 ft0 fs1 # Comparamos |fs2| con Pi/2 y guardamos bool en t0
    
    flt.s t1 fs2 ft3 # Vemos si el numero dato es negativo (fs2 < 0) y booleano en t1
    beq t1 zero bucle_simp_pos # Si t1 == 0 saltamos al bucle de los positivos
    
    bucle_simp_neg: bne t0 zero signo # Si |fs2| > Pi/2
    	fadd.s fs2 fs2 fs0 # Sumamos Pi a fs2
        fabs.s ft0 fs2 # Repetimos proceso
        flt.s t0 ft0 fs1
        addi t3 t3 1 # Contador de iteraciones
        beq t3 t3 bucle_simp_neg # Bucle
    
    bucle_simp_pos: bne t0 zero signo # Si |fs2| > Pi/2
    	fsub.s fs2 fs2 fs0 # Restamos Pi a fs2
        fabs.s ft0 fs2 # Repetimos proceso
        flt.s t0 ft0 fs1
        addi t3 t3 1 # Contador de iteraciones
        beq t3 t3 bucle_simp_pos # Bucle
    
    signo: rem t0 t3 t2 # Comprobacion de si el nomero de iteraciones ha sido impar ("medias vueltas")
    beq t0 zero fin_simplificacion # Si es asi, cambiamos el signo
    fneg.s fs2 fs2
    
    
   	fin_simplificacion: 
    fmv.s fa0 fs2 # Devolvemos en fa0
    
    lw ra, 0(sp)
    flw fs2, 4(sp)
  	flw fs1, 8(sp)
    flw,fs0 12(sp)
    addi sp, sp, 16
    
    
    jr ra

