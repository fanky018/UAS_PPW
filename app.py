# main.py
import streamlit as st
from generate_label import get_label

def main():
    st.set_page_config(
        page_title="Aplikasi Kategori Berita | Klasifikasi Berita AntaraNews", page_icon="📺"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/banner.png", use_column_width=True)

    with col2:
        st.subheader("News Classification: Aplikasi Kategori untuk Berita")
        st.caption(
            "Berita umumnya dikategorikan menjadi beberapa jenis kategori seperti hukum, metro, dan humaniora. Dengan news classification ini kita dapat menemukan jenis kategori berita yang sesuai dengan isi berita tersebut."
        )

    news_text = st.text_area("Masukkan Isi Berita", key="input_text", height=250)

    if st.button("Cari Kategori"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                st.write(f'Berita yang anda masukkan termasuk dalam kategori: {text}')
                url = f"https://www.antaranews.com/{text.lower()}"
                st.write(f'Baca juga berita terbaru terkait {text} 🔎 [Berita {text} hari ini]({url})')
        else:
            st.warning('Masukkan teks terlebih dahulu')

if __name__ == "__main__":
    main()
