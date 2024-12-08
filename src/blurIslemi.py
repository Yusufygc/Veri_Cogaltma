import os
import glob
from PIL import Image, ImageFilter

def apply_blur_and_save(folder_path, blur_radius=2):
    # Verilerin olduğu klasörle aynı dizinde Blur klasörünü oluştur (eğer yoksa)
    parent_folder_path = os.path.dirname(folder_path)
    blur_folder_path = os.path.join(parent_folder_path, "blur")
    os.makedirs(blur_folder_path, exist_ok=True)
    
    # Klasördeki tüm .jpg dosyalarını bul
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg"))
    
    for image_path in image_paths:
        # Resmi oku
        image = Image.open(image_path)
        
        # Resme blur filtre uygula
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        
        # Yeni dosya adı oluştur
        base_name = os.path.basename(image_path)
        new_name = f"{os.path.splitext(base_name)[0]}_blur.jpg"
        new_path = os.path.join(blur_folder_path, new_name)
        
        # Blur filtre uygulanmış resmi kaydet
        blurred_image.save(new_path)

# Örnek kullanım
folder_path = "/path/to/your/images"  # Kendi klasör yolunuzu buraya ekleyin
apply_blur_and_save(folder_path)

# Kullanım örneği:
# apply_blur_and_save('/path/to/your/folder', blur_radius=2)



#apply_blur_and_save("C:\\Users\\TUF Dash F15\\Desktop\\DataCogalt\\veri")