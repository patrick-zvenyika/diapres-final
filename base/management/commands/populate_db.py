import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from base.models import PatientData


class Command(BaseCommand):
    help = "Populates the database with random generated data."

    def add_arguments(self, parser):
        parser.add_argument("--amount", type=int, help="The number of purchases that should be created.")

    def handle(self, *args, **options):
        names = ['Scarlett','Elizabeth','Emily','Chloe','Violet','Abigail','Hazel','Aizivaishe','Akatendeka','Anaishe','Anatswanashe','Anenyasha','Anesu','Danai','Fadziso',' Miriro','Mufaro','Ropafadzo','Rufaro','Akudzwe','Davidzo','Rudo']
        surname = ['Moyo','Ncube','Sibanda','Dube','Ndlovu','Ngwenya','Phiri','Nyoni','Tshuma','Mhlanga','Shumba','Shoko','Tembo','Hove','Maposa','Marufu','Makoni','Muyambo','Masuku','Chauke','Chuma','Takawira','Mpala','Muchenje','Sigauke','Mudzingwa','Taruvinga','Katsande']
        id_number = ['08- 1234567 D 53','01-1002000-A01','02-1012021-A02','03-1022042-C03','04-1032063-D04','05-1042084-E25','16-1052105-F26','27-1062126-G37','48-1072147-H28','19-1082168-I49','10-1092189-J10','11-1102210-K11','12-1112231-L12','13-1122252-M13','14-1132273-N14','15-1142294-O15','16-1152315-P16','17-1162336-Q17','18-1172357-R18','19-1182378-S19','20-1192399-T20','21-1202420-U21']
        sex = ['Female']
        address = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42']
        address_street = ['Nketa','Romney Park','Rujeko','Paddonhurst','Nketa','Lakeside','Emganwini','Lochview','Sauerstown', 'Parklands', 'Kingsdale','Barham Green','Barbour Fields','Ascot','Mucheke','West','Victoria Range','Rodhene','Zimre Park','Senga','Mkoba','Southdowns','Kopje','Mtapa','Woodlands','Nashville','Luveve','Mpopoma', 'Everest Way','Kuwadzana 3','Kuwadzana 1','Kuwadzana 2','Avondale','Budiriro','Chitungwiza',' Hatfield','Sam Levys Village','Selmont Gardens S Machel Ave','Baines Ave','Epworth','Glen View 1','Glen View 2','Glen View 3','Highfields','Avondale', 'Strathaven', 'Mount Pleasant', 'Belgravia', 'Bluff Hill','Glen Lorne', 'Chisipite', 'Gunhill', 'Hogerty Hill','Borrowdale Brooke',]
        address_town = ['Bulawayo','Harare','Mutare','Bindura','Chinhoyi','Mwenezi','Masvingo']
        contact = ['+263771112111','+263771113112','+263771114113','+263771115114','+263771116115','+263771117116','+263771118117','+263771119118','+263771120119','+263771121120','+263771122121','+263771123122','+263771124123','+263771125124','+263771126125','+263771127126','+263771128127','+263771129128','+263771130129','+263771131130','+263771132131','+263771133132','+263771134133','+263771135134','+263771136135','+263771137136','+263771138137','+263771139138','+263771140139','+263771141140','+263771142141','+263771143142','+263771144143','+263771145144','+263771146145','+263771147146','+263771148147','+263771149148','+263771150149','+263771151150','+263771152151','+263771153152','+263771154153','+263771155154','+263771156155','+263771157156','+263771158157','+263771159158','+263771160159','+263771161160','+263771162161','+263771163162','+263771164163','+263771165164','+263771166165','+263771167166','+263771168167','+263771169168','+263771170169','+263772171170','+263772172171','+263772173172','+263772174173','+263772175174']
        pregnancies = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
        glucose_level = ['110.76', '113.04', '120.51', '120.57', '75.7', '74.11', '93.54', '60.21', '87.57', '61.99', '110.04', '60.57', '106.17', '134.38', '60.39', '83.99', '70.01', '136.71', '138.76', '118.31','65.59', '64.76', '87.96', '114.68', '126.68', '74.42', '120.2', '57.69', '108.66', '106.56', '75.62', '96.67', '87.45', '71.07', '138.98', '80.73', '78.87', '121.32', '102.85', '59.09']
        blood_pressure = ['80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','139','140']
        skin_thickness = ['9.3', '8.44', '12.99', '17.55', '15.57', '17.63', '5.38', '16.86', '15.79', '13.57', '12.33', '11.21', '11.25', '13.89', '14.01', '6.52', '11.29', '11.63', '12.39', '17.26']
        insulin = ['15', '9', '12', '10', '9', '10', '15', '13', '9', '10', '9', '8', '14', '11', '13', '11', '8', '11', '13', '15']
        BMI = ['22.17', '21.76', '21.13', '22.6', '24.06', '22.74', '22.77', '21.97', '23.92', '23.14','25.83', '29.77', '29.14', '28.43', '27.0', '25.13', '26.52', '27.83', '28.83', '26.03','39.56', '39.74', '30.7', '36.15', '34.66', '30.45', '31.67', '30.93', '32.53', '37.74']
        dpf = ['0.19', '0.38', '0.61', '0.18', '0.31', '0.11', '0.41', '0.33', '0.11', '0.25','0.74', '0.36', '0.18', '0.44', '0.6', '0.37', '0.5', '0.43', '0.52', '0.35','0.34', '0.61', '0.44', '0.72', '0.66', '0.53', '0.26', '0.24', '0.2', '0.48']
        age = ['39','17','57','20','59','88','61','93','74','50','36','25','39','16','26','80','60','49','80','31','41','30','60','22','75','74','49','77','91','62']
        height = ['1.37', '1.26', '1.34', '1.96', '1.7','1.51', '1.99',' 1.5', '1.66', '1.71', '1.59', '1.97', '1.68', '1.88', '1.96', '1.69',' 1.59', '1.64']
        mass = ['85','72','80','63','78','76','84','94','93','52','79','55','71','65','79','87','84','87','63','58','76','59','69','69','80','62','91','51','87','83','81','69','64','73','88','94','73','63','77','84','55','58','95','82','93','72','91','59','76','94','90','72','90','88','76','69','62','72','86','87']
        status = ['Positive','Negative']
     
        amount = options["amount"] if options["amount"] else 2500
        for i in range(0, amount):
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
            patients = PatientData.objects.create(
                name=random.choice(names) + " " + random.choice(surname),
                id_number = random.choice(id_number),
                sex = random.choice(sex),
                address = random.choice(address) + "," + random.choice(address_street) + "," + random.choice(address_town),
                contact = random.choice(contact),
                pregnancies = random.choice(pregnancies),
                glucose_level = random.choice(glucose_level),
                blood_pressure = random.choice(blood_pressure),
                skin_thickness = random.choice(skin_thickness),
                insulin = random.choice(insulin),
                BMI = random.choice(BMI),
                Diabetes_Pedigree_Function = random.choice(dpf),
                age = random.choice(age),
                height = random.choice(height),
                mass = random.choice(mass),
                status = random.choice(status)
            )
            patients.time = dt
            patients.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))