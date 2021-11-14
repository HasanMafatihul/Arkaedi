label day_1:
    stop music
    scene bg black
    "Gedubrak!"
    "Suara buku-buku yang jatuh akibat tiupan angin musim gugur membangunkanku dari tidur yang amat nyenyak."
    mc "{cps=10}Hoaaaaaaaam…{/cps}"
    scene bg kamar mc berantakan
    with fade
    play music fantasy2 loop
    mc "Ah, aku lupa menutup jendelaku lagi..."
    mc "Sudah jam berapa ini?"

    "Aku mengusap mataku."
    mc "Sudah jam sembilan?!"
    mc "Berarti sarapan sudah selesai??"
    "Kruyuk"
    mc "Uhh… perutku…"
    mc "Sepertinya hari ini aku harus makan di luar lagi…"

    "Perlahan, aku berdiri."
    "Aku berjalan menuju gantungan baju, berhati-hati agar tidak menginjak kertas-kertas yang berserakan di lantai."
    mc "(Suatu saat nanti akan kurapikan…)."
    "Sesampainya disana, aku mengenakan mantel serta {i}top hat{/i}-ku."
    "Aku membuka pintu kamarku sebelum melangkah keluar."
    "Aku menutup pintu kamar di belakangku sebelum menguncinya."
    "Setelah memastikan pintu terkunci, aku bergegas menuju stasiun tram."

label courtyard:
    scene bg courtyard
    with fade
    "Aku memasuki halaman akademi."
    "Sembari berjalan menuju stasiun tram, aku memerhatikan patung gajah yang berdiri di tengah halaman."
    show rhea:
        xalign 1.5
        block:
            linear 0.5 xalign 0.5
    rhea "Ah! My Duke!"
    mc "(Kenapa aku harus bertemu Rhea di sini..)"
    rhea "Engkau mau kemana?{w=1} Ke kota?{w=1} Apakah Engkau sudah sarapan?{w=1} Jika belum, apakah Engkau berkenan untuk makan sarapan buatan hamba?"

    mc "Aku hanya mau mencari makan di luar, Rhea."
    rhea "Makan di luar? {w=1} Apa yang hendak orang kotor di kota mau sajikan ke Duke Yang Mulia?"
    mc "Makan di luar nggak bakal membunuhku, Rhea."
    rhea "Akan tetapi Duke Yang Mulia, Engkau tidak pantas untuk memakan makanan yang dibuat orang-orang biasa. Engkau terlalu tinggi untuk-"
    mc "Sudahlah."
    mc "Lagipula, bukankah kamu memiliki hal yang lebih penting untuk dilakukan selain berbincang denganku?"
    rhea "Ah!{w=1} Hamba lupa!{w=1} Hamba hendak mengirimkan dokumen ini ke kantor OSIS!"
    rhea "Sampai jumpa Duke!{w=1} Semoga kita bertemu lagi!"
    show rhea:
        xalign 0.5
        block:
            linear 1.0 xalign -0.5
    pause 1.5
    hide rhea

    mc "Anak itu selalu saja."
    mc "Huff.."

label tram_station:
    scene bg tram station
    with fade
    mc "Hmm…"
    "Aku menghentakkan kakiku di lantai peron sembari menunggu datangnya tram."
    "Tap. Tap. Tap."
    senpai "Dorian?"
    show senpai
    with Dissolve(.5)
    mc "Senpai?"
    senpai "Kamu mau kemana?"
    mc "Saya hendak ke restoran."
    mc "Saya belum sarapan."
    senpai "Bangun telat?"
    mc "Hehe."
    senpai "Kamu mau ke {i}The Flying Fisherman{/i}, kan?"
    mc "Memang kenapa?"
    senpai "Kebetulan tujuanku satu daerah di situ."
    mc "Kita menggunakan tram yang sama?"
    "Senpai mengangguk."
    "..."
    "Kami terdiam sejenak. Tiba-tiba, terdengar dari kejauhan suara tram bergerak diatas rel."
    play sound tram_jalan
    "Gruduk-gruduk-gruduk-gruduk-"
    "Akhirnya, tram sampai di stasiun"
    play sound tram_bel
    "Kring! Kring!"
    "Announcer" "Tram menuju Stasiun Waterfront akan segera berangkat."
    senpai "Ah, itu tram kita sudah datang."
    senpai "Ayo, kita masuk."
    "Kami berdua memasuki tram."
    hide senpai

label tram_main:
    show bg tram station
    with fade
    "Aku duduk di kursi dekat jendela."
    show senpai:
        xalign -0.5
        block:
            linear 0.5 xalign 0.25
    "Tidak lama kemudian, senpai duduk di sampingku."
    play sound tram_pintu
    "Setelah semua penumpang memasuki tram, pintu tram pun tertutup. Tram berjalan tidak lama setelah itu."
    play sound tram_jalan
    "Gruduk-gruduk-"
    play music tram_inside loop

menu tram_choice:
    "...":
        $ click()
        $tram = "senpai"
        jump tram_senpai
    "Wah, cuaca hari ini indah yah, senpai.":
        $ click()
        $tram = "mc"
        jump tram_mc

label tram_senpai:
    senpai "Hmm… Cuaca hari ini indah, iya kan?"
    mc "..."
    senpai "Pemandangan seperti ini memang bisa menyejukkan hati siapapun yang melihatnya."
    "Senpai benar, pemandangan distrik kampus di musim gugur memang indah."
    "Daun-daun merah-kecoklatan beterbangan ditiup angin yang kencang."
    show senpai
    pause 2.5
    jump tram_main_2

label tram_mc:
    mc "Wah, cuaca hari ini indah yah, senpai."
    senpai "Sangat indah."
    mc "(Duh, bagaimana ini jawabnya?)"
    mc "...{w=0.5} Iya."
    "..."
    senpai "Fufu~"
    mc "Senpai?"
    senpai "Kamu ternyata lucu juga."
    mc "Hah?"
    "Senpai tersenyum tipis."
    mc "Senpai, apa yang lucu dengan aku??"
    senpai "Lupakan saja."
    mc "Senpai!"
    jump tram_main_2

label tram_main_2:
    play sound tram_bel
    "Kring! Kring!"
    stop music
    scene bg tram station
    with fade
    "Announcer" "Kereta telah tiba di Stasiun Waterfront. Mohon berhati-hati ketika turun."
    senpai "Nah, kita sudah sampai."
    "Senpai keluar mendahuluiku."
    if tram == "mc":
        mc "{cps=*0.5}Senpai!!!{/cps}"
    pause 1.0

label kota:
    play music kota loop
    scene bg kota
    with fade
    "Seturunnya aku dari tram, beragam aroma dan suara memenuhi inderaku."
    "Dari sebelah kiri, terdengar suara ombak musim gugur menghantam tembok laut dengan ritme yang menghipnotis."
    "Dari sebelah kanan, tercium wangi rempah dan parfum dari bazaar."
    "Kruyuk kruyuk~"
    mc "(Ah, iya. Makan.)"
    "Aku segera bergegas menuju {i}The Flying Fisherman{/i}, restoran favoritku."

label restaurant:
    scene bg kota
    with fade
    "Aku melangkahkan kaki ke dalam restoran."
    mc "Hmm…"
    "Aroma sedap memenuhi inderaku."
    "Aku segera ke counter."
    mc "Hai, Randall!"
    pelayan "Yang Mulia Dorian!"
    pelayan "Pesanan seperti biasa?"
    mc "Seperti biasa."
    "Randall, si pelayan yang kukenal, mengacungkan jempol."
    "Aku duduk di salah satu kursi kosong di dekat jendela."
    "Sembari menunggu makanan, aku memandang keluar jendela, mataku terpaku pada mercusuar yang berdiri kokoh di tengah lautan yang kacau."
    "..."

    "???" "Shhhhh…"
    "Tiba-tiba, seseorang meniup telingaku."
    "Aku berbalik terkejut, tanganku siap untuk menghajar siapapun yang meniup telingaku."
    "Saat aku melihat siapa yang melakukannya, aku segera menurunkan tanganku."
    mc "Eloise?!"
    show eloise
    with Dissolve(1.0)
    eloise "Hehe."
    "Eloise Wyndham, sang Tuan Putri Kerajaan serta teman masa kecilku, berdiri di belakangku."
    mc "Kamu sedang apa di sini?"
    eloise "Sama seperti kamu."
    "Ia duduk di kursi sebelahku"
    mc "Kamu juga bangun kesiangan?"
    eloise "Lah kamu bangun kesiangan?"
    mc "Loh."
    "Eloise tertawa"
    mc "Ih, aku kira kamu juga bangun kesiangan."
    eloise "Yah, aku tidak akan melakukan hal tidak terpuji seperti itu."
    mc "Iya, iya, \"Tuan Putri\"."
    "Eloise hanya tertawa."
    "Sembari menunggu pelayan mengantarkan pesanan kami, kami berbincang-bincang tentang berbagai hal."
    "Ketika makanan sudah siap dihidangkan, kami makan dengan tenang."
    "Tiba-tiba, Randall datang membawa makananku."
    pelayan "Selamat menikmati, {i}Monsieur{/i}."
    pelayan "Oh? Apakah ada yang mungkin saya sajikan untuk nyonya cantik berbaju putih ini?"
    eloise "Hmm… secangkir kopi sepertinya enak."
    eloise "Ah, buat dua. Sepertinya Monsieur Sleepyhead juga butuh secangkir."
    pelayan "Baiklah. Mohon ditunggu!"
    "Aku menatap Eloise dengan kecewa. Ia tertawa kecil."
    eloise "Itu ikannya dingin lho lama-la-"
    mc "Nggak."
    "Aku segera melahap makananku."
    "Tidak lama kemudian, Randall kembali membawakan kopi kita."
    "Eloise segera minum dari cangkirnya."
    eloise "Ah, omong omong, habis ini kamu mau kemana?"

menu destination_choice:
    "Bazaar":
        $ click()
        mc "Bagaimana kalau kita ke bazaar? Ada beberapa hal yang harus kubeli."
        eloise "Baiklah. Kamu yang bayar belanjaan aku ya~"
        mc "(Ugh... Seandainya bukan putri kerajaan, mungkin sudah aku tampar dia.)"
        eloise "Bercanda~"
        "Kami menghabiskan makanan dan minuman kami."
        "Setelah membayar, kami bergegas menuju bazaar."

        jump bazaar_main
    "Taman Kota":
        $ click()
        mc "Bagaimana kalau ke taman kota?"
        eloise "Ide yang bagus"
        mc "Kamu mau ikut??"
        "Eloise menangguk"
        mc "Baik"
        "Kami beranjak keluar dan menuju taman kota"
        jump taman_kota_main
    "Tidak Ada Rencana":
        $ click()
        $temp = ["taman kota", "bazaar"]
        $destination = random.choice(temp)
        mc "Aku tidak ada rencana setelah ini"
        eloise "Bagaimana kalau kita ke [destination]?"
        mc "Hmmm..."
        mc "Ide yang bagus"
        eloise "Oke!"
        "Eloise meraih tanganku"
        eloise "Ayo, kita ke [destination]!"
        if destination == "bazaar":
            jump bazaar_main
        else:
            jump taman_kota_main

label bazaar_main:
    scene bg black
    with fade
    pause 1.5
    scene bg kota
    with fade
    pause 1.5
    show eloise
    "Kami tiba di bazaar"
    eloise "Hmmm!!"
    "Eloise berlarian ke sekeliling bazaar, membeli segala hal yang ia lihat"
    eloise "Lihat Dorian! Di sana ada yang jual daging bakar!"
    mc "Ah, iya."
    eloise "Lihat lihat! Ada penyanyi di sana!"
    mc "Wah, iya"
    "Tuan Putri Kerajaan memang terkenal anggun, tetapi bazaar seperti ini rupanya dapat menghilangkan segala keanggunannya…"
    "Meskipun begitu, ia terlihat senang."
    "Aku tersenyum tipis melihat teman masa kecilku berbahagia."
    mc "Hmm?"
    hide eloise
    with Dissolve(.5)
    "Di tengah-tengah lautan orang, aku dapat melihat satu wajah yang kukenal."
    "???" "Lihatlah! Pertunjukan sihir terhebat zaman ini!!"
    "Melewati sela-sela, aku bisa melihat jelas wajahnya."
    mc "(Maria?)"
    show maria at rightish with Dissolve(.5)
    "Gadis itu, Maria, terlihat kaget melihatku."
    "Dia dengan cepat kembali ke pertunjukannya seolah tidak melihatku."
    mc "(Apa yang sedang ia lakukan?)"
    "Pertanyaanku segera terjawab."
    "Maria melakukan pertunjukan sihir menggunakan berbagai sihir yang diajarkan di akademi."
    "Kombinasi sihir dan presentasi yang menarik membuat banyak orang berkerumun untuk melihatnya."
    "Aku merasakan Eloise menepuk bahuku."
    show eloise at leftish with Dissolve(.5)
    eloise "Itu si Maria, kan?"
    mc "Iya."
    eloise "Dia sedang apa?"
    mc "Kayaknya dia sedang melakukan pertunjukan sihir."
    eloise "Pertunjukan sihir?"
    "Eloise bergerak maju, mencoba melihat Maria dengan lebih jelas."
    eloise "Waah."
    "Eloise terlihat terpesona dengan pertunjukan Maria."
    " < Beberapa menit kemudian > "
    "Pertunjukan Maria telah selesai."
    maria "Terimakasih! {w=0.5} Terimakasih semua!!"
    "Penonton telah bubar, meninggalkan hanya aku, Eloise, dan Maria."
    "Maria melambaikan tangan ke kami, mengajak kami mendekat."
    maria "Senpai sedang apa di sini?"

menu bazaar_choice_1:
    "Jalan-jalan Biasa":
        $ click()
        mc "Kami hanya sedang jalan-jalan biasa."
        maria "Begitukah?"
        "Aku dan Eloise mengangguk bersamaan."
    "Pacaran":
        $ click()
        mc "Kami sedang pacaran."
        "Eloise & Maria" "Hah??"
        maria "Kalian berdua pacaran??"
        eloise "NGGAK!!"
        "Wajah Eloise terlihat memerah."
        mc "Tapi kenyataannya-"
        "Eloise mendorong-dorong tubuhku, jelas terlihat malu."
        eloise "Udah kamu diam saja, Dorian!!"
        mc "Hehe~"
        maria "Ternyata kalian beneran pacaran..."
        eloise "Nggak!!!"
        "Aku tertawa dalam hati."
        mc "Nggak, nggak, Maria. Aku hanya bercanda."
        "Eloise terlihat sangat memerah."
        eloise "IH KAMU ITU!!"
        "Maria tertawa kecil."
        maria "Sudah, sudah."
    "(biarkan eloise menjawab)":
        $ click()
        eloise "Kita cuman jalan-jalan aja kok."
        eloise "Di sini kan memang tempat untuk jalan-jalan santai."
        maria "Ohh…"
        "Maria tidak menanyakan lebih lanjut."

label bazaar_main_2:
    "Kami berbincang sejenak, membicarakan pertunjukan Maria tadi."
    "Tanpa sadar, matahari sudah mulai tenggelam."
    maria "Wah, sepertinya aku harus segera pulang. Ayahku pasti sudah menunggu."
    maria "Sampai jumpa di sekolah, senpai!"
    eloise "Sampai jumpa, Maria!"
    hide maria with Dissolve(.5)
    show eloise
    eloise "Kalau begitu, aku pulang juga deh. {i}Au revoir{/i}~!"
    hide eloise with Dissolve(.5)
    "Pada akhirnya, hanya aku yang tersisa."
    "Aku bersegera menuju stasiun tram, tidak ingin terlambat kembali ke asrama."
    jump go_home

label taman_kota_main:
    scene bg black
    with fade
    pause 1.5
    scene bg kota
    with fade
    pause 1.5
    show eloise
    "Kami tiba di taman kota."
    eloise "Wah…"
    "Pemandangan di tempat ini sangat indah."
    "Burung-burung beterbangan, orang-orang berjalanan, serta berbagai tumbuhan yang memenuhinya."
    "Beberapa orang terlihat melakukan pertunjukan jalanan."
    "Eloise terlihat tertarik."
    mc "Hmm?"
    "Salah satu perempuan yang melakukan pertunjukan terlihat familiar.."
    show maria at rightish with Dissolve(.5)
    show eloise at leftish with Dissolve(.5)
    eloise "Ada apa Dorian?"
    mc "Kamu kenal si penampil itu?"
    "Eloise melihat ke arah yang kutunjuk."
    eloise "Itu… bukannya Maria?"
    eloise "Itu Maria kan?"
    "Kami mendekati penampil itu."
    mc "Iya itu Maria."
    "Maria terlihat hendak melakukan pertunjukan."
    maria "Lihatlah! Pertunjukan sihir terhebat di zaman ini!"
    "Maria mulai melakukan pertunjukan menggunakan sihir yang diajarkan di akademi"
    eloise "Waah."
    "Eloise terlihat terpesona dengan pertunjukan Maria."
    "Kombinasi sihir dan presentasi yang menarik membuat banyak orang berkerumun untuk melihatnya."
    " < Beberapa menit kemudian > "
    "Pertunjukan Maria telah selesai"
    maria "Terimakasih! {w=0.5} Terimakasih semua!!"
    "Penonton telah bubar, meninggalkan hanya aku, Eloise, dan Maria"
    "Maria melambaikan tangan ke kami, mengajak kami mendekat"
    maria "Senpai sedang apa di sini?"

menu taman_kota_choice_1:
    "Jalan-jalan Biasa":
        $ click()
        mc "Kami hanya sedang jalan-jalan biasa"
        maria "Begitukah?"
        "Aku dan Eloise mengangguk bersamaan"
    "Pacaran":
        $ click()
        mc "Kami sedang pacaran"
        "Eloise & Maria" "Hah??"
        maria "Kalian berdua pacaran??"
        eloise "NGGAK!!"
        "Wajah Eloise terlihat memerah"
        mc "Tapi kenyataannya-"
        "Eloise mendorong-dorong tubuhku, jelas terlihat malu"
        eloise "Udah kamu diam saja, Dorian!!"
        mc "Hehe~"
        maria "Ternyata kalian beneran pacaran..."
        eloise "Nggak!!!"
        "Aku tertawa dalam hati"
        mc "Nggak, nggak, Maria. Aku hanya bercanda"
        "Eloise terlihat sangat memerah"
        eloise "IH KAMU ITU!!"
        "Maria tertawa kecil"
        maria "Sudah, sudah"
    "(biarkan eloise menjawab)":
        $ click()
        eloise "Kita cuman jalan-jalan aja kok"
        eloise "Di sini kan memang tempat untuk jalan-jalan santai"
        maria "Ohh…"
        "Maria tidak menanyakan lebih lanjut"

label taman_kota_2:
    "Kami berbincang sejenak, membicarakan pertunjukan Maria tadi"
    "Tanpa sadar, matahari sudah mulai tenggelam."

    mc "Sampai jumpa!"
    maria "Sampai jumpa di sekolah, senpai!"
    eloise "Semoga kita bertemu lagi"
    "Kami bertiga berpisah ke tujuan masing-masing"
    "Eloise kembali ke istananya, Maria dengan urusan pribadinya, dan aku yang ingin segera kembali ke asrama"
    "Aku bersegera ke stasiun tram, tidak ingin terlambat kembali ke asrama"
    jump go_home

label go_home:
    play music pulang loop
    scene bg tram station with fade
    "..."
    "Announcer" "Tram menuju Stasiun Akademi akan segera berangkat."
    "Aku memasuki tram."
    "Aku menduduki kursi di dekat jendela. Tidak lama kemudian, tram mulai berjalan."
    play sound tram_jalan
    "Gruduk-gruduk-gruduk-"
    "Sembari melihat keluar jendela, aku memikirkan tugasku yang menumpuk."
    mc "(Hadeh…)"
    scene bg black with Dissolve(1.0)
    "..."
    scene bg tram station with Dissolve(1.0)
    play sound tram_bel
    "Kring! Kring!"
    "Announcer" "Tram telah tiba di Stasiun Akademi. Mohon berhati-hati ketika turun."
    "Tanpa sadar, aku telah tiba di Akademi."
    "Aku segera turun dari tram."

    scene bg courtyard
    with fade
    "Tap. Tap. Tap."
    "???" "Dorian?"
    show runa
    with Dissolve(.5)
    mc "Runa-senpai?"
    runa "Kamu habis ngapain di luar?"

menu go_home_choice_senpai:
    "Jalan-jalan":
        $ click()
        mc "Aku habis jalan-jalan di luar."
        runa "Oh, iya kah?"
        "Aku mengangguk."
        runa "Yah, hari ini libur sih."
        runa "Tapi tumben kamu keluar."
        mc "..."
        "Runa-senpai hanya mengangguk-angguk."
    "Cari Makan":
        $ click()
        mc "Aku baru saja mencari makan diluar."
        runa "Mencari makan sampai sore?"
        mc "Ya, kan mumpung di luar."
        "Runa-senpai terlihat curiga, tapi tidak bertanya lebih lanjut."

label go_home_2:
    mc "Senpai sendiri mau kemana?"
    runa "Ah, ini?"
    "Runa-senpai menunjukkan dokumen-dokumen yang dibawanya."
    runa "Aku hendak ke ruang OSIS."
    mc "Ketua OSIS sangat sibuk yah."
    "Runa-senpai terlihat bangga."
    runa "OSIS kan memang memiliki banyak kewajiban."
    runa "Hal ini sudah biasa."
    runa "Ah, aku harus segera ke ruang OSIS."
    runa "Sampai jumpa!"
    mc "Sampai jumpa, Runa-senpai!"
    hide runa
    with Dissolve(.5)
    "Runa senpai pergi."
    "Aku segera melanjutkan perjalananku ke kamarku."
    "..."

label the_letter:
    stop music
    scene bg kamar mc
    with fade
    "Aku akhirnya sampai di kamar."
    "Aku memasukkan kunci ke lubangnya sebelum memutarnya."
    "Klik."
    "Setelah kunci terbuka, aku mendorong pintu sebelum melangkah ke dalam."
    "Aku menutup pintu dibelakangku."
    mc "Haaah…"
    mc "(Hari ini sangat melelahkan…)"
    mc "Aahhh"
    "Aku menjatuhkan diri ke kasur"
    "Kresek."
    mc "Hmm?"
    "Selembar amplop menarik perhatianku"
    show obj amplop with Dissolve(1.0):
        xalign 0.5 yalign 2.0
        block:
            linear 1.0 yalign 0.5
    mc "Apa ini?"
    mc "Amplop? Bukankah pintunya tadi terkunci?"
    "Aku membuka amplop itu"
    "Selembar surat jatuh di tanganku"
    call letter_inside from _call_letter_inside
    hide obj amplop with Dissolve(1.0)
    mc "Apa ini?"
    mc "C?"
    mc "Ah, sudahlah."
    mc "Tidak perlu aku pikirkan sekarang."
    "Aku berbaring di ranjang."
    mc "(C...)"
    show bg black
    with Dissolve(2.0)
    "..."
    "{cps=10}{b}TO BE CONTINUED{/b}{/cps}"
    return

label letter_inside:
    "\"Teruntuk Dorian Auguinaire, Duke of Krysafen,"
    "\"Kemampuan serta potensi Anda telah menarik kami."
    "\"Oleh karena itu, kami secara formal mengundang Anda untuk bergabung dengan kami."
    "\"Besok, datanglah ke air mancur di taman kota."
    "\"Di sana, Anda akan diberikan petunjuk berikutnya."
    "\"Salam, C\""



    return
