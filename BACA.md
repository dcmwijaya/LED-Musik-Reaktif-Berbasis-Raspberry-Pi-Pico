[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?style=flat)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?logo=github&color=%23F7DF1E)](https://opensource.org/licenses/MIT)
![GitHub last commit](https://img.shields.io/github/last-commit/devancakra/LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico)
![Project](https://img.shields.io/badge/Project-Raspberry%20Pi%20Pico-light.svg?style=flat&logo=raspberrypi&logoColor=white&color=%23F7DF1E)

# LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico
<strong>Proyek Tunggal: LED Musik Reaktif Berbasis Raspberry Pi Pico</strong><br><br>


## Kebutuhan Proyek
| Bagian | Deskripsi |
| --- | --- |
| Papan Pengembangan | Raspberry Pi Pico |
| Editor Kode | Thonny IDE |
| Bootloader | MicroPython UF2 |
| Bahasa Pemrograman | MicroPython |
| Paket | • machine (bawaan)<br>• utime (bawaan) |
| Aktuator | LED (x9) |
| Sensor | FC-04: Sensor Suara (x1) |
| Komponen Lainnya | • Kabel USB mikro - USB tipe A (x1)<br>• Kabel jumper (1 set)<br>• Breadboard (x1) |

<br><br>

## Unduh & Instal
1. Thonny IDE

   <table><tr><td width="810">

   ```
   https://thonny.org/
   ```

   </td></tr></table><br>

2. MicroPython UF2

   <table><tr><td width="810">

   ```
   https://bit.ly/MicroPython_UF2
   ```

   </td></tr></table>
   
<br><br>

## Rancangan Proyek
<table>
<tr>
<th width="280">Diagram Blok</th>
<th width="280">Diagram Ilustrasi</th>
<th width="280">Pengkabelan</th>
</tr>
<tr>
<td><img src="https://github.com/devancakra/LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico/assets/54527592/bb91d3f4-d02a-4c98-9538-6bf1f0de724f" alt="Block-Diagram"></td>
<td><img src="https://github.com/devancakra/LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico/assets/54527592/46697952-d430-432c-94fb-fcea55ab3f8c" alt="Pictorial-Diagram"></td>
<td><img src="https://github.com/devancakra/LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico/assets/54527592/10717ed4-ce88-40d7-b2c2-1bae12c23503" alt="Wiring"></td>
</tr>
</table>

<br><br>

## Pengaturan Bootloader MicroPython
1. ``` Unggah firmware ``` :

   <table><tr><td width="810">    

      - Tekan dan tahan tombol ``` BOOTSEL ``` yang ada di papan ``` Raspberry Pi Pico ``` sembari menyambungkan ke komputer melalui kabel ``` mikro USB ```.
        
      - Setelah ``` Raspberry Pi Pico ``` dikenali oleh komputer (terhubung), maka segera lepaskan tombol ``` BOOTSEL ```.
      
      - Ketika berhasil terhubung, maka sebuah drive baru bernama ``` RPI-RP2 ``` akan terbuka.
      
      - ``` Seret -> Lepaskan ``` atau ``` Salin -> Tempelkan ``` file firmware ``` MicroPython UF2 ``` ke dalam drive ``` RPI-RP2 ```.

   </td></tr></table><br>

2. Setelah prosesnya berhasil, maka drive ``` RPI-RP2 ``` akan otomatis tertutup.<br><br>

3. Secara umum, unggah firmware itu hanya perlu dilakukan sekali saja saat anda pertama kali menggunakan board ``` Raspberry Pi Pico ```.

<br><br>

## Pengaturan Thonny IDE
1. Buka ``` Thonny IDE ``` terlebih dahulu.<br><br>

2. Klik ``` Tools ``` -> lalu pilih ``` Options... ``` -> selanjutnya pilih :<br><br>
   
   • ``` Menu Interpreter ```, kemudian ubah bagian :

      <table><tr><td width="810">

      - ``` Interpreter ``` -> ``` MicroPython (Raspberry Pi Pico) ```
        
      - ``` Port ``` -> ``` Board CDC @ COM... ```
  
      - ``` Restart interpreter before running a script ``` -> ``` hapus centang ```

   </td></tr></table>
   
   • ``` Menu Editor ```, kemudian centang semua opsinya kecuali: ``` Indent with tab characters ```.<br><br>

3. Jika tampilan berkas belum ada di ``` Thonny IDE ```, maka silakan anda klik bagian ``` View ``` -> lalu pilih ``` Files ``` untuk menampilkannya.<br><br>

4. Kemudian cari berkas bernama ``` main.py ``` di dalam direktori: ``` LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico/Src ```.<br><br>
   
5. Klik kanan pada berkas tersebut -> pilih ``` Upload to / ```.<br><br>

6. Buka berkas ``` main.py ``` yang ada di penyimpanan ``` Raspberry Pi Pico ``` -> lalu klik ``` Run current script (F5) ```.<br><br>

7. Kode program berhasil di eksekusi -> tandanya: ``` %run -c $EDITOR_CONTENT ```.<br><br>

8. Jika saat unggah program masih terdapat masalah, maka coba periksa pada bagian ``` interpreter ``` / ``` port ``` / ``` yang lainnya ```.

<br><br>

## Memulai
1. Unduh dan ekstrak repositori ini.<br><br>
   
2. Pastikan anda memiliki komponen elektronik yang diperlukan.<br><br>
   
3. Pastikan komponen anda telah dirancang sesuai dengan diagram.<br><br>
    
4. Konfigurasikan perangkat anda menurut pengaturan di atas.<br><br>

5. Selamat menikmati [Selesai].

<br><br>

## Sorotan
<table>
<tr>
<th width="420">Tampilan-1</th>
<th width="420">Tampilan-2</th>
</tr>
<tr>
<td><img width="840" src="https://github.com/devancakra/LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico/assets/54527592/6cacee09-4b5c-428f-ace2-0d7d7a1466e6" alt="img-1"></td>
<td><img width="840" src="https://github.com/devancakra/LED-Musik-Reaktif-Berbasis-Raspberry-Pi-Pico/assets/54527592/1757076e-3e19-401a-8afa-c6c6becae9e2" alt="img-2"></td>
</tr>
</table>

<br><br>

## Apresiasi
Jika karya ini bermanfaat bagi anda, maka dukunglah karya ini sebagai bentuk apresiasi kepada penulis dengan mengklik tombol ``` ⭐Bintang ``` di bagian atas repositori.

<br><br>

## LISENSI
LISENSI MIT - Hak Cipta © 2024 - Devan C. M. Wijaya, S.Kom

Dengan ini diberikan izin tanpa biaya kepada siapa pun yang mendapatkan salinan perangkat lunak ini dan file dokumentasi terkait perangkat lunak untuk menggunakannya tanpa batasan, termasuk namun tidak terbatas pada hak untuk menggunakan, menyalin, memodifikasi, menggabungkan, mempublikasikan, mendistribusikan, mensublisensikan, dan/atau menjual salinan Perangkat Lunak ini, dan mengizinkan orang yang menerima Perangkat Lunak ini untuk dilengkapi dengan persyaratan berikut:

Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus menyertai semua salinan atau bagian penting dari Perangkat Lunak.

DALAM HAL APAPUN, PENULIS ATAU PEMEGANG HAK CIPTA DI SINI TETAP MEMILIKI HAK KEPEMILIKAN PENUH. PERANGKAT LUNAK INI DISEDIAKAN SEBAGAIMANA ADANYA, TANPA JAMINAN APAPUN, BAIK TERSURAT MAUPUN TERSIRAT, OLEH KARENA ITU JIKA TERJADI KERUSAKAN, KEHILANGAN, ATAU LAINNYA YANG TIMBUL DARI PENGGUNAAN ATAU URUSAN LAIN DALAM PERANGKAT LUNAK INI, PENULIS ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB, KARENA PENGGUNAAN PERANGKAT LUNAK INI TIDAK DIPAKSAKAN SAMA SEKALI, SEHINGGA RISIKO ADALAH MILIK ANDA SENDIRI.
