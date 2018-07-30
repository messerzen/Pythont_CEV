def calc_pag(qhoras, vhoras):
    horas = float(qhoras)
    taxa = float(vhoras)
    if horas <= 40:
        salario=horas*taxa
    else:
        hexcd=horas - 40
        salario = 40*taxa*(hexcd*(1.5*taxa))
    return salario
str_horas=float(input('Digite a quantidade de horas trabalhadas: '))
str_taxa=float(input('Digite o valor pago por horas: '))
total=calc_pag(str_horas,str_taxa)
print(f'O valor total a receber é R${total}')