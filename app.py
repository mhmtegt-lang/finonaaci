import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Sayfa Ayarları
st.set_page_config(page_title="Matematik ve Doğa: Fibonacci", layout="wide")

st.title("🌿 Doğanın Şifresi: Fibonacci Spirali")
st.markdown("**Matematik ve Doğa Temalı Proje Çalışması**")
st.write("Aşağıdaki kaydırıcıyı (slider) kullanarak doğadaki altın oranın adım adım nasıl büyüdüğünü keşfedin!")

# Fibonacci hesaplama fonksiyonu
def get_fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Kullanıcı Etkileşimi: Slider
adim_sayisi = st.slider("Kaçıncı adıma kadar çizelim?", min_value=1, max_value=8, value=4, step=1)

# Çizim Alanı
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off') # Eksenleri gizle

fib_sayilari = get_fibonacci(adim_sayisi)
renkler = ['#FF9999', '#FFCC99', '#FFFF99', '#99FF99', '#99FFFF', '#9999FF', '#CC99FF', '#FF99CC']

# Başlangıç noktası ve yönler
x, y = 0, 0
aci = 0

for i, f in enumerate(fib_sayilari):
    # Kareyi çiz
    if i == 0:
        kare = patches.Rectangle((x, y), f, f, edgecolor='black', facecolor=renkler[i], alpha=0.7)
        merkez_x, merkez_y = x + f/2, y + f/2
    elif i == 1:
        x = x + fib_sayilari[0]
        kare = patches.Rectangle((x, y), f, f, edgecolor='black', facecolor=renkler[i], alpha=0.7)
        merkez_x, merkez_y = x + f/2, y + f/2
    else:
        # Yön hesaplama (sola, aşağı, sağa, yukarı döngüsü)
        yon = i % 4
        if yon == 2: # Sola ve aşağı
            x = x - f
            y = y - fib_sayilari[i-2]
        elif yon == 3: # Aşağı ve sağa
            y = y - f
            x = x + fib_sayilari[i-1]
        elif yon == 0: # Sağa ve yukarı
            x = x + fib_sayilari[i-1]
            y = y + fib_sayilari[i-2]
        elif yon == 1: # Yukarı ve sola
            x = x - fib_sayilari[i-2]
            y = y + f
            
        kare = patches.Rectangle((x, y), f, f, edgecolor='black', facecolor=renkler[i], alpha=0.7)
        merkez_x, merkez_y = x + f/2, y + f/2

    ax.add_patch(kare)
    
    # Karenin içine sayıyı yaz
    ax.text(merkez_x, merkez_y, str(f), ha='center', va='center', fontsize=12, fontweight='bold')

    # Yayı (Spirali) çiz
    yay_merkez_x = x if (i%4==0 or i%4==3) else x+f
    yay_merkez_y = y if (i%4==2 or i%4==3) else y+f
    
    yay = patches.Arc((yay_merkez_x, yay_merkez_y), f*2, f*2, angle=0, theta1=90-(i%4)*90, theta2=180-(i%4)*90, color='blue', linewidth=2)
    ax.add_patch(yay)

# Grafiği sınırlandır
ax.autoscale_view()
st.pyplot(fig)

# Bilgi Kutusu
st.info(f"**Şu anki Fibonacci Sayıları:** {fib_sayilari}\n\n"
        "Doğada çam kozalakları, ayçiçeği çekirdekleri ve deniz kabukları tam olarak bu çizdiğimiz matematiksel büyüme modelini takip eder.")
