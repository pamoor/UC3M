

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
    
    li a1 1
    jal ra simplificador # Llamamos al simplificador (parametro ya en fa0)
    
    li s0 0 # Contador de iteraciones del sumatorio en s0
    li s1 7 # Limite del sumatorio en s1
    fcvt.s.w fs6 s0 # Cargamos un 0 (float) en fs6 (donde se iria haciendo el sumatorio)
    
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
            
cos:
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
    
    li a1 0
	jal ra simplificador# Llamamos al simplificador (parametro ya en fa0)
    
    li s0 0 # Contador de iteraciones del sumatorio en s0
    li s1 7 # Limite del sumatorio en s1
    fcvt.s.w fs6 s0 # Cargamos un 0 (float) en fs6 (donde se ira haciendo el sumatorio)
    
    fmv.s fs2 fa0 # Guardamos el numero del que buscamos el coseno (x) en fs2 
    
    
    sumatorio_coseno: bge s0 s1 fin_coseno 
    	
        li t0 2
        mul s3 s0 t0  # exponente en s3 (2*n)
        
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
        rem t3 s0 t1	# Vemos si el nuumero de iteracion es par o impar (para ver el signo del numerador -> 1^n)
        beq t3 zero coseno_positivo 
        
        fneg.s fs5 fs5	# Cambiamos signo si es impar
        
        coseno_positivo: 	# Numerador (con signo) en fs5
        
        fcvt.s.w fs4 s4 # Pasamos a float el denominador para poder dividir al numerador
        
        fdiv.s ft0 fs5 fs4 # Dividimos
        fadd.s fs6 fs6 ft0 # Sumamos en fs6 (resultado)
        addi s0 s0 1 # Anadimos 1 al contador de iteraciones
        
        j sumatorio_coseno
        
   fin_coseno: 
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
            
tg:
	addi sp, sp, -28
    fsw fs0, 24(sp)
    fsw fs1, 20(sp)
    fsw fs2, 16(sp)
    fsw fs3, 12(sp)
    fsw fs4, 8(sp)
    fsw fs5, 4(sp)
    sw ra, 0(sp)
	
# 	def tg(x: float):
	fmv.s fs0 fa0 #fs0 valor inicial
    li t0 0x7F800000 #Valor infinito en hexadecimal, simple precisiÃÂÃÂÃÂÃÂ³n
	fmv.w.x fs4 t0 # Infinito en fs4
    li t1 0x38D1B717 #Valor mas pequeÃÂÃÂÃÂÃÂ±o para el cos
    fmv.w.x fs5 t1 # 0.0001 en fs5
  
    
    
#     seno = sin(x)
#     coseno = cos(x)
	jal ra sin
    
    fmv.s fs1 fa0 #fs1 valor sin
    
    fmv.s fa0 fs0 # vuelvo a cargar el valor inicial en fa0 para pasar el parametro al cos
    
    jal ra cos
    
    fmv.s fs2 fa0 #fs2 valor cos
    fabs.s ft0 fs2 #|Cos|
    
  #Comprobar que el coseno no es cero,  en ese caso devolver infinito 
  	fle.s t2, fs5, ft0 # t2 bool 0.0001 <= |cos| 
	li t3 1
	beq t2 t3 no_infinito # condicion del bool
    
    fmv.s fa0 fs4 # Movemos a fa0 el infinito
    j fin_tg # Saltamos al final de la subrutina

no_infinito:

	fdiv.s fs3 fs1 fs2 #     resultado = seno / coseno
    
    fmv.s fa0 fs3 # Resultado en fa0
    
fin_tg:    
    
    lw ra, 0(sp)
    flw fs5, 4(sp)
    flw fs4, 8(sp)
    flw fs3, 12(sp)
    flw fs2, 16(sp)
    flw fs1, 20(sp)
    flw fs0, 24(sp)
    addi sp, sp, 28
    
#     return resultado
	jr ra
            
E:	addi sp, sp, -24
	sw s0, 20(sp)
	sw s1, 16(sp)
    sw s2, 12(sp)
    fsw fs0, 8(sp)
    fsw fs1, 4(sp)
    sw ra, 0(sp)
	
# resultado = float(0)
# resultado en fs0
#    i = 0
	li s0 0
    li s1 7 # Guardamos el numero de iteraciones
  	# Para comparar en el bucle
#     while i < 7:
bucle_E_1:	bge s0 s1 fin_E
        	mv a0 s0 # muevo como parametro i par hacer el factorial
#         	denominador = factorial(i)
			jal ra factorial
            mv s2 a0 # resultado del factorial a fs1 (fs1 = denominador)
            fcvt.s.w fs1 s2 #lo transformo a float
#         	resultadotemp = 1 / denominador
			li t0 1
            fcvt.s.w ft0 t0
			
            fdiv.s ft1 ft0 fs1 #resultadotemp = 1 / denominador
        
#           resultado += resultadotemp
			fadd.s fs0 fs0 ft1
#        	i += 1
			addi s0 s0 1
            
            beq s0 s0 bucle_E_1 #vuelvo arriba del bucle
			
      
#     return resultado
fin_E:	fmv.s fa0 fs0 # muevo el resultado a fa0 por convenio
		lw ra, 0(sp) # desapilo los registros usados en la funcion
        flw fs1, 4(sp)
        flw fs0, 8(sp)
		lw s2, 12(sp)
		lw s1, 16(sp)
        lw s0, 20(sp)
		addi sp, sp, 24

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
    
    
    bucle_exp: bge t1 a1 fin_exp # Bucle se repite hasta el numero del exponente
    
    	fmul.s ft0 ft0 fa0 # Multiplicamos el resultado actual por el parametro
        addi t1 t1 1
        beq t1 t1 bucle_exp
    
    fin_exp: 
    		fmv.s fa0 ft0 # Devolvemos
            jr ra
            
simplificador:
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
    
    signo: rem t0 t3 t2 # Comprobacion de si el numero de iteraciones ha sido impar ("medias vueltas") 
    beq t0 zero fin_simplificacion # Si es asi, cambiamos el signo
    beq a1 zero signo_cos # TambiÃ©n comprobamos que no estamos operando con un coseno, puesto que su respuesta a las "medias vueltas es distinta"
    
    fneg.s fs2 fs2 # Para el caso del seno, simplemente cambiamos el signo
    j fin_simplificacion
    
    signo_cos: flt.s t1 fs2 ft3 # Para el caso del coseno, vemos si el valor actual es positivo, al que sumariamos pi/2, o negativo, al que restariamos pi/2
    beq t1 zero signo_cos_positivo
    fadd.s fs2 fs0 fs2 #Caso negativo
    j fin_simplificacion
    
    signo_cos_positivo:
    fsub.s fs2 fs0 fs2 #Caso positivo
    
   	fin_simplificacion: 
    fmv.s fa0 fs2 # Devolvemos en fa0
    
    lw ra, 0(sp)
    flw fs2, 4(sp)
  	flw fs1, 8(sp)
    flw,fs0 12(sp)
    addi sp, sp, 16
    
    
    jr ra
    	
        
    
    
    
    