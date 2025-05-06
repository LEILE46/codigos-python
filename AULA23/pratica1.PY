aluno1={"nome":"leileane","curso":"dev","ano":2025}
print (aluno1)
print(aluno1["curso"])
print(aluno1.get("nome"))
aluno1["idade"]=16
print(aluno1)
aluno1.update({'periodo':"vespertino"})
info={"telefone":'6799997070'}
aluno1.update(info)
print(aluno1)
aluno1.pop("telefone")
print(aluno1)
del aluno1  ["periodo"]
print(aluno1)
aluno1.clear()
print(aluno1)
aluno1={"nome":"leileane","curso":"dev","ano":2025}
aluno1.popitem()
print(aluno1)
aluno1.update(info)
for chave,valor in aluno1.items():
    print(f"{chave}: {valor}")