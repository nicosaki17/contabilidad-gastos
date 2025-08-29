import os

DATA_DIR  = "data"
FILENAME = os.path.join(DATA_DIR, "gastos_data.txt")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#GUARDAR EN .TXT
def save_data(datas):
    with open(FILENAME, "w", encoding= "utf-8") as f:
        for d in datas:
            f.write(f"{d['name']} - {d['amount']} - {d['date']} - {d['reason']}\n")

#CARGAR DESDE .TXT
def load_data():
    if not os.path.exists(FILENAME):
        return[]
    datas = []
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            name, amount, date, reason = line.strip().split(" - ")
            datas.append({"name": name, "amount": float(amount), "date": date, "reason": reason})

    return datas

#MOSTRAR GASTOS
def show_data(datas):
    if not datas:
        print("no hay gastos guardados\n")
        return
    for i, d in enumerate(datas, 1):
        print(f"{i}- Gasto: {d['name']}\n Valor: {d['amount']}\n Fecha: {d['date']}\n Motivo: {d['reason']}\n---")

#AGREGAR UN GASTO
def add_data(datas):
    name = input("Ingrese el gasto:")
    while True:
        try:
            amount = float(input("Ingrese el valor: "))
            break

        except ValueError:
            print("Ingrese un valor numerico")

    date = input("Ingrese la fecha: ")
    reason = input("Ingrese el motivo: ")
    datas.append({"name": name, "amount": amount, "date": date, "reason": reason})
    save_data(datas)
    print("--Gasto agregado--")

#ELIMINAR UN GASTO
def del_data(datas):
    show_data(datas)
    try:
        choice = int(input("Numero de gasto a eliminar"))
        datas.pop(choice - 1)
        save_data(datas)
        print("Gasto eliminado correctamente")
    except (ValueError, IndexError):
        print("El gasto no existe")

#SUMAR GASTOS
def total_data(datas):
    if not datas:
        print("No hay gastos.")
        return
    total = sum(d['amount'] for d in datas)
    print(f"Total de gastos: {total}")

#MENU PRINCIPAL
def main():
    datas = load_data()
    
    while True:
        print("ELIGE UNA OPCION")
        print("1- Agregar gasto")
        print("2- Ver gastos")
        print("3- Eliminar gastos")
        print("4- Total de gastos")
        print("5- Salir")
        opt = input("Opcion: ")

        if opt== "1":
            add_data(datas)
        elif opt == "2":
            show_data(datas)
        elif opt == "3":
            del_data(datas)
        elif opt == "4":
            total_data(datas)
        elif opt == "5":
            print("Saliendo")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()