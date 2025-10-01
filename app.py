import csv
import streamlit as st

# --- Fungsi untuk load data ---
def load_news(filename):
    """Baca file news_data.csv ke list of dict"""
    # TODO: buka file CSV (filename) dan baca dengan csv.DictReader
    # kembalikan hasilnya dalam bentuk list
    with open(filename, 'r', encoding='utf-8') as datafile:
        reader = csv.DictReader(datafile)
        return list(reader)
    
def load_comments(filename):
    """Baca file comment_news.csv ke list of dict"""
    # TODO: sama seperti load_news tapi untuk file komentar
    with open(filename, 'r', encoding='utf-8') as datafile:
        reader = csv.DictReader(datafile)
        return list(reader)

# --- Fungsi untuk memproses data ---
def process_data(news_list, comments_list):
    """
    Gabungkan berita dan komentar,
    hitung jumlah komentar & rata-rata rating.
    Hasilnya list of dict.
    """
    # TODO: Buat dictionary untuk kumpulkan komentar per idBerita
    comments_per_news = {}

    for komen in comments_list:
        idb = komen['idBerita']
        rating = float(komen['Rating']) if komen['Rating'] else 0
        if idb not in comments_per_news:
            comments_per_news[idb] = {"Rating": []}
        comments_per_news[idb]["Rating"].append(rating)

    # TODO: isi comments_per_news dari comments_list
    # hint: per idBerita simpan Rating (list) dan count

    # TODO: Buat list hasil gabungan
    result = []
    for n in news_list:
        idb = n['idBerita']
        headline = n['Headline']
        # TODO: cek apakah idb ada di comments_per_news,
        # hitung rata-rata rating dan jumlah komentar
        if idb in comments_per_news:
            rating = comments_per_news[idb]["Rating"]
            jumlah = len(rating)
            rata = sum(rating) / jumlah if jumlah > 0 else 0.0
        else:
            rata = 0  # ganti dengan hitungan
            jumlah = 0  # ganti dengan hitungan

        result.append({
            'ID Berita': idb,
            'Headline': headline,
            'Rata-rata Rating': round(rata, 2),
            'Jumlah Komentar': jumlah
        })

    # --- Urutkan berdasarkan rating pakai fungsi biasa ---
    def ambil_rating(item):
        return item['Rata-rata Rating']

    # TODO: urutkan result berdasarkan ambil_rating reverse=True
    result = sorted(result, key=ambil_rating, reverse=True)
    return result

# --- Fungsi untuk tampilkan di Streamlit ---
def main():
    st.title("Analisis Sentimen & Popularitas Berita")
    st.write("Menampilkan ID, Headline, Rata-rata Rating, dan Jumlah Komentar, diurutkan dari Rating tertinggi.")

    # TODO: baca data CSV
    news_data = load_news("news_data.csv")     # ganti dengan pemanggilan load_news
    comment_data = load_comments("comment_news.csv")  # ganti dengan pemanggilan load_comments

    # TODO: proses data
    hasil = process_data(news_data, comment_data)  # ganti dengan pemanggilan process_data

    # TODO: tampilkan tabel di Streamlit
    # hint: gunakan st.table(hasil)
    st.table(hasil)

if __name__ == '__main__':
    main()
