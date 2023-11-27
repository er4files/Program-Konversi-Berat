def convert_weight(amount, from_unit, to_unit):
    # Dictionary untuk menyimpan faktor konversi antar satuan berat
    units = {
        'gram': 1,
        'kilogram': 1000,
        'ons': 28.3495,
        'pound': 453.592,
        'ton': 1000000
    }

    # Periksa apakah satuan berat yang dimasukkan valid
    if from_unit not in units or to_unit not in units:
        print("Satuan berat tidak valid.")
        return None

    # Hitung hasil konversi
    result = amount * units[from_unit] / units[to_unit]
    return result

def main():
    # Tampilkan judul program dengan bingkai
    print("=====================================")
    print("|      Program Konversi Berat       |")
    print("=====================================")

    # Masukkan jumlah berat dan satuan berat awal
    amount = float(input("Masukkan jumlah berat: "))
    from_unit = input("Satuan berat dari (gram/kilogram/ons/pound/ton): ").lower()
    to_unit = input("Satuan berat ke (gram/kilogram/ons/pound/ton): ").lower()

    # Panggil fungsi konversi berat
    converted_weight = convert_weight(amount, from_unit, to_unit)

    # Tampilkan hasil konversi jika valid
    if converted_weight is not None:
        print(f"{amount} {from_unit.capitalize()} sama dengan {converted_weight} {to_unit.capitalize()}")

if __name__ == "__main__":
    main()
