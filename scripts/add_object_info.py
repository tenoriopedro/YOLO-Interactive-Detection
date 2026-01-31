from src.yolo_detector.database.operations import InfoData

# List of COCO classes translated into Portuguese
COCO_CLASSES_PT = [
    "pessoa", "bicicleta", "carro", "motocicleta", "avião", "autocarro",
    "comboio", "camião", "barco", "semáforo", "hidrante", "sinal de stop",
    "parquímetro", "banco", "pássaro", "gato", "cão", "cavalo", "ovelha",
    "vaca", "elefante", "urso", "zebra", "girafa", "mochila",
    "guarda-chuva", "carteira", "gravata", "mala", "frisbee", "esquis",
    "prancha de snowboard", "bola desportiva", "papagaio",
    "taco de baseball", "luva de baseball", "skate", "prancha de surf",
    "raquete de ténis", "garrafa", "copo de vinho", "chavena", "garfo",
    "faca", "colher", "taça", "banana", "maçã", "sanduiche", "laranja",
    "brocolos", "cenoura", "cachorro quente", "pizza", "donut", "bolo",
    "cadeira", "sofa", "planta em vaso", "cama", "mesa de jantar",
    "sanita", "televisão", "portátil", "rato", "comando", "teclado",
    "telemóvel", "microondas", "forno", "torradeira", "lava-loiça",
    "frigorífico", "livro", "relógio", "vaso", "tesoura",
    "urso depeluche", "secador de cabelo", "escova de dentes"
]

# If you want to add more classes to be detected,
# Run this file and then choose an exact name
# that is in the variable (COCO_CLASSES_PT),
# a description and a link


def main() -> None:
    print("=== Adicionar novo objeto à base de dados ===\n")

    info_data = InfoData()

    while True:
        obj = input("Nome do objeto (ex: cadeira): ").strip()
        if not obj:
            print("Nome do objeto não pode estar vazio.")
            continue

        if obj not in COCO_CLASSES_PT:
            print("Nome inválido.")
            continue

        description = input("Descrição do objeto: ").strip()
        if not description:
            print("Descrição não pode estar vazia.")
            continue

        link = input("Link com mais informações: ").strip()
        if not link:
            print("Link não pode estar vazio.")
            continue

        # Insert into database
        info_data.insert_into_database(obj, description, link)
        print(f"\nObjeto '{obj}' adicionado com sucesso!")

        more = input("\nDeseja adicionar outro? (s/n): ").strip().lower()
        if more != "s":
            break

    print("Finalizado.")


if __name__ == "__main__":
    main()
