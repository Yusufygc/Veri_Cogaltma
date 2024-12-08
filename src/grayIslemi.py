import os
import glob
from PIL import Image

def apply_grayscale_and_save(folder_path):
    # Verilerin olduğu klasörle aynı dizinde Gray klasörünü oluştur (eğer yoksa)
    parent_folder_path = os.path.dirname(folder_path)
    gray_folder_path = os.path.join(parent_folder_path, "gray")
    os.makedirs(gray_folder_path, exist_ok=True)
    
    # Klasördeki tüm .jpg dosyalarını bul
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg"))
    
    for image_path in image_paths:
        # Resmi oku
        image = Image.open(image_path)
        
        # Resme gri filtre uygula
        gray_image = image.convert("L")
        
        # Yeni dosya adı oluştur
        base_name = os.path.basename(image_path)
        new_name = f"{os.path.splitext(base_name)[0]}_gray.jpg"
        new_path = os.path.join(gray_folder_path, new_name)
        
        # Gri filtre uygulanmış resmi kaydet
        gray_image.save(new_path)

# Örnek kullanım
folder_path = "/path/to/your/images"  # Kendi klasör yolunuzu buraya ekleyin
apply_grayscale_and_save(folder_path)


# Kullanım örneği:
# apply_grayscale_and_save('/path/to/your/folder')


#apply_grayscale_and_save("C:\\Users\\TUF Dash F15\\Desktop\\DataCogalt\\veri")