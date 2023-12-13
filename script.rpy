﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aria")
define d = Character("Dr. Hikari")
define b = Character("Bryan")

# The game starts here.

label start:

    # Prolog...
    "Dalam dunia yang penuh dengan misteri dan keajaiban, terdapat sebuah sekolah khusus yang menyimpan rahasia tak terduga. Sekolah ini tidak biasa, karena di dalamnya terdapat sesuatu yang disebut 'Pintu Gerbang Alam Semesta.' Pintu ini, suatu keajaiban yang aneh, membawa karakter utama kita, Aria, ke dalam petualangan yang melibatkan pengetahuan, budaya, dan sejarah di seluruh dunia."

    "Aria, seorang siswi yang penuh semangat untuk belajar, menemukan Pintu Gerbang Alam Semesta secara tak sengaja. Tanpa menyadari kekuatan besar di baliknya, dia bersiap-siap untuk memulai perjalanan yang akan mengubah hidupnya."

    "Episode 1: 'Pembukaan Pintu Alam Semesta'"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "aria.png" to the images
    # directory.

    show a at left
    "Aria: (dengan penuh keheranan) 'Apa ini? Mengapa tidak pernah kudengar sebelumnya?'"

    # Display lines of dialogue.

    "Suatu hari, di sekolah khusus itu, Aria tanpa sengaja menemukan ruang tersembunyi yang tidak terlihat oleh mata manusia biasa. Di ruang itu, terdapat Pintu Gerbang Alam Semesta."

    show a at left
    "Aria: (dengan penuh keheranan) 'Apa ini? Mengapa tidak pernah kudengar sebelumnya?'"

    "Tanpa berpikir panjang, Aria memutuskan untuk membuka pintu misterius tersebut. Begitu pintu terbuka, dia merasakan kekuatan ajaib yang menyeretnya masuk ke dalam sebuah portal cahaya yang mempesona."

    "Sesaat kemudian, Aria mendapati dirinya berdiri di tengah-tengah hutan hujan Amazon. Keindahan alam yang luar biasa dan suara alam yang merdu memenuhi telinganya."

    show a at left
    "Aria: 'Ini... ini luar biasa! Tapi, bagaimana aku bisa berada di sini?'"

    # Seorang pria muncul dari bayangan. Dia mengenakan pakaian eksplorasi dan tersenyum ramah.

    show d at right
    "Dr. Hikari: 'Selamat datang, Aria. Kamu telah membuka Pintu Gerbang Alam Semesta. Bersiaplah untuk petualangan ilmiah dan pengetahuan yang tak terduga.'"

    show a at left
    "Aria: 'Siapa Anda? Dan mengapa saya di sini?'"

    show d at right
    "Dr. Hikari: 'Saya Dr. Hikari, profesor eksplorasi di sekolah ini. Kamu di sini untuk menjelajahi pengetahuan di seluruh dunia. Mari kita mulai petualangan ini!'"

    "Dr. Hikari menjelaskan pada Aria tentang keberadaan Pintu Gerbang Alam Semesta dan mengapa dia dipilih untuk menjalani petualangan ini. Dengan antusias, Aria setuju untuk menjelajahi tempat-tempat bersejarah."

    "Bersama-sama, mereka melangkah keluar dari hutan Amazon dan tiba di Piramida Mesir. Puncak piramida menawarkan pemandangan matahari terbenam yang memukau."

    show a at left
    "Aria: 'Wow, pemandangannya sungguh mengagumkan! Piramida ini lebih besar dari yang pernah saya bayangkan.'"

    show d at right
    "Dr. Hikari: 'Kalian berdua, kita tidak hanya datang ke sini untuk menikmati pemandangan. Ada sesuatu yang menarik perhatian saya. Lihatlah ke arah matahari terbenam di sana.'"

    "Ketiganya memandang ke arah matahari yang perlahan tenggelam di cakrawala."

    show a at left
    "Aria: 'Ada apa dengan matahari terbenam ini?'"

    show d at right
    "Dr. Hikari: 'Piramida Mesir adalah salah satu struktur kuno yang diatur dengan presisi astronomi. Matahari terbenam ini memberi petunjuk pada kalender kuno mereka. Kalian dapat belajar banyak tentang astronomi dan sistem penanggalan dari sini.'"

    "Bryan, teman sekelas Aria, yang tanpa sengaja ikut dalam petualangan ini, berkomentar, 'Benar-benar luar biasa! Tapi, ada apa di sini, Profesor?'"

    show d at right
    "Dr. Hikari: 'Menarik sekali! Bagaimana kita bisa belajar lebih lanjut?'"

    show d at right
    "Dr. Hikari: 'Mari kita turun ke dalam piramida ini. Di dalam, terdapat ruang khusus yang memuat pengetahuan mendalam tentang astronomi kuno Mesir. Ayo jelajahi bersama!'"

    "Seiring mereka masuk ke dalam piramida, suasana gelap berganti dengan sorotan lampu di sekitar mereka. Mereka mulai membaca hieroglif dan menemukan mekanisme kuno yang mengungkapkan rahasia astronomi Mesir."

    show a at left
    "Aria: 'Ini luar biasa, Profesor! Saya tidak pernah tahu seberapa maju pengetahuan mereka dalam astronomi.'"

    show b at center
    "Bryan: 'Sungguh menakjubkan! Ini benar-benar petualangan pengetahuan yang menyenangkan.'"

    show d at right
    "Dr. Hikari: 'Dan ini baru awalnya. Pintu Gerbang Alam Semesta masih membuka pintu ke destinasi-destinasi luar biasa lainnya. Siapkah kalian untuk terus menjelajahi dan memperdalam pengetahuan?'"

    "Ketiganya berpandangan dengan semangat, siap melangkah ke petualangan berikutnya."

    "Cerita ini mengajak pemain untuk menjelajahi pengetahuan melalui petualangan yang menarik dan edukatif di berbagai tempat bersejarah di seluruh dunia."

    return