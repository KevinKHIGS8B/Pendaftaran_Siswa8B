from json import dump, load
from os import system

member = {}

fileSiswa = 'barang.json'


dataSiswa = {
	"nama" : "Kevin",
	"kelas" : "8.B",
	"laporan" : "Project Kelas 8"
}
def print_member():
	if len(member) > 0:
		for info in member:
			print(f'Nama \t: {info}\t Usia \t: {member[info]}')
	else:
		print('Gaada Siswa.')
class Data:

	def __init__(self, filename, documentTitle, heading):
		self.filename = filename
		self.documentTitle = documentTitle
		self.heading = heading
		self.info = """
		Kevin KH
		8.B
		"""

#str(dataSiswa['nama']+dataSiswa["kelas"]+".pdf")
myData = Data(str(dataSiswa['nama']+dataSiswa["kelas"]+".pdf"), "Hasil Ujian",dataSiswa['laporan'])
myPdf = canvas.Canvas(myData.filename)
myPdf.setTitle(myData.documentTitle)

#PRINT ON PAPER
#myPdf.drawString(300,770,myData.heading) #x,y,heading

myPdf.setFont("Helvetica", 30)
myPdf.setFillColorRGB(150,0,0)
myPdf.drawCentredString(300, 770,"Jumlah Siswa")
myPdf.line(30, 760, 560, 760)
#           x1  y1    x2   y2

myText = myPdf.beginText(40,680)
myText.setFont("Helvetica", 18)

Lines = ["Berikut Data Siswa", "-Bambang", "12"]

datajason = (f'Nama \t: {info}\t Usia \t: {member[info]}')


for line in Lines:
	myText.textLine(line)
myPdf.drawText(myText)


for line in datajason:
	myText2.textline(line)
myPdf.drawText(mytext2)


myPdf.drawInlineImage("sagu.jpg", 130, 400)


myPdf.save()

#print("ok")