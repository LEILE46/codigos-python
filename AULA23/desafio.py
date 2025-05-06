alunos={ "leileane": 8,
         "erica":7,
        "vinicios":6}

print("Alunos aprovados:")
for nome,nota in alunos.items():
    if (nota)>= 7:
        print(f"{nome} = Nota: {nota}")