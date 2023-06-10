import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from base.models import EarlyDiagnosisPatient


class Command(BaseCommand):
    help = "Populates the database with random generated data."

    def add_arguments(self, parser):
        parser.add_argument("--amount", type=int, help="The number of purchases that should be created.")

    def handle(self, *args, **options):
        names = ['Scarlett','Elizabeth','Emily','Chloe','Violet','Abigail','Hazel','Aizivaishe','Akatendeka','Anaishe','Anatswanashe','Anenyasha','Anesu','Danai','Fadziso',' Miriro','Mufaro','Ropafadzo','Rufaro','Akudzwe','Davidzo','Rudo']
        surname = ['Moyo','Ncube','Sibanda','Dube','Ndlovu','Ngwenya','Phiri','Nyoni','Tshuma','Mhlanga','Shumba','Shoko','Tembo','Hove','Maposa','Marufu','Makoni','Muyambo','Masuku','Chauke','Chuma','Takawira','Mpala','Muchenje','Sigauke','Mudzingwa','Taruvinga','Katsande']
        id_number = ['08- 1234567 D 53','01-1002000-A01','02-1012021-A02','03-1022042-C03','04-1032063-D04','05-1042084-E25','16-1052105-F26','27-1062126-G37','48-1072147-H28','19-1082168-I49','10-1092189-J10','11-1102210-K11','12-1112231-L12','13-1122252-M13','14-1132273-N14','15-1142294-O15','16-1152315-P16','17-1162336-Q17','18-1172357-R18','19-1182378-S19','20-1192399-T20','21-1202420-U21']
        sex = ['Male']
        address = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42']
        address_street = ['Nketa','Romney Park','Rujeko','Paddonhurst','Nketa','Lakeside','Emganwini','Lochview','Sauerstown', 'Parklands', 'Kingsdale','Barham Green','Barbour Fields','Ascot','Mucheke','West','Victoria Range','Rodhene','Zimre Park','Senga','Mkoba','Southdowns','Kopje','Mtapa','Woodlands','Nashville','Luveve','Mpopoma', 'Everest Way','Kuwadzana 3','Kuwadzana 1','Kuwadzana 2','Avondale','Budiriro','Chitungwiza',' Hatfield','Sam Levys Village','Selmont Gardens S Machel Ave','Baines Ave','Epworth','Glen View 1','Glen View 2','Glen View 3','Highfields','Avondale', 'Strathaven', 'Mount Pleasant', 'Belgravia', 'Bluff Hill','Glen Lorne', 'Chisipite', 'Gunhill', 'Hogerty Hill','Borrowdale Brooke',]
        address_town = ['Bulawayo','Harare','Mutare','Bindura','Chinhoyi','Mwenezi','Masvingo']
        contact = ['+263771112111','+263771113112','+263771114113','+263771115114','+263771116115','+263771117116','+263771118117','+263771119118','+263771120119','+263771121120','+263771122121','+263771123122','+263771124123','+263771125124','+263771126125','+263771127126','+263771128127','+263771129128','+263771130129','+263771131130','+263771132131','+263771133132','+263771134133','+263771135134','+263771136135','+263771137136','+263771138137','+263771139138','+263771140139','+263771141140','+263771142141','+263771143142','+263771144143','+263771145144','+263771146145','+263771147146','+263771148147','+263771149148','+263771150149','+263771151150','+263771152151','+263771153152','+263771154153','+263771155154','+263771156155','+263771157156','+263771158157','+263771159158','+263771160159','+263771161160','+263771162161','+263771163162','+263771164163','+263771165164','+263771166165','+263771167166','+263771168167','+263771169168','+263771170169','+263772171170','+263772172171','+263772173172','+263772174173','+263772175174']
        polyuria = ['Yes','No']
        polydipsia = ['Yes','No']
        sudden_weight_loss = ['Yes','No']
        weakness = ['Yes','No']
        polyphagia = ['Yes','No']
        genital_thrush = ['Yes','No']
        visual_blurring = ['Yes','No']
        itching = ['Yes','No']
        irritability = ['Yes','No']
        delayed_healing = ['Yes','No']
        partial_paresis = ['Yes','No']
        muscle_stifness = ['Yes','No']
        alopecia = ['Yes','No']
        obesity = ['Yes','No']
        age = ['39','17','57','20','59','88','61','93','74','50','36','25','39','16','26','80','60','49','80','31','41','30','60','22','75','74','49','77','91','62']
        height = ['1.37', '1.26', '1.34', '1.96', '1.7','1.51', '1.99',' 1.5', '1.66', '1.71', '1.59', '1.97', '1.68', '1.88', '1.96', '1.69',' 1.59', '1.64']
        mass = ['85','72','80','63','78','76','84','94','93','52','79','55','71','65','79','87','84','87','63','58','76','59','69','69','80','62','91','51','87','83','81','69','64','73','88','94','73','63','77','84','55','58','95','82','93','72','91','59','76','94','90','72','90','88','76','69','62','72','86','87']
        status = ['Positive','Negative']
     
        amount = options["amount"] if options["amount"] else 2500
        for i in range(0, amount):
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
            patients = EarlyDiagnosisPatient.objects.create(
                name=random.choice(names) + " " + random.choice(surname),
                id_number = random.choice(id_number),
                gender = random.choice(sex),
                address = random.choice(address) + "," + random.choice(address_street) + "," + random.choice(address_town),
                contact = random.choice(contact),
                polyuria = random.choice(polyuria),
                polydipsia = random.choice(polydipsia),
                polyphagia = random.choice(polyphagia),
                sudden_weight_loss = random.choice(sudden_weight_loss),
                weakness = random.choice(weakness),
                genital_thrush = random.choice(genital_thrush),
                visual_blurring = random.choice(visual_blurring),
                itching = random.choice(itching),
                irritability = random.choice(irritability),
                delayed_healing = random.choice(delayed_healing),
                partial_paresis = random.choice(partial_paresis),
                muscle_stiffness = random.choice(muscle_stifness),
                alopecia = random.choice(alopecia),
                obesity = random.choice(obesity),
                age = random.choice(age),
                height = random.choice(height),
                mass = random.choice(mass),
                status = random.choice(status)
            )
            patients.time = dt
            patients.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))