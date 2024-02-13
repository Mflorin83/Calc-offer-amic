import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def create_app():
    root = tk.Tk()
    root.title("Calculator tarife AMIC")
    root.geometry("1024x768")
    root.configure(background='#F4FAFC')

    questions_and_comboboxes = {}
    editable_questions_entries = {}

    def is_numeric(P):
        return P.isdigit() or P == ""

    validate_numeric = root.register(is_numeric)

    def calculate_cost_for_salariati(numar_salariati):
        if numar_salariati <= 3:
            return 50
        else:
            return 50 + (numar_salariati - 3) * 10

    def calculate_cost_for_facturi(numar_facturi):
        if numar_facturi <= 10:
            return 20 + numar_facturi * 10
        else:
            return 120 + (numar_facturi - 10) * 5

    def calculate_cost_for_conturi(numar_conturi):
        costuri = {
            0: 0, 1: 30, 2: 60, 3: 80, 4: 90, 5: 100, 6: 105, 7: 110, 8: 115, 9: 120,
            10: 125, 11: 130, 12: 135, 13: 140, 14: 145, 15: 150, 16: 155, 17: 160,
            18: 165, 19: 170, 20: 175
        }
        if numar_conturi <= 20:
            return costuri.get(numar_conturi, 175)
        else:
            return 175 + (numar_conturi - 20) * 10

    def calculate_price():
        total_price = 0
        print(f"Total inițial: {total_price}")
        error_occurred = False  # Flag pentru a indica dacă a apărut o eroare
        for question, combobox in questions_and_comboboxes.items():
            answer = combobox.get()
            print(f"Răspuns la '{question}': {answer}")  # Debug: Afișează răspunsul la întrebările cu Combobox
            # Logica de calcul a prețului pe baza răspunsurilor la întrebările cu Combobox
            if question == "În ce domeniu de activitate va desfășurați business-ul?":
                if answer == "Comerț (cumpăr și revând)":
                    total_price += 100
                elif answer == "Prestez servicii":
                    total_price += 50
                elif answer == "Produc lucruri":
                    total_price += 150
                print(f"Total după '{question}': {total_price}")
            if question == "Compania este plătitoare de TVA?":
                if answer == "Nu sunt plătitor de TVA.":
                    total_price += 0
                elif answer == "Sunt plătitor lunar de TVA.":
                    total_price += 100
                elif answer == "Sunt plătitor trimestrial de TVA.":
                    total_price += 50
                print(f"Total după '{question}': {total_price}")
            if question == "Compania efectuează importuri de bunuri și servicii din alte țări?":
                if answer == "NU":
                    total_price += 0
                elif answer == "Da, doar din țări UE.":
                    total_price += 50
                elif answer == "Da, doar din țări non-UE.":
                    total_price += 50
                elif answer == "Atât din UE cât și din țări non-UE.":
                    total_price += 100
                print(f"Total după '{question}': {total_price}")
        for question, entry in editable_questions_entries.items():
            answer = entry.get()
            print(f"Răspuns la '{question}': {answer}")  # Debug: Afișează răspunsul la întrebările editabile
            # Logica de calcul a prețului pe baza răspunsurilor la întrebările cu răspunsuri editabile
            if question == "Câți salariați are compania dumneavoastră?":
                try:
                    num_salariati = int(answer)
                    total_price += calculate_cost_for_salariati(num_salariati)
                    print(f"Total după '{question}': {total_price}")
                except ValueError:
                    messagebox.showerror("Eroare", "Răspunsul trebuie să fie numeric.")
                    error_occurred = True  # Setează flag-ul pe True dacă apare o eroare

            elif question == "Care este numărul mediu de documente lunare (facturi, bonuri, chitante) pe care le primiți de la furnizori?":
                try:
                    numar_facturi = int(answer)
                    total_price += calculate_cost_for_facturi(numar_facturi)
                    print(f"Total după '{question}': {total_price}")
                except ValueError:
                    messagebox.showerror("Eroare", "Numărul de facturi trebuie să fie un număr întreg.")
                    error_occurred = True

            elif question == "Care este numărul mediu de documente lunare emise (facturi, raport zilnic de vânzări casă de marcat)?":
                try:
                    numar_documente_emise = int(answer)
                    # Presupunând că aveți o funcție de calcul similară pentru documente emise
                    total_price += calculate_cost_for_facturi(numar_documente_emise)
                    print(f"Total după '{question}': {total_price}")
                except ValueError:
                    messagebox.showerror("Eroare", "Numărul de documente emise trebuie să fie un număr întreg.")
                    error_occurred = True

            elif question == "Câte conturi bancare are societatea?":
                try:
                    numar_conturi = int(answer)
                    total_price += calculate_cost_for_conturi(numar_conturi)
                    print(f"Total după '{question}': {total_price}")
                except ValueError:
                    messagebox.showerror("Eroare",
                                         "Numărul de conturi bancare trebuie să fie un număr întreg.")
                    error_occurred = True  # Setează flag-ul pe True dacă apare o eroare

        if error_occurred:
            messagebox.showerror("Eroare", "Unul sau mai multe răspunsuri sunt incorecte. Te rog să verifici.")
        else:
            messagebox.showinfo("Preț calculat", f"Preț: {total_price} RON")

    def blink_price_label():
        current_color = price_label.cget("foreground")
        next_color = "red" if current_color == "black" else "black"
        price_label.config(foreground=next_color)
        root.after(500, blink_price_label)
        # Crearea unui obiect de validare

    validate_numeric = root.register(is_numeric)
    # Încărcarea și afișarea logoului
    logo_path = r"C:\Users\flori\OneDrive\Desktop\Calculator tarife AMIC\Amic logo final.png"  # Actualizează calea
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Crearea unui frame pentru logo și titlu
    top_frame = tk.Frame(root, background='#F4FAFC')
    top_frame.pack(side="top", fill="x")

    # Adăugarea logoului în frame
    logo_label = tk.Label(top_frame, image=logo_photo, background='#F4FAFC')
    logo_label.image = logo_photo
    logo_label.pack(side="left", padx=10)

    # Adăugarea titlului în frame
    title_label = tk.Label(top_frame, text="Cere o cotație de preț completând câmpurile de mai jos:",
                           background='#F4FAFC', font=("Poppins", 17))
    title_label.pack(side="left", padx=10)

    # Crearea unui frame pentru întrebări
    questions_frame = tk.Frame(root, background='#F4FAFC')
    questions_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Lista de întrebări cu răspunsuri editabile
    editable_questions = [
        "Care este numele companiei d-voastra?"
    ]
    # Crearea întrebărilor cu răspunsuri editabile
    for question in editable_questions:
        question_label = tk.Label(questions_frame, text=question, background='#F4FAFC', font=("Poppins", 12))
        question_label.pack(side="top", anchor="w")

        answer_entry = tk.Entry(questions_frame, font=("Poppins", 12), width=30)
        answer_entry.pack(side="top", anchor="w", pady=5)

    # Lista de întrebări și opțiuni pentru fiecare întrebare
    questions_and_options = {
        "În ce domeniu de activitate va desfășurați business-ul?": ["Comerț (cumpăr și revând)", "Prestez servicii",
                                                                    "Produc lucruri"],
        "Compania este plătitoare de TVA?": ["Nu sunt plătitor de TVA.", "Sunt plătitor lunar de TVA.",
                                             "Sunt plătitor trimestrial de TVA."],
        "Compania efectuează importuri de bunuri și servicii din alte țări?": ["NU", "Da, doar din țări UE.",
                                                                               "Da, doar din țări non-UE.",
                                                                               "Atât din UE cât și din țări non-UE."],
    }

    # Crearea întrebărilor și câmpurilor de răspuns de tip Combobox
    for question, options in questions_and_options.items():
        question_label = tk.Label(questions_frame, text=question, background='#F4FAFC', font=("Poppins", 12))
        question_label.pack(side="top", anchor="w")

        answer_combobox = ttk.Combobox(questions_frame, values=options, font=("Poppins", 12), state="readonly")
        answer_combobox.pack(side="top", anchor="w", pady=5)
        questions_and_comboboxes[question] = answer_combobox

    # Lista de întrebări cu răspunsuri editabile
    editable_questions_entries = {}
    editable_questions_numeric = [
        "Câți salariați are compania dumneavoastră?",
        "Care este numărul mediu de documente lunare (facturi, bonuri, chitante) pe care le primiți de la furnizori?",
        "Care este numărul mediu de documente lunare emise (facturi, raport zilnic de vânzări casă de marcat)?",
        "Câte conturi bancare are societatea?",

    ]

    # Crearea întrebărilor cu răspunsuri editabile numerice

    for question in editable_questions_numeric:
        question_label = tk.Label(questions_frame, text=question, background='#F4FAFC', font=("Poppins", 12))
        question_label.pack(side="top", anchor="w")

        answer_entry = tk.Entry(questions_frame, font=("Poppins", 12), width=30,
                                validate="key", validatecommand=(validate_numeric, '%P'))
        answer_entry.pack(side="top", anchor="w", pady=5)
        editable_questions_entries[question] = answer_entry

    # Funcția de validare pentru toate câmpurile
    def validate_all_fields():
        for _, combobox in questions_and_options.items():
            if not combobox.get():
                messagebox.showwarning("Avertisment", "Te rog să completezi toate câmpurile.")
                return

        for entry in editable_questions_numeric:
            if not entry.get():
                messagebox.showwarning("Avertisment", "Te rog să completezi toate câmpurile.")
                return
        # Crearea unui frame pentru buton și eticheta de preț
    bottom_frame = tk.Frame(root, background='#F4FAFC')
    bottom_frame.pack(side='top', fill="x", padx=5, pady=5)

    calculate_button = tk.Button(bottom_frame, text="Obține Ofertă!", command=calculate_price)
    calculate_button.pack(side="left")

    global price_label
    price_label = tk.Label(bottom_frame, text="", font=("Poppins", 12), foreground="white", background='#F4FAFC')
    price_label.pack(side='left')
    # ... [Restul definiției interfeței, inclusiv butoane, etichete și câmpuri de intrare]

    root.mainloop()
if __name__ == "__main__":
    create_app()