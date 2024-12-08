import os
import src.flipIslemi as flipIslemi
import src.grayIslemi as grayIslemi
import src.blurIslemi as blurIslemi
import src.rotate180 as rotate180
import src.rotate90 as rotate90

def get_folder_path():
    while True:
        folder_path = input("Lütfen resimlerin bulunduğu klasör yolunu girin (Çıkmak için 'q' tuşuna basın): ")
        if folder_path.lower() == 'q':
            return None
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            return folder_path
        else:
            print("Geçersiz klasör yolu, lütfen tekrar deneyin.")

def perform_operation(secim, folder_path):
    operations = {
        1: ("Flip İşlemi", flipIslemi.flip_images_in_folder),
        2: ("Gray İşlemi", grayIslemi.apply_grayscale_and_save),
        3: ("Blur İşlemi", blurIslemi.apply_blur_and_save),
        4: ("180 Derece Döndürme", rotate180.rotate_images_180_and_save),
        5: ("90 Derece Döndürme", rotate90.rotate_images_90_and_save)
    }
    try:
        if secim in operations:
            operations[secim][1](folder_path)
            print(f"{operations[secim][0]} başarıyla tamamlandı.")
        else:
            print("Geçersiz seçim")
            return False
        return True
    except Exception as e:
        print(f"İşlem sırasında bir hata oluştu: {e}")
        return False

def main():
    while True:
        print("1- Flip İşlemi")
        print("2- Gray İşlemi")
        print("3- Blur İşlemi")
        print("4- 180 Derece Döndürme")
        print("5- 90 Derece Döndürme")
        print("Çıkmak için 'q' tuşuna basın")

        secim = input("Seçiminizi yapınız: ").lower()
        if secim == 'q':
            print("Programdan çıkılıyor...")
            break

        try:
            secim = int(secim)
        except ValueError:
            print("Geçerli bir sayı giriniz")
            continue

        folder_path = get_folder_path()
        if folder_path is None:
            print("Programdan çıkılıyor...")
            break
        
        if perform_operation(secim, folder_path):
            another_operation = input("Başka bir işlem yapmak ister misiniz? (E/h): ").lower()
            if another_operation != 'e':
                print("Programdan çıkılıyor...")
                break
        else:
            retry = input("Geçersiz seçim veya işlem sırasında bir hata oluştu. Tekrar denemek ister misiniz? (E/h): ").lower()
            if retry != 'e':
                print("Programdan çıkılıyor...")
                break

if __name__ == "__main__":
    main()
