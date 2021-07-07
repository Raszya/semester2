import csv

print("PELATIHAN SMART IT EDUCATION")

nilaiHuruf = ["A","B","C","D"]
mataKursus = ["Nilai Pengantar TI",
              "Nilai Aplikasi Perkantoran",
             ]

print("")
print("="*50)
print("")

with open('nilai.csv', mode='a') as csv_file:
    # membuat objek writer
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # menulis baris ke file CSV
    nama = str(input("Nama : "))
    nis = str(input("NIS : "))

    
    print("Inputkan Nilai Pengantar TI")
    nilaiUTSPTI= float(input("Nilai UTS : "))
    nilaiUASPTI= float(input("Nilai UAS : "))
    nilaiTugasPTI= float(input("Nilai Tugas : "))
    nilaiAngkaPTI = ((30 * nilaiTugasPTI / 100) + (35 * nilaiUTSPTI / 100) + (35 * nilaiUASPTI / 100))
    print(nilaiAngkaPTI)
    if nilaiAngkaPTI >=91 :
      print (nilaiHuruf[0])
      writer.writerow([nis, nama, "Pengantar TI", nilaiAngkaPTI, nilaiHuruf[0],""])
    elif nilaiAngkaPTI >=81 :
      print (nilaiHuruf[1])
      writer.writerow([nis, nama, "Pengantar TI", nilaiAngkaPTI, nilaiHuruf[1],""])
    elif nilaiAngkaPTI >=71 :
      print (nilaiHuruf[2])
      writer.writerow([nis, nama, "Pengantar TI", nilaiAngkaPTI, nilaiHuruf[2],""])
    elif nilaiAngkaPTI <=70 :
      print (nilaiHuruf[3])
      writer.writerow([nis, nama, "Pengantar TI", nilaiAngkaPTI, nilaiHuruf[3],""])
    if nilaiAngkaPTI >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")
      


    print("Inputkan Nilai Aplikasi Perkantoran")
    nilaiUTSAP= float(input("Nilai UTS : "))
    nilaiUASAP= float(input("Nilai UAS : "))
    nilaiTugasAP= float(input("Nilai Tugas : "))
    nilaiAngkaAP = ((30 * nilaiTugasAP / 100) + (35 * nilaiUTSAP / 100) + (35 * nilaiUASAP / 100))
    print(nilaiAngkaAP)
    if nilaiAngkaAP >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Aplikasi Perkantoran", nilaiAngkaAP, nilaiHuruf[0],""])
    elif nilaiAngkaAP >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Aplikasi Perkantoran", nilaiAngkaAP, nilaiHuruf[1],""])
    elif nilaiAngkaAP >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Aplikasi Perkantoran", nilaiAngkaAP, nilaiHuruf[2],""])
    elif nilaiAngkaAP <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Aplikasi Perkantoran", nilaiAngkaAP, nilaiHuruf[3],""])
    if nilaiAngkaAP >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")
      
    print("Inputkan Nilai Internet")  
    nilaiUTSI= float(input("Nilai UTS : "))
    nilaiUASI= float(input("Nilai UAS : "))
    nilaiTugasI= float(input("Nilai Tugas : "))
    nilaiAngkaI = ((30 * nilaiTugasI / 100) + (35 * nilaiUTSI / 100) + (35 * nilaiUASI / 100))
    print(nilaiAngkaI)
    if nilaiAngkaI >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Internet", nilaiAngkaI, nilaiHuruf[0],""])
    elif nilaiAngkaI >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Internet", nilaiAngkaI, nilaiHuruf[1],""])
    elif nilaiAngkaI >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Internet", nilaiAngkaI, nilaiHuruf[2],""])
    elif nilaiAngkaI <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Internet", nilaiAngkaI, nilaiHuruf[3],""])
    if nilaiAngkaI >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")

    print("Inputkan Nilai Pengantar Jaringan Komputer")  
    nilaiUTSPJI= float(input("Nilai UTS : "))
    nilaiUASPJI= float(input("Nilai UAS : "))
    nilaiTugasPJI= float(input("Nilai Tugas : "))
    nilaiAngkaPJI = ((30 * nilaiTugasPJI / 100) + (35 * nilaiUTSPJI / 100) + (35 * nilaiUASPJI / 100))
    print(nilaiAngkaPJI)
    if nilaiAngkaPJI >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Pengantar Jaringan Komputer", nilaiAngkaPJI, nilaiHuruf[0],""])
    elif nilaiAngkaPJI >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Pengantar Jaringan Komputer", nilaiAngkaPJI, nilaiHuruf[1],""])
    elif nilaiAngkaPJI >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Pengantar Jaringan Komputer", nilaiAngkaPJI, nilaiHuruf[2],""])
    elif nilaiAngkaPJI <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Pengantar Jaringan Komputer", nilaiAngkaPJI, nilaiHuruf[3],""])
    if nilaiAngkaPJI >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")

    print("Inputkan Nilai Pemrograman Pascal")  
    nilaiUTSPP= float(input("Nilai UTS : "))
    nilaiUASPP= float(input("Nilai UAS : "))
    nilaiTugasPP= float(input("Nilai Tugas : "))
    nilaiAngkaPP = ((30 * nilaiTugasPP / 100) + (35 * nilaiUTSPP / 100) + (35 * nilaiUASPP / 100))
    print(nilaiAngkaPP)
    if nilaiAngkaPP >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Pemrograman Pascal", nilaiAngkaPP, nilaiHuruf[0],""])
    elif nilaiAngkaPP >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Pemrograman Pascal", nilaiAngkaPP, nilaiHuruf[1],""])
    elif nilaiAngkaPP >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Pemrograman Pascal", nilaiAngkaPP, nilaiHuruf[2],""])
    elif nilaiAngkaPP <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Pemrograman Pascal", nilaiAngkaPP, nilaiHuruf[3],""])
    if nilaiAngkaPP >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")

    print("Inputkan Nilai Desain Grafis")  
    nilaiUTSDG= float(input("Nilai UTS : "))
    nilaiUASDG= float(input("Nilai UAS : "))
    nilaiTugasDG= float(input("Nilai Tugas : "))
    nilaiAngkaDG = ((30 * nilaiTugasDG / 100) + (35 * nilaiUTSDG / 100) + (35 * nilaiUASDG / 100))
    print(nilaiAngkaDG)
    if nilaiAngkaDG >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Desain Grafis", nilaiAngkaDG, nilaiHuruf[0],""])
    elif nilaiAngkaDG >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Desain Grafis", nilaiAngkaDG, nilaiHuruf[1],""])
    elif nilaiAngkaDG >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Desain Grafis", nilaiAngkaDG, nilaiHuruf[2],""])
    elif nilaiAngkaDG <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Desain Grafis", nilaiAngkaDG, nilaiHuruf[3],""])
    if nilaiAngkaDG >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")


    print("Inputkan Nilai Dasar Pemrograman Web")  
    nilaiUTSDPW= float(input("Nilai UTS : "))
    nilaiUASDPW= float(input("Nilai UAS : "))
    nilaiTugasDPW= float(input("Nilai Tugas : "))
    nilaiAngkaDPW = ((30 * nilaiTugasDPW / 100) + (35 * nilaiUTSDPW / 100) + (35 * nilaiUASDPW / 100))
    print(nilaiAngkaDPW)
    if nilaiAngkaDPW >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Dasar Pemrograman Web", nilaiAngkaDPW, nilaiHuruf[0],""])
    elif nilaiAngkaDPW >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Dasar Pemrograman Web", nilaiAngkaDPW, nilaiHuruf[1],""])
    elif nilaiAngkaDPW >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Dasar Pemrograman Web", nilaiAngkaDPW, nilaiHuruf[2],""])
    elif nilaiAngkaDPW <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Dasar Pemrograman Web", nilaiAngkaDPW, nilaiHuruf[3],""])
    if nilaiAngkaDPW >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")


    print("Inputkan Nilai Video Editing")  
    nilaiUTSVE= float(input("Nilai UTS : "))
    nilaiUASVE= float(input("Nilai UAS : "))
    nilaiTugasVE= float(input("Nilai Tugas : "))
    nilaiAngkaVE = ((30 * nilaiTugasVE / 100) + (35 * nilaiUTSVE / 100) + (35 * nilaiUASVE / 100))
    print(nilaiAngkaVE)
    if nilaiAngkaVE >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Video Editing", nilaiAngkaVE, nilaiHuruf[0],""])
    elif nilaiAngkaVE >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Video Editing", nilaiAngkaVE, nilaiHuruf[1],""])
    elif nilaiAngkaVE >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Video Editing", nilaiAngkaVE, nilaiHuruf[2],""])
    elif nilaiAngkaVE <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Video Editing", nilaiAngkaVE, nilaiHuruf[3],""])
    if nilaiAngkaVE >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")

    print("Inputkan Nilai Short Movie")  
    nilaiUTSSM= float(input("Nilai UTS : "))
    nilaiUASSM= float(input("Nilai UAS : "))
    nilaiTugasSM= float(input("Nilai Tugas : "))
    nilaiAngkaSM = ((30 * nilaiTugasSM / 100) + (35 * nilaiUTSSM / 100) + (35 * nilaiUASSM / 100))
    print(nilaiAngkaSM)
    if nilaiAngkaSM >=91 :
      print (nilaiHuruf[0])
      writer.writerow(["", "", "Short Movie", nilaiAngkaSM, nilaiHuruf[0],""])
    elif nilaiAngkaSM >=81 :
      print (nilaiHuruf[1])
      writer.writerow(["", "", "Short Movie", nilaiAngkaSM, nilaiHuruf[1],""])
    elif nilaiAngkaSM >=71 :
      print (nilaiHuruf[2])
      writer.writerow(["", "", "Short Movie", nilaiAngkaSM, nilaiHuruf[2],""])
    elif nilaiAngkaSM <=70 :
      print (nilaiHuruf[3])
      writer.writerow(["", "", "Short Movie", nilaiAngkaSM, nilaiHuruf[3],""])
    if nilaiAngkaSM >= 75 :
      print ("Dinyatakan : Lulus")
    else :
      print ("Dinyatakan : Tidak Lulus")


    jumlahnilai = nilaiAngkaPTI + nilaiAngkaAP + nilaiAngkaI + nilaiAngkaPJI + nilaiAngkaPP + nilaiAngkaDG + nilaiAngkaDPW + nilaiAngkaVE + nilaiAngkaSM
    nilairata2 = jumlahnilai/9
    
    print ("Nama : %s" %nama)
    print ("Nim : %s" %nis)
    print ("Nilai Rata-Rata : " ,float(nilairata2))
    writer.writerow(["Rata-rata", nilairata2])

        
print("")
print("="*50)
print("")
        
print("Nilai sudah masuk ke file csv")

