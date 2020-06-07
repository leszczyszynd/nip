from help import help_functions as hf

how_much = int(input('Podaj liczbę nipów do wygenerowania :'))
generated = hf.nip_generate(how_much)
for k,v in generated.items():
    print(f'NIP : "{k}" nadany przez "{v}"')



