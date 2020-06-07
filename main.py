print('Suspeitos de um crime.\n')
sim = []
nao = []
pt = []
 
while len(pt) < 5:
 
   p1 = int(input('O suspeito telefonou pra vítima?\n' + '1.Sim\n' + '2.Não\n'))
   pt.append(1)
 
   if p1 == 1:
       sim.append(p1)
       print('SIM\n')
   elif p1 == 2:
       nao.append(p1)
       print('NÃO\n')
 
   p2 = int(input('O suspeito esteve no local do crime?\n' + '1.Sim\n' + '2.Não\n'))
   pt.append(1)
 
   if p2 == 1:
       sim.append(p2)
       print('SIM\n')
   elif p2 == 2:
       nao.append(p2)
       print('NÃO\n')
 
   p3 = int(input('Mora perto da vítima?\n' + '1.Sim\n' + '2.Não\n'))
   pt.append(1)
 
   if p3 == 1:
       sim.append(p3)
       print('SIM\n')
   elif p3 == 2:
       nao.append(p3)
       print('NÃO\n')
 
   p4 = int(input('Devia pra vítima?\n' + '1.Sim\n' + '2.Não\n'))
   pt.append(1)
 
   if p4 == 1:
       sim.append(p4)
       print('SIM\n')
   elif p4 == 2:
       nao.append(p4)
       print('NÃO\n')
 
   p5 = int(input('Já trabalhou com a vítima?\n' + '1.Sim\n' + '2.Não\n'))
   pt.append(1)
 
   if p5 == 1:
       sim.append(p5)
       print('SIM\n')
   elif p5 == 2:
       nao.append(p5)
       print('NÃO\n')
 
if len(pt) == 5:
  
   if len(sim) > 1 and len(sim) <=2:
       print('\n Suspeito.')
   elif len(sim) >= 3 and len(sim) <= 4:
       print('\n Cúmplice.')
   elif len(sim) == 5:
       print('\n Culpado')
   else:
       print('\n Inocente.')

			 #alteração