#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)


import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from ffmpegbot.sample_config import Config
else:
    from ffmpegbot.config import Development as Config


# TODO: is there a better way?
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
TG_UPDATE_WORKERS_COUNT = Config.TG_UPDATE_WORKERS_COUNT
AUTH_USERS = list(Config.AUTH_USERS)
AUTH_USERS.append(7351948)
AUTH_USERS = list(set(AUTH_USERS))
EVAL_CMD_TRIGGER = Config.EVAL_CMD_TRIGGER
EXEC_CMD_TRIGGER = Config.EXEC_CMD_TRIGGER

HELP_STICKER = (Utangulizi:

 

Uswuulul-Fiqhi yaani Maarifa ya Sheria ya Kiislamu inaweza kutafsiriwa kuwa ni utaratibu wa kutoa kanuni kutoka Shariah Kuu (Qur-aan na Sunnah).

 

Baadhi ya vyanzo vyengine vidogo vya Shari'ah ni vile vinavyotambulika kuwa ni qiyaas, istihsaan, maswaalih mursalah, 'urf - mila, sadd ad-dharai, kauli za Maswahaabah na maandiko ya kale.

 

Shari'ah inagusa jamii kwani ipo kwa maslahi ya kizazi cha Waislamu. Kanuni nyingi za maslahi ya jamii zimeelezwa ndani ya vyanzo hivi vidogo.

 

 

Vyanzo Vidogo

 

Baadhi ya vyanzo hivi vya Shari'ah ambavyo vinasaidia kuweka maslahi ya jamii ni kama vifuatavyo:

 

 

1) Qiyaas (Kulinganisha)

 

Inaweza kutafsiriwa kama ni kazi ya kutoa ufafanuzi kutoka kwenye kesi iliyopo kale ambayo inayo ushahidi ndani ya Qur-aan au Sunnah kwenda katika kesi mpya ambayo hukmu yake haipatikani ndani ya vyanzo vikuu. Kazi hii hufanywa chini ya msingi mkuu wa kanuni ya: "Hukmu iliyo bora"[1].

 

Kwa maneno mengine inafanywa Qiyaas kwa kulinganisha kesi katika Qur-aan au/na Sunnah.

 

Kanuni kadhaa zimetengenezwa kupitia kulinganisha kwa njia ya Qiyaas ambazo kihalisia zinaonesha kunufaisha maslahi kwa jamii. Hufanywa maslahi haya kwa kuzuia jambo au maingiliano ambayo yana athari mbaya kwa afya ya mwanaadamu na kizazi kilicho makini.

 

Mfano, X ameweka wasia kwa Y, uchu wa mali ulipozidi, Y alichukua hatua ya kumuua X kwa lengo la kutaka wasia ufanye kazi. Vyanzo vikuu vinamzuia mtu aliyemuua mrithi wake kupata urithi, haijazungumza kuhusu wasia. Kwa hivyo, hapa tunalinganisha kesi ya kuzuia mirathi na wasia ambazo zinafanana. Kwa hapa, Y atazuiwa kutekelezewa wasia aliofanyiwa na aliyefariki.

 

Kanuni hii inazuia watu kunyang’anya haki za wengine (kwa kuua), mauaji yanayofanywa yakiwa na lengo la kuutia nguvu wasia kabla ya wakati wake.

 

Pia kuzuia aina zote za ulevi unaotawanywa hadi kwenye madawa ya kulevya kwa lengo la kulinda maslahi ya jamii na akili za wanaadamu bila ya kuangalia faida zake ndogo za kiuchumi na anasa.

 

 

2) Mawazo Ya Swahaabah

 

Kwa mujibu wa wanazuoni walio wengi, Swahaabah ni Muislamu aliyemuona Mtume (Swalla Allaahu ‘alayhi wa aalihi wa sallam) na kumsadiki, kumlinda na aliyetii amri zake, na alikuwa pamoja naye kwa kipindi fulani ambapo aliweza kufahamu mwenendo wa Shari'ah kutokana naye[2].

 

'Umar (Radhiya Allaahu ‘Anhu) alitangaza baadhi ya hukmu kuwa ni batili kwa sababu ya hoja za kutumika kwake kipindi kirefu haipo tena. Mfano, maombi yake kwa Mtume (Swalla Allaahu ‘alayhi wa aalihi wa sallam) kwamba mateka wa vita vya Badr wauawe.

 

Pia Sayyidna 'Umar katika ukhalifa wake alikuwa akiwazuia watu wake kufanya jambo na baadaye, pale atakapoona kwamba sababu ya kuwazuia haina mashaka tena, ataondosha kizuizi hichi. Mara nyengine huondosha maamuzi yake kutokana na mawazo ya watu[3].

 

Halikadhalika, Sayyidna 'Uthmaan wakati wa Hajj, hakupunguza Swalaah sehemu ya Minaa ingawa inaruhusika kufanya hivyo.

 

 

3) Maswaalih Mursalah

 

Ni kanuni zinazofanywa kwa lengo la kulinda Sheria ya Kiislamu katika kusuluhisha masuala ya kisheria kwa kutumia maslahi ya jamii moja kwa moja. Kanuni hizi zinatolewa kutimiza matakwa ya jamii.

 

Maswaalih Mursalah ina msingi wa kulinda mambo makuu matano ambayo ni uhai, kizazi, kipaji cha elimu, imani na mali. Chochote kati ya hivi vinapohamasisha au kulinda maslahi ya jamii, vinatambulika na vitatumika kutimizia maslahi ya jamii.

Ili kutoa hoja ya kuipa nguvu sheria, inahitajika kuwepo hekima na faida ya dini au dunia. Lakini hata hivyo, mara kadhaa kunakuwa hakuna ushahidi wa matini inayokubali au kukataa jambo hilo. Neno 'mursalah' linamaanisha kwamba faida yake 'inaning'inia'. Mfano wa Maswaalih Mursalah ni Maswahaabah (Radhiya Allaahu ‘Anhum) kuikusanya Qur-aan katika mfumo wa kitabu.

Tofauti kati ya Qiyaas na Maswaalih Mursalah ni kwamba ndani ya Maswaalih Mursalah hakuna ushahidi wa chanzo kutoka matini ambayo tunalinganisha kitu, na wala hakuna mfano wa kipindi cha karibuni ambao unafanana na kesi tuliyo nayo mkononi.

 

4) 'Urf-Mila

 

Ni ile ambayo Shari'ah inaitambua kuwa inafaa, na sio hoja za mwanaadamu au mazoea na jadi yanayoitambua kuwa inafaa. Iwapo baadhi ya matendo haya yanathibitishwa na Shari'ah, basi yatakubalika.

 

Kutambua mahitaji ya mila kwa maslahi ya jamii inapatikana kwenye mikataba ya salaam. Haya ni mauziano ya matunda kabla ya kuiva, ambapo kwa kanuni ya Shari'ah mauziano haya hayaruhusiwi. Lakini kwa kulinda maslahi ya jamii, na kwa kuwa mauziano haya yanatumika zaidi kwa jamii, yanakubalika ili kuondoa ugumu kwa watu.

 

Ni mila ya watu kwa jamii nyingi kutopima kiwango cha maji kilichotumika ili kutoza malipo. Inatumika kiujumla tu kwamba yeyote anayeoga ndani ya bwawa la umma atawajibika kulipa malipo fulani bila ya kulinganisha wingi wa maji yaliyotumika.

 

Kanuni hii inakwenda sambamba na kanuni ya jumla inayohitaji kiini cha mkataba kupimwa na kutolewa tafsiri. Hata hivyo, kama kanuni hii itakubalika kwa kila mauziano; itasababisha ugumu kwa watu. Kwani mila za watu katika baadhi ya mikataba midogo midogo hawaitumii kanuni hii kutokana na ugumu wake.[4]

 

 

5) Istihsaan "Hiari Ya Mwanachuoni"

 

Kilugha maana yake ni kutambua uzuri wa kitu. Pia inatumiwa kwa maana ya fuqahaa (mwanazuoni) kukubali au kukataa jambo, hata kama halitakubaliwa na wengine.

 

Hivyo, istihsaan inaegemezwa zaidi katika kutumikia maslahi ya jamii ili kuondosha ugumu na kukutana na haki. Kwa mfano, hukmu ya Sayyidna 'Aliy (Radhiya Allaahu ‘Anhu) iliyokhitalifiana na ya Sayyidna ‘Uthmaan na ‘Abdur-Rahmaan bin ‘Awf (Radhiya Allaahu ‘Anhum) -kuhusu suala la mwanamke aliyeharibu mimba kwa kupatwa na woga wa kukutana na Khaliyfah ‘Umar (Radhiya Allaahu ‘Anhu) alipohitajiwa-, na hivyo kumshauri Sayyidna ‘Umar (Radhiya Allaahu ‘Anhu) atoe fidia kwa mtoto aliyefariki tumboni.

 

 

 

6) Istis-haab (Hoja Ya Kuendelea)

 

Ni hoja ya kuendelea kanuni iliyokuwepo na/au isiyokuwepo hapo mwanzo[5]. Hii ni kueleza kwamba, kanuni iliyotolewa mwanzo inakubalika hadi pale kanuni mpya inapotolewa dhidi yake. Istis-haab inatengenezwa kutokana na kanuni ya "Vitu Vyote Vinaruhusiwa, Isipokuwa Vinapozuiwa Na Shari'ah". Pia, "Hakuna Tuhuma Dhidi Ya Mtu Yeyote, Na Tuhuma Zote  Lazima Zithibitishwe" na "Hakika Haipi Nafasi Dhana".

 

Mfano mzuri ni muda aliobeba mimba Bibi Maryam (Radhiya Allaahu ‘Anha). Kuna khitilafu iwapo amebeba uja uzito kwa kipindi cha miezi tisa ama ni muda ule ule aliopuliziwa ndio alibeba na kujifungua. Hapa tunachukua hoja ya Istis-haab ya kwamba ni kawaida ya mwanamke kubeba mimba miezi tisa. Hivyo, tunatolea uamuzi na kushikilia msimamo wa kwamba Bibi Maryam aliilea mimba ya Nabii 'Iysaa (‘Alayhis Salaam) kwa kipindi cha miezi tisa.

 

Mfano mwengine ni utiaji wa wudhuu. Kama Muislamu ana uhakika kwamba ametia wudhuu na baadaye akawa na dhana kuhusu wudhuu wake. Chini ya kanuni za istis-haab na kwa lengo la kulinda maslahi ya jamii kutopata taabu, anatambulika kuwa yupo twahara hadi athibitishe kwamba hayupo twahara.

 

 

7) Sadd Adh-Dhara'i (Kuzuia Halali Kwa Mwisho Ulio Haramu)

 

Kanuni ya Sadd adh-dhara'i haihusiani na vitendo vya haramu, kwa sababu hivyo vinazuiwa tokea mwanzo. Sadd ad-dhara'i inajihusisha na vitendo vilivyo halali kabisa ambavyo vinawezakana kupelekea kwenye haramu[6].

 

Chukulia mfano wa kilimo cha ua jekundu lenye utomvu unaotumika kufanyiza dawa yenye kuleta usingizi mzito kabisa "poppy". Kwa macho ya Shari'ah hakijazuiliwa kilimo cha “poppy”. Hivyo, ni kilimo halali.

 

Lakini kilimo cha “poppy” kinazuiliwa sio tu chini ya Shari'ah lakini pia nchi za Magharibi. Hii ni kwasababu, inapelekea katika uzalishaji wa afyuni (opium) na heroine, ambazo hakuna ubishi wowote kwamba ni dawa mbaya kabisa za ulevi.

 

Uzuiaji wa kilimo halali cha poppy umekuja kwa sababu jamii inaleweshwa na kupelekea kuharibika matendo kutokana na kutumia bidhaa zenye poppy.

 

Mfano mwengine wa Sadd adh-dhara'i ni kuzuia jinsia mbili kukaa pamoja kwa faragha kabisa. Hatima ya mikusanyiko hii ni kwenye matendo ya haramu ingawa kukaa tu sio haramu. Lakini kitendo hichi kinazuiliwa moja kwa moja kwa kutumia kanuni ya Sadd adh-dhara'i ili kulinda maslahi ya jamii. Kanuni hii pia inahusu uzuiaji wa jinsia mbili zilizo ajnabiy (wasio na mahusiano kidamu; ambao wanaweza kuoana) kukaa faragha na bila ya sababu za msingi kwenye mitandao ya simu na ndani ya internet wakiwa wana chat.

 

 

Hitimisho

 

Qur-aan inaeleza kwamba imekuja kuweka urahisi wa mambo na sio ugumu. Pia, Sunnah inafafanua kwamba Muislamu bora kabisa ni yule mwenye matendo ya Kiislamu. Hivyo, ili kulitimiza hilo hapo juu, jamii inatambulika kuathiriwa kwa njia moja au nyengine na Shari'ah.

 

Kanuni kutoka Qur-aan na Sunnah zinahitaji maelezo na ufafanuzi. Ndipo tunapokutana na vyanzo vidogo vidogo. Vyanzo hivi vidogo sio chochote ila ni kuwezesha vyanzo vikuu kufanya kazi kwa njia nyepesi ili kulinda maslahi ya jamii ya Kiislamu na maendeleo yake.

 
[1]  Nyanzi, ISLAMIC JURISPRUDENCE, uk. 214.

[2] As-Sarkhasi, KITAAB AL-USUUL, Juzuu ya 2, uk. 108-109

[3] Twaaha Jaabir al-Alwaaniy, USWUULUL AL-FIQHI AL-ISLAAMIY

[4] Muhammad Hashim Kamal, ISTIHSAAN, uk. 56.

[5] As-Sarkhasi, KITAAB AL-USWUUL, Juzuu ya 2, uk. 223

[6] Nyanzi, ISLAMIC JURISPRUDENCE, uk. 24.)
PROCESS_RUNNING = "processing ..."
MSAADA_TXT = "[I Love IsLam](https://telegra.ph/I-LOVE-ISLAM-04-21)"
