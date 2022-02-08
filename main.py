from building import Kikoto, varosfal
from tkinter import *
import time
import tkinter as tk
import os
import json
print(varosfal[0].level)

path = os.path.dirname(os.path.abspath(__file__))

buildings = {
    "akademia": "Az akadémia egy fenséges hely tele tudásanyaggal\n a régi tradíciók és az új technológiák összegzésével.\n A legbölcsebb agyak a városban várják a bebocsájtást! Vedd figyelembe hogy minden tudósnak \nszüksége lesz laboratóriumra, ami pénzbe kerül. \nMinél nagyobb az akadémia, \nannál több tudóst alkalmazhatsz egyszerre.",
    "barakk": "A barakkokban nyüzsgő fiatalokat képeznek ki elmés\n harcosokká. A katonáid tudják majd\n, hogy bánjanak a karddal, lándzsával és katapulttal,\n és képesek lesznek elvezetni a legnagyobb háborús eszközöket\n a csatamezőn. A katonák képzése gyorsabb, ha nagyobb a barakk.",
    "acsmester": "Csak a legjobb minőségű fa kerül felhasználásra az ácsmester\n műhelyében. Ennek köszönhetően az ügyes mesterünk tartós\n szerkezeteket tud összeállítani és a házakat nem kell majd\n javítani folyton. Az ácsmester műhelyének minden\n egyes szintje csökkenti az építőanyag szükségletet 1%-kal.",
    "raktar": "A készleteid egy része a raktárépületben van. \nEz kívül tartja a fosztogatókat, esőt és más kellemetlenségeket. \nA raktárépület gondnoka pedig pontosan tudja hogy mi van itt tárolva.\n A raktárépület fejlesztésével több készletet tudsz itt tárolni.",
    "piac": "Árusok és kereskedők bonyolítják az üzleteket a kereskedő\n poszton. Alkut kötnek, üzletelnek. \nA messziről jött kereskedők inkább mennek a nagy és jól ismert kereskedő posztokba!\n A hatóköre és kapacitása a kereskedő posztodnak növekszik minden második fejlesztés után.",
    "fogado": "Egy nehéz napi munka után nincs jobb mint egy pohár hideg bor. Pont emiatt szeretnek a lakosaid a fogadóban összejönni. És miután az utolsó jó régi dalok is el lettek dalolva (szellemes mi? :P) a nap végén, vidáman hazamennek pihenni. Minden szinttel több bort szolgáltathatsz fel a fogadóban.",
    "palota": "A palota egy nagyszerű hely ahhoz, hogy a birodalmadat \nvezesd a jövő felé! Ezen kívül gyönyörű\n a kilátás a tengerre. \nA palota minden fejlesztése egy új telep létrehozását teszi lehetővé.",
    "rejtekhely": "Egy bölcs vezető rajta tartja a szemét\n a szövetségesein és az ellenségein is. \nA rejtekhelyen kémeket bérelhetsz fel, \nakik információval látnak el téged más városokból. \nNagyobb rejtekhelyből több kémet bérelhetsz.",
    "erdeszhaz": "Az erős favágók még a legnagyobb fákat is kivágják. \nDe az erdészek tudják hogy az erdőket újra kell telepíteni,\n a fákat újra kell ültetni ahhoz hogy a házainkat folyamatosan jó minőségű fából építhessük.\n A fatermelés 2%-kal nő épület szintenként.",
    "bortermelo": "A bortermelő csak a legalkalmasabb domboldalakat választja ki a szőlő termesztéséhez. \nÍgy a szőlőkertek minőségi gyümölcsökkel tudnak szolgálni a szüret idején.\n Minden szint után nő a bortermelés 2%-kal",
    "nagykovetseg": "A Nagykövetség egy elfoglalt hely: \ndiplomaták érkeznek ide a világ minden tájáról egyezségekről tárgyalni, \negyezményeket kötni és szövetségeket alapítani. Ahhoz, hogy nagyobb szövetséged legyen, fejlesztened kell \na Nagykövetségedet. A Nagykövetség minden egyes szintje növeli a diplomácia pontjaidat.",
    "templom": "A templom a hit és a becsület palotája. \nPapok élnek itt, imádkoznak az Istenhez és terjesztik az igét a szigeten. \nItt imádkozhatsz csodákért is, persze csak ha elég tiszteletet mutatsz feléjük.",
    "epitesz": "Szög, kerület és mérőrúd: Az építész irodája \nbiztos tervekkel lát el minket hogy a házak falai egyenesebbek, és a tetők stabilabbak legyenek. \nTovábbá egy jól megtervezett házhoz kevesebb márványt használunk el. \nÉpület fejlesztési szintenként a márvány szükséglet a városban 1%-kal csökken.",
    "muhely": "A legképzettebb emberek dolgoznak a műhelyben. \nFejlesztik a katonák és hajók felszerelését az újabbnál újabb találmányaikkal. \nÉs egyre erősebbek lehetnek ezek! A műhely szintjének emelésével egyre \ntöbb fejlesztés lesz elérhető a katonák és a hajók számára.",
    "muzeum": "A múzeumban a lakosok szemlélhetik, hogy más népek hogyan \npróbálják másolni a kultúránkat. Ha nagyobb kiállítást akarsz, fejlesztened kell a múzeumot. \nA múzeum minden egyes szintje után egy új kulturális terméket tudsz bemutatni.",
    "tuzszeresz": "A folyamatos kísérletezés a robbanószerekkel \nnem csak az eget világítja meg de néha a környező épületeket is. \nA kutatóink a kísérletezésekkel tökéletesítve a robbanóanyagokat, csökkenthetik a kén szükségleteket. \nMinden épület szint fejlesztés után 1%-kal kevesebb a kén szükséglet a városban.",
    "optikus": "A lencsék a tudósoknak nem csak a tisztánlátásban, \nhanem a minket büszkévé tevő új találmányok megszületésében is \nsegítenek. Az optikusok minden ilyen eszközt gondosan dobozokban tárolnak, így azok nem tűnnek \nolyan könnyen el. A kristály szükséglet épület szintenként 1%-kal csökken.",
    "szolopres": "Csakis a legjobb borok érlelődnek városunk hűvös pincéiben. \nA borászmester pedig biztosra megy, hogy egy csepp bor se ússzon el, \nés az összes bor legördüljön a lakosaink torkán. Minden szint után \n1%-kal csökken a bor szükséglet."
}

hajo_fejlesztes = {"acsmesterseg": "A szigetünk zöld erdőiben található fák nagyon masszívak,\n erősek, ezért elbírják a házak tetőzetét. De hogy ez így legyen, \na gerendákat nagy hozzáértéssel kell kiválasztani és kezelni. \nEgy ács a városban mindezt tudja felügyelni, így kevesebb építőanyagot kell használnunk.",
                   "fegyverek": "Egy forgó szerkezet a csatahajóinkon, \namire egy nagy fegyver van erősítve! Kezdésnek a feltalálóink egy\n nagy számszeríjszerű fegyvert szereltek rá. \nDe úgy gondoljuk, hogy a szerkezet elbír majd nagyobb gépezeteket is. \nTehát amint a kutatóinknak támad egy megvalósítható ötlete ezzel kapcsolatban, fejleszthetünk tovább.",
                   "kalozkodas": "Az nagy Kalóz erőd erős legénységével csak az utasításaidra vár. Arany és nyersanyag fosztására rendezkedtek be. Hírnév és hatalmas források várják a legsikeresebb kalózokat.",
                   "hajokarbantartas": "Ha a hajóinkat mindig szépen és tisztán tartjuk, nem kell annyiszor javítani őket. Ez a tengerészeink morálját is megemeli, így ahelyett hogy a hajót takarítanák és a ruháikat mosnák, vidáman dalolnak majd.",
                   "merules": "A tudósaink rájöttek arra, hogy ha kevesebb árut szállítunk, kisebb lesz a vízellenállás. Ez azt jelenti, hogy nagyobb vitorlákat tudunk az árbócrúdra szerelni, így gyorsabban lehet utazni.",
                   "terjeszkedes": "Odakint nem csak az óceán van! Más szigetek várják, hogy felfedezzük őket. Nem vagyunk egyedül! Akár földet is szerezhetünk egy újonnan felfedezett szigeten, és megismerhetünk más népeket! A hivatalnokaink pedig alig várják, hogy többet adminisztrálhassanak, kereskedőink készek az új földekre elhajózni!",
                   "idegenkultura": "Ha megismerünk más népeket, az segíthet minket a fejlődésben. Normális beszélgetések és kedves szavak csodákat tesznek, új szövetségekhez és barátságokhoz vezethethetnek. Természetesen szükség lesz egy elegáns épületre a nagyköveteknek és a lakomáknak, amiket az ő tiszteletükre fogunk tartani!",
                   "szurok": "Ez valami nehéz és kellemetlen szagú folyadék, amit a tudósok találtak! De mióta a hajóinkra kenjük, kevesebb gond van velük!",
                   "piac": "A legkülönösebb cikkek érkeznek messzi szigetekről a piacra. Itt üzletelhetünk a kereskedőkkel, így szerezhetünk megfelelő nyersanyagokat is.",
                   "gorogtuz": "A tűz, amit nem olt el a víz! Ezzel a titkos keverékkel felégethetjük az ellenséges hajókat! Így meghódíthatjuk a tengereket olyan hajókkal, amik úgy okádják a tüzet, mint egy sárkány!",
                   "ellensuly": "A kutatóink megerősítették a nagyobb fegyverek hozzáépítését a hajóinkhoz, így nem esnek szét, ha az ellenségre lövünk velük. Ennek köszönhetően az ellensúly a katapultot a hajón tartja, így az nem fogja magát kilőni a hajóról.",
                   "diplomacia": "Az egyik filozófusunk bölcs gondolatokat írt le a háborúról és békéről. Azt tanácsolja, hogy kössünk egyezséget más népekkel, így talán könnyebben legyőzhetjük az ellenségeinket!",
                   "tengerterkepek": "Az utazások sokkal biztonságosabbá válnának, ha lejegyezzük, hogy merre vannak a zátonyok! Így a tengerészeink nem fognak tartani a víz alatti szikláktól, vagy a szirének hívogató dalától.",
                   "lapatkerekes": "Nagyszerű hír tengerészeinknek: a gőz hajtotta lapátkerék lehetővé teszi, hogy hajóink sokkal gyorsabban haladhassanak, mint evezőkkel bármikor. Az új gőz hajtotta lapátkerekek félelmet keltenek ellenségeinkben.",
                   "tomorites": "Ezzel a technológiával mérnökeink képesek lezárni a hajóinkon keletkező lékeket, sérüléseket. A művelet elég bonyolult, de megadja flottánk esélyét arra, hogy két támadás között a sérüléseket kijavíthassuk.",
                   "hajuagyu": "Ez az ágyú olyan hatalmas, hogy még Herkules sem tudná megmozdítani. Csak egy erős gőzhajó tudja ezeket, és azokat a nehéz golyókat szállítani , amiket az ellenségre lőnek.",
                   "nehezkos": "A legveszélyesebb tengeri egységek építhetők a kossal. A mérnöki találékonység eme mesterműve a hajó orr-részére szerelhető, és más hajókban hatalmas károk okozására képes.",
                   "tengeribazis": "Ezzel a fejlesztéssel a legnagyobb hajót tudjuk hajógyárunkban legyártani. A hajó léghajókat szállít, amik bombákkal harcolnak a nyílt tengeren.",
                   "hajozasjovoje": "Az óceánok titkai végre a mienk! A hajóink egyre ellenállóbbak és erősebbek! Szinte nincs más hajó, amely a mieinkkel versenyezhetne."
                   }

gazdasag_fejlesztes = {
    "megorzes": "Védhetjük és tárolhatjuk a nyersanyagainkat hosszabb időn át. Így a nyersanyagaink egy része biztonságban marad a fosztogató kalózoktól és ellenségektől!",
    "emelocsiga": "Egy nagyszerű ötlet: egy kötél, melyet egy kerékre feszítve húznak, egy embernek Herkules erejét adja. Tehát a munkásaink egymaguk mostmár hatalmas köveket mozgathatnak meg és így gyorsabban épülnek az épületek!",
    "vagyon": "A föld tele van értékes kincsekkel! Megtanultuk, hogyan bányászhatunk ként, kristályt és hogyan fejthetünk márványt.Szintén elsajátítottuk a szőlőtermelést, így most nagy szőlő ültetvényeink vannak a dombokon! A jólét egy új korszaka köszönt ránk, amikor elkezdjük hasznosítani ezeket a javakat. El is adhatjuk ezeket a kincseket a kereskedelmi poszton, vagy megvehetjük az idegen kereskedőktől azt, amire éppen szükségünk van.",
    "szolokultura": "A boldog lakosságunknak szüksége van fesztiválokra, ahol órákat eltölthetnek énekelve és iszogatva. Dionysos szereti nézni, ahogy élvezzük az ajándékát!",
    "fejlesztett": "Jó idő eltelt már azóta, hogy megtanultuk a szigetünk kincseit használni a saját szükségletünkre. Most a dolgozókat kellene tanítani, és minden bányát egy tapasztalt és erős ember irányítása alá helyezni. Ezzel még nagyobb termelést érhetünk el, és a civilizációnk gazdagabb lesz mint valaha!",
    "geometria": "Megfelelő szögek, háromszögek, körök – néhány éles elme elég ahhoz, hogy kiszámolják, hogyan építsük az épületeinket szebbre és jobbra. Így a városunk hamar példaként áll a világ előtt!",
    "epiteszet": "Egy jó ház ellent tud állni a legerősebb természeti elemeknek is. Viszont még ellenállóbbá lehet tenni, ha egy bölcs elme foglalkozik vele még a megépítés előtt, sok rajzolással és kis matematikával. Így a falak egyenesek és a tető feszes tud lenni. A vonalzónak és a körzőnek köszönhetően még stabilabbak lesznek és védettek az esőtől. Egy építész irodájával jól járnánk, csak gondolj a megtakarításra, amit egy új épület építésekor nyerhetünk!",
    "szabadsag": "Egy pihent munkásnak talán sokkal több kedve lehet dolgozni, mint egy kimerültnek. Ezért minden lakosnak lehetne hetente egy szabadnapja. Ez sokkal boldogabbá teheti őket!",
    "torvenyhozas": "Úgy gondoljuk, jó lenne írásba foglalni a közösségi élet szabályait. Ez azt jelenti hogy minden szigetlakó megnézheti mit szabad és mit nem - így nem lenne több kifogás!",
    "gasztronomia": "A kultúránk gazdag a különleges ízekben! Ha a szakácsaink csatlakoznak a katonáinkhoz a csatában, az illat is elég lesz ahhoz, hogy emlékeztesse őket az itthoni konyhára, ezzel erősödik a harci szellemük. És azt sem feledhetjük el hogy egy jóízű lakoma mindig talpra állítja az embert. És persze a szakácsnak van egy éles kése, amivel beszállhat a küzdelembe.",
    "segitokezek": "Ha a lakosaink segítenének kicsit a föld alatt, és nem a parton lopnák a napot, akkor talán több nyersanyagot bányásznának ahelyett, hogy leégnének a napon. Segítségre mindig van szükség a bányákban, fafeldolgozókban és a szőlőföldeken.",
    "vizszint": "A víz mindig egyenletes. Ugyanezt a gondolatot kéne felhasználnunk az épületeknél is, így azok is egyenletesebbek lesznek! A városaink szebbek lesznek, és kevesebb fát és követ kell felhasználnunk hozzájuk!",
    "szolopres": "Micsoda esemény! Az egész falu ott van a szőlőtaposó ünnepen, amikor folyékony arany lesz belőle! Egy préssel, amelyet egy tapasztalt bortermelő kezel, sokkal hatékonyabban tudnánk ezt megtenni, és kevesebb bor veszne kárba. A bortermelő a borokat szép rendben tartja, így a bor a kellő ideig tud érni, hogy a legfinomabb legyen!",
    "nyersanyag": "Ahogy a raktárak nem tudják kezelni az egyre több nyersanyagot, szükségessé válik egy hosszú távú alternatíva. A lezárt ponyvák fejlett módszere lehetővé teszi számunkra nagy mennyiségú nyersanyag szabad ég alatti tárolását.",
    "katonacsere": "Fényes páncéljukban feszítő harcedzett katonáink és precíz harci gépeink híre legendás. Eljött az idő, hogy profitot termeljenek nekünk. A szigetvilág más vezetői sorban állnak majd egységeinkért.",
    "burokracia": "A palotánkban már rengeteg polc, doboz, szekrény és még több kupac irat van, még a legjobb írnok sem látná ezt át. Építhetnénk ennek egy külön épületet, ahol adminisztrálhatjuk és nyilvántarthatjuk ezeket! A megnövekedett adminisztráció és a folyó ügyek aprólékos dokumentálása miatt a továbbiakban nem tudunk észrevétlenül árukat mozgatni elfoglalt városainkból/városainkba, mert a város elfoglalója is értesül minden ottani lépésünkről.",
    "utopia": "A lakosaink jólétben és fényűzően élnek. Egészségesek és boldogak, és nem sok aggódnivalójuk van. Igen tulajdonképpen mondhatni, hogy olyan helyen élnek melyeket csak filozófusok írtak le, idillikus világként.",
    "gazdasagjovoje": "A lakosaink fényűzésben élnek, és a piacterünk tele van finomságokkal a világ minden tájáról! Az utcák tiszták és fejlettek, így az építőanyag könnyebben eljut az építési területre."
}

tudomany_fejlesztes = {
    "kutasas": "Heuréka! Egy kút a településünkben! Most már nem kell várnunk az esőt. A lakosainknak ez nagy segítséget jelent hiszen akkor öntözik majd a földjeiket, amikor csak jónak látják!",
    "papir": "Találtunk módot arra, hogy hogyan jegyezzük le tudásunkat! Most már írásainkat a papirusz növényből előállított papírra jegyezhetjük, így már nem lesz szükség azokra a nehéz kőtáblákra!",
    "kemkedes": "Ha a lakosaink közül néhányan letelepednek más városokban, segíthetnek nekünk figyelni a szomszédainkat. Ezáltal informálva lehetünk arról hogy a szomszédaink milyen felfedezéseket tesznek vagy hogy mennyi nyersanyaguk van.",
    "politeizmus": "Az ember nem tud mindent ép ésszel megmagyarázni. Amikor nem képes magyarázatot találni, a választ az isteneknél keresi. Az istenek az emberekhez hasonlóak kinézetben, de ugyanakkor különböznek is. Hiszen, mi más magyarázata lehetne a megmagyarázhatatlannak?",
    "tinta": "A természet megadja a lehetőséget az írásra: A madarak a tollukat, a tintahalak a tengerekből pedig fekete tintát adnak! Így sokkal egyszerűbbé válik az írás!",
    "kormanyalapitas": "Sokáig gondolkodtunk azon, hogy a kormányunk jobban is működhetne, ha egy kicsit máshogy csinálnánk. Sok munkával járna és biztosan lenne költsége is, de jó lenne ha egy ilyen kormányunk lenne.",
    "feltalalas": "Néhány incidens történt mostanság a lőporral és egyéb anyagokkal kapcsolatban. Ezért felállítunk egy saját műhelyt az összes kíváncsi tudósnak, így a robbanások nem fogják zavarni az akadémiai munkát. Erősebb falai is vannak ennek az épületnek, és nem ég le olyan könnyen.",
    "kulturaliscsereuzlet": "A lakosaink igazán szentelhetnének némi figyelmet más népek kulturális alkotásainak. Ezzel talán azok a népek cserébe kiállítanák a mi nagyszerű műalkotásainkat a múzeumaikban.",
    "anatomia": "Sokat tanultunk az emberi testről! Most már küldhetünk felcsereket a csatába, hogy segíthessenek a sebesült katonáknak, hogy azok mielőbb a talpukra álljanak. Természetesen belekeverhetnek az orvosságokba néhány hatóanyagot, például néhány felcser ismerhet olyan keveréket, ami bátrabbá teszi a katonáinkat.",
    "fenytan": "Miközben a tudósaink új dolgokat fedeznek fel, nagyon sok kristály eltörhet. Vagy elveszik a laborokban, a tisztaság ugyanis nem a legjellemzőbb rájuk. Ha egy optikus figyelne a minőségre, és a kristályokat mindig visszatenné a helyükre, akkor sokkal kevesebb kristályra lenne szükségünk!",
    "kisérletek": "A tudósaink szeretnék tesztelni az elméleteiket a gyakorlatban. Ezek a próbák minden bizonnyal gyorsítanák a kutatások idejét, de ez nem jelenti azt, hogy további laboratóriumi felszerelésre van szükség.",
    "mechanikustoll": "Milyen nagyszerű ötlet: egy ügyes feltaláló megtanított egy gépet írni. Most már könnyedén lemásolhatjuk a jegyzeteinket, és így az akadémiák is gyorsabban cserélhetnek információt!",
    "madarrepules": "Felfedeztük, hogy hogyan repüljünk úgy, mint a madár! Építhetünk olyan gépet, ami egy embert az égbe emel és lélegzetelállító sebességgel süvít el majd az ellenség feje fölött, miközben nyilakat lő rájuk.",
    "archivalas": "Archiválhatjuk féltve őrzött tengeri térképeinket. Ez lehetővé teszi tengerészeinknek, hogy mindig megtalálhassák a térképet, és időt takarítsanak meg az utazáskor.",
    "levelcsuszda": "Egy csoda: tekercseket küldhetünk csöveken keresztül nagy sebességgel, így azok hamarabb jutnak a tudósokhoz! Ezzel mi is kevesebb aranyat fizetünk majd a tudósaink után!",
    "allamvallas": "Nincs szükségünk világi törvényekre - a vallásiak bőven elegek. És ha már itt tartunk: nincs szükségünk civil szolgákra.",
    "nyomaskamra": "Feltaláltuk a hajót, ami a víz alatt is tud úszni anélkül, hogy elsüllyedne! Az óceán a miénk! Egy ellenség sem fog észrevenni minket, ahogy a víz alól süllyesztjük el a hajóit!",
    "archimedeszielv": "Megalkottuk a gépet, ami repül! Most már az ég sem akadály! Felengedhetünk hatalmas léggömböket az ellenségeink feje fölé, ahonnan tűzesőt is ereszthetünk rájuk!",
    "tudomanyjovoje": "A legeszesebb emberek dolgoznak azon, hogy megválaszoljanak egy nagy kérdést: Miért vagyunk itt? Miért vannak úgy a dolgok ahogy vannak? Ezzel közelebb kerülünk a megvilágosodáshoz"
}

hadugy_fejlesztes = {
    "szarazdokk": "Egy medence közel a parthoz, ahonnan a vizet leengedhetjük, hogy könnyebb legyen hajókat építeni és vízre helyezni őket Egy hatalmas flotta épül majd, mely megtanítja az ellenséget a félelemre!",
    "terkepek": "Ezek miatt a hosszú menetelések miatt a hegyeken és mocsarakon keresztül, a készleteink gyorsan kifogynak. Ha leírjuk a katonáinknak az útvonalat, hogy merre kerüljék ki az ilyen természetes akadályokat, végül mi jutunk ki ebből némi megtakarítással.",
    "professzionalissereg": "A kalózok és barbárok elkergetése sokkal könnyebb lesz, ha elit katonáink vannak! Ez talán drágább lesz mint a lakosainkat kiképezni háború idején, de cserébe a katonáink sokkal jobb képzést kapnak, és jobban forgatják majd a kardot, lándzsát és pajzsot!",
    "ostrom": "Egy faltörő kost terveztünk, ami fémből készül, és kb. 10 ember ereje kell a mozgatásához. Most már könnyebb lesz a katonáinknak elfoglalni más városokat!",
    "becsuletkodex": "A katonáink büszkék arra, hogy az egységükben szolgálhatják a szigetbirodalmat! Mostmár az egyenruháikkal is jobban bánnak, így nekünk kevesebbet kell azokon javítani.",
    "ballisztika": "Már nyilakat tudunk lőni az ellenségeinkre. Azonnal el kell kezdenünk kiképezni a katonáinkat erre, így mihamarabb íjászok is lesznek a seregünkben!",
    "erokartorvenye": "Ezzel a technológiával olyan erőt fejthetünk ki, amivel hatalmas köveket is repíthetünk a levegőbe! És ha a kövek elég nagyok, falakat rombolhatnak le!",
    "helytarto": "Ha civil hivatalnokokat is kiküldünk, nemcsak kifoszthatunk más városokat, de irányíthatjuk is őket. Seregeinkkel képesek leszünk idegen városokat megszállni, és onnan indíthatunk akciókat, hogy növeljük a gazdagságot és a jólétet.",
    "pirotechnika": "A kén az ördög műve! Minden egyes új keverékkel új hatásait ismerjük meg. Egy biztonságos gyakorlóhely jó lenne az újdonságok kipróbálására, így sokkal kevesebb kár keletkezne a környezetben és nem utolsósorban sokkal kevesebb kénre lenne szükség.",
    "logisztika": "A katonáink sokkal jobban tudnak harcolni, ha kevesebb teher van rajtuk. És a felszerelésük is tovább kitart a hosszú menetelések során, így nekünk ezzel is kevesebbet kell foglalkozni.",
    "lopor": "Ez a fekete keverék az alkimisták konyhájából tüzet tud teremteni hangos robbanás kíséretében, és ez bizony durva dolgokat tud művelni! Építhetünk fémcsöveket, amiket megtöltünk ezzel a porral, és nehéz golyókat lövünk ki belőlük!",
    "robotok": "A tudósaink építettek egy mechanikus óriást fémizmokkal és gőz hajtotta szívvel! Csakis a legelszántabb és legképzettebb katonák mernének szembeszállni egy ilyen kolosszussal!",
    "agyuepites": "A vasunk kezd keményebb és nehezebb lenni: most már építhetünk nagy hengerszerű csöveket, melyeken keresztül nagy golyókat lőhetünk az ellenségre! Ha ilyen golyókat lövünk nagy távolságról az ellenségre, a falaik összeomlanak, és félni fognak minket!",
    "hadugyjovoje": "A harci gépezeteink nagyobbak és erősebbek, mint valaha, és a seregünk sokkal szervezettebb! A civil vezetés mindent irányítás alá vesz, és a fenntartási költség is kevesebb."
}


def timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


def fejlesztes():
    newWindow = Toplevel(root)
    newWindow.title("Fejlesztések")
    newWindow.geometry("400x500")
    Label(newWindow, text="Fejlesztések").place(x=0, y=25)
    Label(newWindow, text="Hajógyár").place(x=0, y=50)
    Button(newWindow, text="Build").place(x=300, y=25)
    Button(newWindow, text="Build").place(x=300, y=50)


def red_build():
    newWindow = Toplevel(root)
    newWindow.title("Üres beépíthető terület")
    newWindow.geometry("400x500")
    Label(newWindow, text="Akadémia").place(x=0, y=25)
    Label(newWindow, text="Barakk").place(x=0, y=50)
    Label(newWindow, text="Ácsmester").place(x=0, y=75)
    Label(newWindow, text="Raktár épület").place(x=0, y=100)
    Label(newWindow, text="Kereskedo poszt").place(x=0, y=125)
    Label(newWindow, text="Fogadó").place(x=0, y=150)
    Label(newWindow, text="Palota").place(x=0, y=175)
    Label(newWindow, text="Rejtekhely").place(x=0, y=200)
    Label(newWindow, text="Erdeszház").place(x=0, y=225)
    Label(newWindow, text="Bortermelo").place(x=0, y=250)
    Label(newWindow, text="Nagykövetség").place(x=0, y=275)
    Label(newWindow, text="Templom").place(x=0, y=300)
    Label(newWindow, text="Mühely").place(x=0, y=325)
    Label(newWindow, text="Múzeum").place(x=0, y=350)
    Label(newWindow, text="Tüzszeresz teszt terület").place(x=0, y=375)
    Label(newWindow, text="Optikus").place(x=0, y=400)
    Label(newWindow, text="Szölőprés").place(x=0, y=425)
    Label(newWindow, text="Nyersanyag").place(x=0, y=450)
    Button(newWindow, text="Build", command=akademia).place(x=300, y=25)
    Button(newWindow, text="Build", command=barakk).place(x=300, y=50)
    Button(newWindow, text="Build", command=acsmester).place(x=300, y=75)
    Button(newWindow, text="Build", command=raktar).place(x=300, y=100)
    Button(newWindow, text="Build", command=piac).place(x=300, y=125)
    Button(newWindow, text="Build", command=fogado).place(x=300, y=150)
    Button(newWindow, text="Build", command=palota).place(x=300, y=175)
    Button(newWindow, text="Build", command=rejtekhely).place(x=300, y=200)
    Button(newWindow, text="Build", command=rejtekhely).place(x=300, y=225)
    Button(newWindow, text="Build", command=erdeszhaz).place(x=300, y=250)
    Button(newWindow, text="Build", command=bortermelo).place(x=300, y=275)
    Button(newWindow, text="Build", command=nagykovetseg).place(x=300, y=300)
    Button(newWindow, text="Build", command=templom).place(x=300, y=325)
    Button(newWindow, text="Build", command=muhely).place(x=300, y=350)
    Button(newWindow, text="Build", command=muzeum).place(x=300, y=375)
    Button(newWindow, text="Build", command=tuzszeresz).place(x=300, y=400)
    Button(newWindow, text="Build", command=optikus).place(x=300, y=425)
    Button(newWindow, text="Build", command=szolopres).place(x=300, y=450)


def green_build():
    newWindow = Toplevel(root)
    newWindow.title("Üres beépíthető terület")
    newWindow.geometry("400x500")
    Label(newWindow, text="Kereskedelmi kikötő").place(x=0, y=25)
    Label(newWindow, text="Hajógyár").place(x=0, y=50)
    Button(newWindow, text="Build").place(x=300, y=25)
    Button(newWindow, text="Build").place(x=300, y=50)


def yellow_build():
    build_time = 60
    newWindow = Toplevel(root)
    newWindow.title("Üres beépíthető terület")
    newWindow.geometry("400x500")
    Label(newWindow, text="Városfal").place(x=0, y=25)
    Button(newWindow, text="Build", command=build_varosfal).place(x=300, y=25)


def yellow_upgrade():
    newWindow = Toplevel(root)
    newWindow.title("Városfal")
    newWindow.geometry("400x500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=200, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=300, y=25)


def acsmester():
    newWindow = Toplevel(root)
    newWindow.title("Ácsmester")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['acsmester'],
          font=("Arial", 8)).place(x=300, y=25)


def raktar():
    newWindow = Toplevel(root)
    newWindow.title("Raktár")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['raktar'],
          font=("Arial", 8)).place(x=300, y=25)


def piac():
    newWindow = Toplevel(root)
    newWindow.title("Piac")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['piac'],
          font=("Arial", 8)).place(x=300, y=25)


def fogado():
    newWindow = Toplevel(root)
    newWindow.title("Fogadó")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['fogado'],
          font=("Arial", 8)).place(x=300, y=25)


def palota():
    newWindow = Toplevel(root)
    newWindow.title("Palota")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['palota'],
          font=("Arial", 8)).place(x=300, y=25)


def rejtekhely():
    newWindow = Toplevel(root)
    newWindow.title("Rejtekhely")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['rejtekhely'],
          font=("Arial", 8)).place(x=300, y=25)


def erdeszhaz():
    newWindow = Toplevel(root)
    newWindow.title("Erdészház")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['erdeszhaz'],
          font=("Arial", 8)).place(x=300, y=25)


def bortermelo():
    newWindow = Toplevel(root)
    newWindow.title("Bortermelő")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['bortermelo'],
          font=("Arial", 8)).place(x=300, y=25)


def nagykovetseg():
    newWindow = Toplevel(root)
    newWindow.title("Nagykövetség")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['nagykovetseg'],
          font=("Arial", 8)).place(x=300, y=25)


def templom():
    newWindow = Toplevel(root)
    newWindow.title("Templom")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['templom'],
          font=("Arial", 8)).place(x=300, y=25)


def epitesz():
    newWindow = Toplevel(root)
    newWindow.title("Építész")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['epitesz'],
          font=("Arial", 8)).place(x=300, y=25)


def muhely():
    newWindow = Toplevel(root)
    newWindow.title("muhely")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['muhely'],
          font=("Arial", 8)).place(x=300, y=25)


def muzeum():
    newWindow = Toplevel(root)
    newWindow.title("muzeum")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['muzeum'],
          font=("Arial", 8)).place(x=300, y=25)


def tuzszeresz():
    newWindow = Toplevel(root)
    newWindow.title("Tüzszeresz")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['tuzszeresz'],
          font=("Arial", 8)).place(x=300, y=25)


def optikus():
    newWindow = Toplevel(root)
    newWindow.title("Optikus")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['optikus'],
          font=("Arial", 8)).place(x=300, y=25)


def szolopres():
    newWindow = Toplevel(root)
    newWindow.title("Szölőprés")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['szolopres'],
          font=("Arial", 8)).place(x=300, y=25)


def akademia():
    newWindow = Toplevel(root)
    newWindow.title("Akedémia")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['akademia'],
          font=("Arial", 8)).place(x=300, y=25)


def barakk():
    newWindow = Toplevel(root)
    newWindow.title("Barakk")
    newWindow.geometry("800x1500")
    Button(newWindow, text="Fejleszt",
           command=build_varosfal).place(x=50, y=25)
    Button(newWindow, text="Lerombol",
           command=build_varosfal).place(x=100, y=25)
    Label(newWindow, text=buildings['barakk'],
          font=("Arial", 8)).place(x=300, y=25)


def kikoto():
    newWindow = Toplevel(root)
    hajok_szama = get_teherhajok_szama()
    hajo_ar = get_ar_teherhajo(hajok_szama)
    arany = get_arany()
    newWindow.title("Teherhajó")
    newWindow.geometry("400x500")
    Label(newWindow, text="Teherhajok szama:").place(x=100, y=15)
    Label(newWindow, text=hajok_szama).place(x=200, y=15)
    Label(newWindow, text="Ár:").place(x=100, y=45)
    Label(newWindow, text=hajo_ar).place(x=100, y=45)
    Button(newWindow, text="Teherhajó vétel",
           command=teherhajo_vetel).place(x=200, y=45)
    Label(newWindow, text='Jelenlegi arany:').place(x=100, y=75)
    Label(newWindow, text=arany).place(x=200, y=75)


def varoshaza():
    newWindow = Toplevel(root)
    newWindow.title("Városháza")
    newWindow.geometry("400x500")
    max_lakossag = 60
    current_lakossag = 60
    varosnev = "Polisz"
    num = 23

    Label(newWindow, text=varosnev).place(x=200, y=10)
    Button(newWindow, text="átnevez").place(x=320, y=10)
    Label(newWindow, text="Lakóhely:").place(x=100, y=40)
    Label(newWindow, text=current_lakossag).place(x=160, y=40)
    Label(newWindow, text="/").place(x=180, y=40)
    Label(newWindow, text=max_lakossag).place(x=190, y=40)
    Label(newWindow, text="Akció pontok:").place(x=100, y=60)
    Label(newWindow, text="Növekedés:").place(x=240, y=40)
    Label(newWindow, text=num).place(x=340, y=40)

    # Button(newWindow, text="Fejleszt",
    #        command=build_varosfal).place(x=200, y=25)
    # Button(newWindow, text="Lerombol",
    #        command=build_varosfal).place(x=300, y=25)


def get_red_pos1():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['1']


def set_red_pos1(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = bulding_name
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos2(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = bulding_name
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos3(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = bulding_name
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos4(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = bulding_name
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos5(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = bulding_name
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos6(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = bulding_name
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos7(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = bulding_name
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos8(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = bulding_name
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos9(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = bulding_name
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos10(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = bulding_name
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos11(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = bulding_name
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos12(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = bulding_name
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos13(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = bulding_name
            newRecord['14'] = elem['14']
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos14(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = bulding_name
            newRecord['15'] = elem['15']
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def set_red_pos15(bulding_name):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            newRecord = {}
            newRecord['1'] = elem['1']
            newRecord['2'] = elem['2']
            newRecord['3'] = elem['3']
            newRecord['4'] = elem['4']
            newRecord['5'] = elem['5']
            newRecord['6'] = elem['6']
            newRecord['7'] = elem['7']
            newRecord['8'] = elem['8']
            newRecord['9'] = elem['9']
            newRecord['10'] = elem['10']
            newRecord['11'] = elem['11']
            newRecord['12'] = elem['12']
            newRecord['13'] = elem['13']
            newRecord['14'] = elem['14']
            newRecord['15'] = bulding_name
            newVersion.append(newRecord)
        with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\place_building.json', 'w') as f:
            f.write(json.dumps(newVersion))


def get_red_pos2():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['2']


def get_red_pos3():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['3']


def get_red_pos4():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['4']


def get_red_pos5():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['5']


def get_red_pos6():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['6']


def get_red_pos7():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['7']


def get_red_pos8():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['8']


def get_red_pos9():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['9']


def get_red_pos10():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['10']


def get_red_pos11():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['11']


def get_red_pos12():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['12']


def get_red_pos13():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['13']


def get_red_pos14():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['14']


def get_red_pos15():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['15']


def teherhajo_vetel():
    teherhajok_szama = get_teherhajok_szama()
    teherhajok_szama += 1
    set_teherhajok(teherhajok_szama)
    ar = get_ar_teherhajo(teherhajok_szama)
    print(ar)
    osszes_arany = get_arany()
    jelenlegi_arany = osszes_arany - ar
    print(jelenlegi_arany)
    set_arany(jelenlegi_arany)


def get_level_varosfal():
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            if elem["username"] == 'me':
                return elem["varosfal"]


def get_teherhajok_szama():
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\teherhajo.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['osszes']


print(get_teherhajok_szama())


def get_ar_teherhajo(count):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\teherhajo_ar.json') as f:
        gobble = json.loads(f.read())
        for element in gobble:
            for key, value in element.items():
                if int(key) == int(count) + 1:
                    return value


print(get_level_varosfal())
# return in this form {'fa : 114}


def get_cost_varosfal():
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\varosfal.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            for key, value in elem.items():
                if int(key) == get_level_varosfal():
                    return value


def get_osszes_fa():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\nyersanyag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            for key, value in elem.items():
                if key == 'fa':
                    return (value)


def get_osszes_marvany():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\nyersanyag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            for key, value in elem.items():
                if key == 'marvany':
                    return(value)


def get_arany():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\nyersanyag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            for key, value in elem.items():
                if key == 'arany':
                    return(value)


get_osszes_fa()


def set_teherhajok(amount):
    newVersion = []
    newRecord = {}
    newRecord['osszes'] = amount
    newVersion.append(newRecord)
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\teherhajo.json', 'w') as f:
        f.write(json.dumps(newVersion))


def set_osszes_marvany(marvany):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\nyersanyag.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            if elem['username'] == 'me':
                newRecord = {}
                newRecord['fa'] = elem['fa']
                newRecord['username'] = elem['username']
                newRecord['bor'] = elem['bor']
                newRecord['marvany'] = marvany
                newRecord['kristaly'] = elem['kristaly']
                newRecord['ken'] = elem['ken']
                newRecord['arany'] = elem['arany']
                newRecord['hajo'] = elem['hajo']
                newRecord['fejlesztes'] = elem['fejlesztes']
                newVersion.append(newRecord)
            else:
                newRecord = {}
                newRecord['fa'] = elem['fa']
                newRecord['username'] = elem['username']
                newRecord['bor'] = elem['bor']
                newRecord['marvany'] = elem['marvany']
                newRecord['kristaly'] = elem['kristaly']
                newRecord['ken'] = elem['ken']
                newRecord['arany'] = elem['arany']
                newRecord['hajo'] = elem['hajo']
                newRecord['fejlesztes'] = elem['fejlesztes']
                newVersion.append(newRecord)
            with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\nyersanyag.json', 'w') as f:
                f.write(json.dumps(newVersion))


def set_osszes_fa(fa):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\nyersanyag.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            if elem['username'] == 'me':
                newRecord = {}
                newRecord['fa'] = fa
                newRecord['username'] = elem['username']
                newRecord['bor'] = elem['bor']
                newRecord['marvany'] = elem['marvany']
                newRecord['kristaly'] = elem['kristaly']
                newRecord['ken'] = elem['ken']
                newRecord['arany'] = elem['arany']
                newRecord['hajo'] = elem['hajo']
                newRecord['fejlesztes'] = elem['fejlesztes']
                newVersion.append(newRecord)
            else:
                newRecord = {}
                newRecord['fa'] = elem['fa']
                newRecord['username'] = elem['username']
                newRecord['bor'] = elem['bor']
                newRecord['marvany'] = elem['marvany']
                newRecord['kristaly'] = elem['kristaly']
                newRecord['ken'] = elem['ken']
                newRecord['arany'] = elem['arany']
                newRecord['hajo'] = elem['hajo']
                newRecord['fejlesztes'] = elem['fejlesztes']
                newVersion.append(newRecord)
            with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\nyersanyag.json', 'w') as f:
                f.write(json.dumps(newVersion))


def set_arany(arany):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\nyersanyag.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            if elem['username'] == 'me':
                newRecord = {}
                newRecord['fa'] = elem['fa']
                newRecord['username'] = elem['username']
                newRecord['bor'] = elem['bor']
                newRecord['marvany'] = elem['marvany']
                newRecord['kristaly'] = elem['kristaly']
                newRecord['ken'] = elem['ken']
                newRecord['arany'] = arany
                newRecord['hajo'] = elem['hajo']
                newRecord['fejlesztes'] = elem['fejlesztes']
                newVersion.append(newRecord)
            else:
                newRecord = {}
                newRecord['fa'] = elem['fa']
                newRecord['username'] = elem['username']
                newRecord['bor'] = elem['bor']
                newRecord['marvany'] = elem['marvany']
                newRecord['kristaly'] = elem['kristaly']
                newRecord['ken'] = elem['ken']
                newRecord['arany'] = elem['arany']
                newRecord['hajo'] = elem['hajo']
                newRecord['fejlesztes'] = elem['fejlesztes']
                newVersion.append(newRecord)
            with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\nyersanyag.json', 'w') as f:
                f.write(json.dumps(newVersion))


def set_varosfal(level):
    with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\building.json') as f:
        gobble = json.loads(f.read())
        newVersion = []
        for elem in gobble:
            if elem['username'] == 'me':
                newRecord = {}
                newRecord['username'] = elem['username']
                newRecord['varoshaza'] = elem['varoshaza']
                newRecord['akademia'] = elem['akademia']
                newRecord['raktar'] = elem['raktar']
                newRecord['fogado'] = elem['fogado']
                newRecord['palota'] = elem['palota']
                newRecord['helytarto'] = elem['helytarto']
                newRecord['muzeum'] = elem['muzeum']
                newRecord['kikoto'] = elem['kikoto']
                newRecord['hajogyar'] = elem['hajogyar']
                newRecord['barakk'] = elem['barakk']
                newRecord['varosfal'] = level
                newRecord['nagykovetseg'] = elem['nagykovetseg']
                newRecord['piac'] = elem['piac']
                newRecord['muhely'] = elem['muhely']
                newRecord['rejtekhely'] = elem['rejtekhely']
                newRecord['erdeszhaz'] = elem['erdeszhaz']
                newRecord['uvegfuvo'] = elem['uvegfuvo']
                newRecord['alkimistatorony'] = elem['alkimistatorony']
                newRecord['bortermelo'] = elem['bortermelo']
                newRecord['komuves'] = elem['komuves']
                newRecord['acsmester'] = elem['acsmester']
                newRecord['optikus'] = elem['optikus']
                newRecord['tuzszeresz'] = elem['tuzszeresz']
                newRecord['szolopres'] = elem['szolopres']
                newRecord['epitesz'] = elem['epitesz']
                newRecord['templom'] = elem['templom']
                newRecord['kalozerod'] = elem['kalozerod']
                newVersion.append(newRecord)

            else:
                newRecord = {}
                newRecord['username'] = elem['username']
                newRecord['varoshaza'] = elem['varoshaza']
                newRecord['akademia'] = elem['akademia']
                newRecord['raktar'] = elem['raktar']
                newRecord['fogado'] = elem['fogado']
                newRecord['palota'] = elem['palota']
                newRecord['helytarto'] = elem['helytarto']
                newRecord['muzeum'] = elem['muzeum']
                newRecord['kikoto'] = elem['kikoto']
                newRecord['hajogyar'] = elem['hajogyar']
                newRecord['barakk'] = elem['barakk']
                newRecord['varosfal'] = elem['varosfal']
                newRecord['nagykovetseg'] = elem['nagykovetseg']
                newRecord['piac'] = elem['piac']
                newRecord['muhely'] = elem['muhely']
                newRecord['rejtekhely'] = elem['rejtekhely']
                newRecord['erdeszhaz'] = elem['erdeszhaz']
                newRecord['uvegfuvo'] = elem['uvegfuvo']
                newRecord['alkimistatorony'] = elem['alkimistatorony']
                newRecord['bortermelo'] = elem['bortermelo']
                newRecord['komuves'] = elem['komuves']
                newRecord['acsmester'] = elem['acsmester']
                newRecord['optikus'] = elem['optikus']
                newRecord['tuzszeresz'] = elem['tuzszeresz']
                newRecord['szolopres'] = elem['szolopres']
                newRecord['epitesz'] = elem['epitesz']
                newRecord['templom'] = elem['templom']
                newRecord['kalozerod'] = elem['kalozerod']
                newVersion.append(newRecord)
                with open('C:\\Users\\CFY\\Desktop\\prjoketek\\ikariam\\src\\config\\building.json', 'w') as f:
                    f.write(json.dumps(newVersion))


def build_varosfal():
    lvl_varosfal = int(get_level_varosfal())
    # build time in sec
    build_time = varosfal[lvl_varosfal].ido * 60
    print(build_time)
    # time.sleep(build_time)
    isFa = False
    isMarvany = True
    print(lvl_varosfal)
    cost_varosfal = get_cost_varosfal()
    for key, value in cost_varosfal.items():
        if key == 'fa':
            if value < get_osszes_fa():
                osszes_fa = get_osszes_fa() - value
                isFa = True
        if key == 'marvany':
            if value > get_osszes_marvany():
                isMarvany = False
            elif get_osszes_marvany() > value:
                osszes_marvany = get_osszes_marvany() - value
    if isFa and isMarvany:
        set_osszes_marvany(osszes_marvany)
        set_osszes_fa(osszes_marvany)
        lvl_varosfal += 1
        print(lvl_varosfal)
        set_varosfal(lvl_varosfal)
        print('varosfal updated')
    else:
        print("nincs elég nyersanyag")

# blue area


def is_pos1_empty():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\blue_flag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            for key, value in elem.items():
                if(value['name']) == '':
                    return True
                break
    return False


def is_pos2_empty():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\blue_flag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            if(elem.get("pos2").get("name")) == '':
                return True
    return False


def is_pos1_kikoto():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\blue_flag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            for key, value in elem.items():
                if(value['name']) == 'kikoto':
                    return True
                break
    return False


def is_pos1_hajogyar():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\blue_flag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            for key, value in elem.items():
                if(value['name']) == 'hajogyar':
                    return True
                break
    return False


def is_pos2_kikoto():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\blue_flag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            if(elem.get("pos2").get("name")) == 'kikoto':
                return True
    return False


def is_pos2_hajogyar():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\blue_flag.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            if(elem.get("pos2").get("name")) == 'hajogyar':
                return True
    return False


def get_red_pos1():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['1']


def get_red_pos2():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['2']


def get_red_pos3():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['3']


def get_red_pos4():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['4']


def get_red_pos5():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['5']


def get_red_pos6():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['6']


def get_red_pos7():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['7']


def get_red_pos8():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['8']


def get_red_pos9():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['9']


def get_red_pos10():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['10']


def get_red_pos11():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['11']


def get_red_pos12():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['12']


def get_red_pos13():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['13']


def get_red_pos14():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['14']


def get_red_pos15():
    with open('C:\\Users\\CFY\\Desktop\prjoketek\\ikariam\\src\\config\\place_building.json') as f:
        gobble = json.loads(f.read())
        for elem in gobble:
            return elem['15']
# build_varosfal()

# get_cost_varosfal()
# print(type(get_level_varosfal()))


root = Tk()
canvas = Canvas(root, width=5000, height=1500)
# yellowFlag = Label(root, text='got', font="50")
# yellowFlag.place(x=500, y=250)

build_list = ['acsmester', 'akademia', 'alkimistatorony', 'barakk', 'bortermelo', 'epitesz', 'erdeszhaz', 'fogado', 'helytarto', 'kaloz', 'komuves',
              'muhely', 'muzeum', 'nagykovetseg', 'nyersanyag', 'optikus', 'palota', 'piac', 'raktar', 'rejtekhely', 'szolopres', 'remplom', 'tuzszeresz', 'uvegfuvo']


if(get_red_pos1() == ''):
    redFlag1Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag1Button.place(x=520, y=400)
elif get_red_pos1() in build_list:
    path_full = path + "\\" + get_red_pos1() + ".png"
    red1_img = PhotoImage(file=path_full)
    redFlag1 = Button(root, text='build', image=red1_img, font="50")
    redFlag1.place(x=480, y=350)

if get_red_pos2() == '':
    redFlag2Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag2Button.place(x=520, y=520)
elif get_red_pos2() in build_list:
    path_full = path + "\\" + get_red_pos2() + ".png"
    red2_img = PhotoImage(file=path_full)
    redFlag2 = Button(root, text='build', image=red2_img, font="50")
    redFlag2.place(x=480, y=480)

print('red pos3:', get_red_pos3())
if get_red_pos3() == '':
    redFlag3Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag3Button.place(x=560, y=700)
elif get_red_pos3() in build_list:
    path_full = path + "\\" + get_red_pos3() + ".png"
    red3_img = PhotoImage(file=path_full)
    redFlag3 = Button(root, text='build', image=red3_img, font="50")
    redFlag3.place(x=540, y=660)

if get_red_pos4() == '':
    redFlag4Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag4Button.place(x=680, y=560)
elif get_red_pos4() in build_list:
    path_full = path + "\\" + get_red_pos4() + ".png"
    red4_img = PhotoImage(file=path_full)
    redFlag4 = Button(root, text='build', image=red4_img, font="50")
    redFlag4.place(x=540, y=660)

if get_red_pos5() == '':
    redFlag5Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag5Button.place(x=680, y=440)
elif get_red_pos5() in build_list:
    path_full = path + "\\" + get_red_pos5() + ".png"
    red5_img = PhotoImage(file=path_full)
    redFlag5 = Button(root, text='build', image=red5_img, font="50")
    redFlag5.place(x=650, y=380)

if get_red_pos6() == '':
    redFlag6Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag6Button.place(x=880, y=580)
elif get_red_pos6() in build_list:
    path_full = path + "\\" + get_red_pos6() + ".png"
    red6_img = PhotoImage(file=path_full)
    redFlag6 = Button(root, text='build', image=red6_img, font="50")
    redFlag6.place(x=830, y=500)

if get_red_pos7() == '':
    redFlag7Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag7Button.place(x=1040, y=540)
elif get_red_pos7() in build_list:
    path_full = path + "\\" + get_red_pos7() + ".png"
    red7_img = PhotoImage(file=path_full)
    redFlag7 = Button(root, text='build', image=red7_img, font="50")
    redFlag7.place(x=1000, y=450)

if get_red_pos9() == '':
    redFlag9Button = tk.Button(root,
                               text="build",
                               command=red_build)
    redFlag9Button.place(x=1240, y=520)

elif get_red_pos9() in build_list:
    path_full = path + "\\" + get_red_pos9() + ".png"
    red9_img = PhotoImage(file=path_full)
    redFlag9 = Button(root, text='build', image=red9_img, font="50")
    redFlag9.place(x=1240, y=520)

if get_red_pos10() == '':
    redFlag10Button = tk.Button(root,
                                text="build",
                                command=red_build)
    redFlag10Button.place(x=1365, y=570)

elif get_red_pos10() in build_list:
    path_full = path + "\\" + get_red_pos10() + ".png"
    red10_img = PhotoImage(file=path_full)
    redFlag10 = Button(root, text='build', image=red10_img, font="50")
    redFlag10.place(x=1320, y=520)

if get_red_pos11() == '':
    redFlag11Button = tk.Button(root,
                                text="build",
                                command=red_build)
    redFlag11Button.place(x=1350, y=190)

elif get_red_pos11() in build_list:
    path_full = path + "\\" + get_red_pos11() + ".png"
    red11_img = PhotoImage(file=path_full)
    redFlag11 = Button(root, text='build', image=red11_img, font="50")
    redFlag11.place(x=1320, y=140)
if get_red_pos12() == '':
    redFlag12Button = tk.Button(root,
                                text="build",
                                command=red_build)
    redFlag12Button.place(x=940, y=300)
elif get_red_pos12() in build_list:
    path_full = path + "\\" + get_red_pos12() + ".png"
    red12_img = PhotoImage(file=path_full)
    redFlag12 = Button(root, text='build', image=red12_img, font="50")
    redFlag12.place(x=900, y=260)
if get_red_pos13() == '':
    redFlag13Button = tk.Button(root,
                                text="build",
                                command=red_build)
    redFlag13Button.place(x=1120, y=300)
elif get_red_pos13() in build_list:
    path_full = path + "\\" + get_red_pos13() + ".png"
    red13_img = PhotoImage(file=path_full)
    redFlag13 = Button(root, text='build', image=red13_img, font="50")
    redFlag13.place(x=1080, y=230)

if get_red_pos14() == '':
    redFlag14Button = tk.Button(root,
                                text="build",
                                command=red_build)
    redFlag14Button.place(x=1080, y=400)

elif get_red_pos14() in build_list:
    path_full = path + "\\" + get_red_pos14() + ".png"
    red14_img = PhotoImage(file=path_full)
    redFlag14 = Button(root, text='build', image=red14_img, font="50")
    redFlag14.place(x=1040, y=350)

if get_red_pos15() == '':
    redFlag15Button = tk.Button(root,
                                text="build",
                                command=red_build)
    redFlag15Button.place(x=1240, y=360)

elif get_red_pos15() in build_list:
    path_full = path + "\\" + get_red_pos15() + ".png"
    red15_img = PhotoImage(file=path_full)
    redFlag15 = Button(root, text='build', image=red15_img, font="50")
    redFlag15.place(x=1200, y=280)

varoshaza = tk.Button(root,
                      text="show",
                      command=varoshaza)
varoshaza.place(x=910, y=420)

if is_pos1_empty():
    blueFlag1 = Button(root, text='build', font="50")
    blueFlag1.place(x=760, y=720)
if is_pos2_empty():
    blueFlag2 = Button(root, text='build', font="50")
    blueFlag2.place(x=1120, y=700)
if is_pos1_hajogyar():
    hajogyar_img = PhotoImage(file=path+"\\hajogyar.png")
    blueFlag1 = Button(root, text='build', image=hajogyar_img, font="50")
    blueFlag1.place(x=710, y=680)
if is_pos2_hajogyar():
    hajogyar_img1 = PhotoImage(file=path+"\\hajogyar1.png")
    blueFlag2 = Button(root, text='build', image=hajogyar_img1, font="50")
    blueFlag2.place(x=1030, y=650)
if is_pos1_kikoto():
    kikoto_img = PhotoImage(file=path+"\\kikoto.png")
    blueFlag1 = Button(root, text='build', image=kikoto_img,
                       font="50", command=kikoto)
    blueFlag1.place(x=710, y=680)
if is_pos2_kikoto():
    kikoto_img1 = PhotoImage(file=path+"\\kikoto1.png")
    blueFlag2 = Button(root, text='build', image=kikoto_img1,
                       font="50", command=kikoto)
    blueFlag2.place(x=1030, y=650)
canvas.pack()

print(path)
img = PhotoImage(file=path+"\\main.png")
canvas.create_image(150, 100, anchor=NW, image=img)
varosfal_level = get_level_varosfal()
if(varosfal_level == 0):
    yellowFlagButton = Button(
        root, text='build', font="50", command=yellow_build, width=50, height=140)
    yellowFlagButton.place(x=500, y=250)
else:

    varosfal_img = PhotoImage(file=path+"\\varosfal.png")
    yellowFlagButton = Button(root, image=varosfal_img,
                              borderwidth=0, command=yellow_upgrade)
    yellowFlagButton.place(x=400, y=200)
    # canvas.create_image(440, 220, anchor=NW, image=varosfal_img)

# print('osszes_fa:', get_osszes_fa())

mainloop()
