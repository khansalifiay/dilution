import streamlit as st

st.subheader('Hi! :wave:')
st.title('KALKULATOR PENGENCERAN')
st.markdown('Aplikasi yang bertujuan untuk memudahkan dalam menghitung volume larutan yang dibutuhkan saat akan melakukan pengenceran suatu larutan.')

st.write('-----')

st.markdown('Pengenceran berarti mengurangi konsentrasi larutan dengan menambahkan pelarut. Selama proses pengenceran, volume dan molaritas berubah sedangkan jumlah mol tetap sama. Setiap larutan yang dibuat pasti mempunyai kepekatan atau konsentrasi tertentu.')

st.write('-----')

st.write('Kelompok 7 :')
col1, col2=st.columns(2)
with col1:
   st.write(''' 
\n :boy: Angga Putra Haryanto (2220445)
\n :boy: Yoga Danuarta (2220499)
\n :boy: Uristyo Utomo (2119005)''')
with col2:
    st.write(''' 
\n :girl: Khansa Alifia Yasmin (2220463)
\n :girl: Maria Asumta P.D.A (2220465)
\n :girl: Nita Agustin Sapitri (2220478)''')

st.write('-----')

st.write('''Rumus Pengenceran:
\nC1.V1=C2.V2
\n :small_orange_diamond: C1 merupakan konsentrasi yang diinginkan
\n :small_orange_diamond: C2 merupakan konsentrasi yang dimiliki
\n :small_orange_diamond: V1 merupakan volume yang diinginkan
\n :small_orange_diamond: V2 merupakan volume yang harus dipindahkan''')

st.write('-----')

st.write('silahkan masukkan angka')
c1=st.number_input('konsentrasi yang diinginkan')
v1=st.number_input('volume yang diinginkan (mL)')
c2=st.number_input('konsentrasi yang dimiliki')

if st.button('hitung'):
    v2=(c1*v1)/c2
    st.write(f'volume yang harus dipindahkan adalah {v2} mL')
else:
    st.write('silahkan tekan tombol hitung')
    
st.write('-----')

st.markdown('Terimakasih sudah menggunakan aplikasi ini, semoga bermanfaat!')