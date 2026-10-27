
agenda = {
    "Maria": "99999-1234",
    "João": "98888-5678",
    "Pedro": "97777-4321"
}

print("AGENDA TELEFÔNICA")

for nome, telefone in agenda.items():
    print(nome, "-", telefone)

print("\nTelefone da Maria:", agenda["Maria"])
