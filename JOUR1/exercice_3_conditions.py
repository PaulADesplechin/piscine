

def demo_conditions():
    """Demonstration des conditions"""
    print("=== Conditions ===")

    nombre = 7
    if nombre % 2 == 0:
        print(f"{nombre} est pair")
    else:
        print(f"{nombre} est impair")
    
    
    age = 20
    if age >= 18:
        print("Peut voter")
    else:
        print("Ne peut pas voter")
    
    
    note = 14
    if note >= 16:
        print("Tres bien")
    elif note >= 14:
        print("Bien")
    elif note >= 12:
        print("Assez bien")
    else:
        print("Insuffisant")

if __name__ == "__main__":
    demo_conditions()
