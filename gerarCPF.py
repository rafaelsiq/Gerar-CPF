#!/usr/bin/python2
#!-*- coding:UTF-8 -*-
import re
import sys
_translate = lambda cpf: ''.join(re.findall("\d", cpf))
def _exceptions(cpf):
    if len(cpf)!=11:
        return True
    else:
        s=''.join(str(x) for x in cpf)
        if s=='00000000000' or s=='11111111111' or s=='22222222222' or s=='33333333333' or s=='44444444444' or s=='55555555555' or s=='66666666666' or s=='77777777777' or s=='88888888888' or s=='99999999999':
            return True
    return False

def _gen(cpf):
    res = []
    for i, a in enumerate(cpf):
        b = len(cpf) + 1 - i
        res.append(b * a)

    res = sum(res) % 11

    if res > 1:
        return 11 - res
    else:
        return 0


class CPF(object):
    _gen = staticmethod(_gen)
    _translate = staticmethod(_translate)
    def __init__(self, cpf):
        if isinstance(cpf, basestring):
            if not cpf.isdigit():
               cpf = self._translate(cpf)
        self.cpf = [int(x) for x in cpf]

    def __getitem__(self, index):
        return self.cpf[index]

    def __repr__(self):
        return "CPF('%s')" % ''.join(str(x) for x in self.cpf)

    def __eq__(self, other):
        return isinstance(other, CPF) and self.cpf == other.cpf
    def __str__(self):
        d = iter("..-")
        s = map(str, self.cpf)
        for i in xrange(3, 12, 4):
            s.insert(i, d.next())
        r = ''.join(s)
        return r

    def isValid(self):
        if _exceptions(self.cpf):
            return False

        s = self.cpf[:9]
        s.append(self._gen(s))
        s.append(self._gen(s))
        return s == self.cpf[:]
inicial = "0"
cpf_con = [str]

# qualquer um dos dois formatos (com pontos ou não) pode ser usado

class Util(object):
    def validaCpf(self,cpf,d1=0,d2=0,i=0):
        while i<10:
            d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
        return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))

def substituirCPF(cpf):
    contador=int(0)
    if cpf.find("x".upper()) != -1:
        CPFgera = []
        CPF_temp = []
        for i in range(10):
            CPFgera.append(cpf)
        for i in CPFgera:
            CPF_temp.append(i.replace("X",str(contador),1))
            contador+=1
        contador =0
        teste = []
        CPFgera = CPF_temp
        for i in CPFgera:
            if i.find("X") > -1:
                teste = substituirCPF(i)
                for i in teste:
                    CPFgera.append(i)
        teste = []
        CPF_temp = []
        for i in CPFgera:
            if i.find("X") == -1:
                CPF_temp.append(i)
        CPFgera = CPF_temp
        return CPFgera
if __name__ == "__main__":
    CPForiginal =[]
    if sys.argv.__len__() <2:
    	cpf = raw_input("\nDigite um CPF substituindo por X os digitos desconhecidos:\nNão use pontos\n")
    #else:
	#cpf = sys.argv[1]

    if (len(cpf) == 11):
        CPForiginal = substituirCPF(cpf.upper())
    
    print("\n")
    contador = 0
    for i in CPForiginal:
        if Util().validaCpf(i):
            contador += 1
            print(CPF(i))
    print("___________________TOTAL DE CPFs = "+str(contador)+"___________________")
