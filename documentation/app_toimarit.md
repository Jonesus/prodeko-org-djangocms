===========================
app_toimarit Documentation
===========================

P�ivitetty: 13.11.2018


*********************************
Toimarien lis��minen
*********************************

- Jaostot on lis�tt�v� ensin manuaalisesti admin-paneelin kautta, mik�li niit� ei ole jo luotu
- CSV-tiedoston voi ladata admin --> Guild Officials/Toimihenkil�t --> Lataa CSV
- Vanhat toimarit eiv�t poistu CSV-tiedostoa ladatessa, joten tarvittaessa ne tulee poistaa ennen tiedoston lataamista
- Toimarien kuvat linkittyv�t automaattisesti oikeisiin henkil�ihin, kun ne ladataan kansioon prodekoorg/app_toimarit/static/images/toimari_photos
- Kuvien nime�misen tulee noudattaa muotoa Etunimi_Sukunimi.jpg 
- Oletuskuvaa voi vaihtaa samasta kansiosta tiedostosta anonyymi_uniseksi_maskulinoitu.jpg



*********************************
Hallituksen j�senten lis��minen
*********************************

- Manuaalisesti admin-paneelin kautta
- Toimarien kuvat linkittyv�t automaattisesti oikeisiin henkil�ihin, kun ne ladataan kansioon prodekoorg/app_toimarit/static/images/hallitus_photos
- Kuvien nime�misen tulee noudattaa muotoa Etunimi_Sukunimi.jpg 
- Oletuskuvaa voi vaihtaa samasta kansiosta tiedostosta placeholder.jpg

*********************************
Muut toiminnallisuudet
*********************************

-Admin-paneelista kaikki toimarit voi ladata omalle koneelle CSV-tiedostona valitsemalla kaikki toimarit ja valitsemalla "Export selected as CSV" vasemmasta yl�kulmasta.