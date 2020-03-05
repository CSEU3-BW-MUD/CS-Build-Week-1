from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.rooms import room_title, room_descriptions

# cities = ["Abbott", "Abernathy", "Abilene", "Abram-Perezville", "Ackerly", "Addison", "Adrian", "Agua Dulce", "Agua Dulce", "Airport Road Addition", "Alamo", "Alamo Heights", "Alba", "Albany", "Aldine", "Aledo", "Alfred-South La Paloma", "Alice", "Alice Acres", "Allen", "Alma", "Alpine", "Alto", "Alto Bonito", "Alton", "Alton North", "Alvarado", "Alvin", "Alvord", "Amarillo", "Ames", "Amherst", "Anahuac", "Anderson", "Anderson Mill", "Andrews", "Angleton", "Angus", "Anna", "Annetta", "Annetta North", "Annetta South", "Annona", "Anson", "Anthony", "Anton", "Appleby", "Aquilla", "Aransas Pass", "Archer City", "Arcola", "Argyle", "Arlington", "Arp", "Arroyo Alto", "Arroyo Colorado Estates", "Arroyo Gardens-La Tina Ranch", "Asherton", "Aspermont", "Atascocita", "Athens", "Atlanta", "Aubrey", "Aurora", "Austin", "Austwell", "Avery", "Avinger", "Azle", "Bacliff", "Bailey", "Bailey'S Prairie", "Baird", "Balch Springs", "Balcones Heights", "Ballinger", "Balmorhea", "Bandera", "Bangs", "Bardwell", "Barrett", "Barry", "Barstow", "Bartlett", "Barton Creek", "Bartonville", "Bastrop", "Batesville", "Bausell And Ellis", "Bay City", "Bayou Vista", "Bayside", "Baytown", "Bayview", "Beach City", "Bear Creek", "Beasley", "Beaumont", "Beckville", "Bedford", "Bee Cave", "Beeville", "Bellaire", "Bellevue", "Bellmead", "Bells", "Bellville", "Belton", "Benavides", "Benbrook", "Benjamin", "Berryville", "Bertram", "Beverly Hills", "Bevil Oaks", "Bigfoot", "Big Lake", "Big Sandy", "Big Spring", "Big Wells", "Bishop", "Bishop Hills", "Bixby", "Blackwell", "Blanco", "Blanket", "Blessing", "Bloomburg", "Blooming Grove", "Bloomington", "Blossom", "Blue Berry Hill", "Blue Mound", "Blue Ridge", "Bluetown-Iglesia Antigua", "Blum", "Boerne", "Bogata", "Boling-Iago", "Bolivar Peninsula", "Bonham", "Bonney", "Booker", "Borger", "Botines", "Bovina", "Bowie", "Box Canyon-Amistad", "Boyd", "Brackettville", "Brady", "Brazoria", "Breckenridge", "Bremond", "Brenham", "Briar", "Briarcliff", "Briaroaks", "Bridge City", "Bridgeport", "Broaddus", "Bronte", "Brookshire", "Brookside Village", "Browndell", "Brownfield", "Brownsboro", "Brownsville", "Brownwood", "Bruceville-Eddy", "Brundage", "Bruni", "Brushy Creek", "Bryan", "Bryson", "Buchanan Dam", "Buckholts", "Buda", "Buffalo", "Buffalo Gap", "Buffalo Springs", "Bullard", "Bulverde", "Buna", "Bunker Hill Village", "Burkburnett", "Burke", "Burleson", "Burnet", "Burton", "Butterfield", "Byers", "Bynum", "Cactus", "Caddo Mills", "Caldwell", "Callisburg", "Calvert", "Cameron", "Cameron Park", "Campbell", "Camp Swift", "Camp Wood", "Canadian", "Caney City", "Canton", "Cantu Addition", "Canutillo", "Canyon", "Canyon Lake", "Carbon", "Carl'S Corner", "Carmine", "Carrizo Hill", "Carrizo Springs", "Carrollton", "Carthage", "Castle Hills", "Castroville", "Catarina", "Cedar Hill", "Cedar Park", "Celeste", "Celina", "Center", "Centerville", "Central Gardens", "Cesar Chavez", "Chandler", "Channelview", "Channing", "Charlotte", "Chester", "Chico", "Childress", "Chillicothe", "China", "China Grove", "Chireno", "Christine", "Christoval", "Chula Vista-Orason", "Chula Vista-River Spur", "Cibolo", "Cienegas Terrace", "Cinco Ranch", "Circle D-Kc Estates", "Cisco", "Citrus City", "Clarendon", "Clarksville", "Clarksville City", "Claude", "Clear Lake Shores", "Cleburne", "Cleveland", "Clifton", "Clint", "Cloverleaf", "Clute", "Clyde", "Coahoma", "Cockrell Hill", "Coffee City", "Coldspring", "Coleman", "College Station", "Colleyville", "Collinsville", "Colmesneil", "Colorado City", "Columbus", "Comanche", "Combes", "Combine", "Comfort", "Commerce", "Como", "Concepcion", "Conroe", "Converse", "Cool", "Coolidge", "Cooper", "Coppell", "Copperas Cove", "Copper Canyon", "Corinth", "Corpus Christi", "Corral City", "Corrigan", "Corsicana", "Cottonwood", "Cottonwood Shores", "Cotulla", "Cove", "Covington", "Coyanosa", "Coyote Acres", "Crandall", "Crane", "Cranfills Gap", "Crawford", "Creedmoor", "Crockett", "Crosby", "Crosbyton", "Cross Mountain", "Cross Plains", "Cross Roads", "Cross Timber", "Crowell", "Crowley", "Crystal City", "Cuero", "Cuevitas", "Cumby", "Cumings", "Cuney", "Cushing", "Cut And Shoot", "Daingerfield", "Daisetta", "Dalhart", "Dallas", "Dalworthington Gardens", "Damon", "Danbury", "Darrouzett", "Dawson", "Dayton", "Dayton Lakes", "Dean", "Decatur", "Deer Park", "De Kalb", "De Leon", "Dell City", "Del Mar Heights", "Del Rio", "Del Sol-Loma Linda", "Denison", "Denton", "Denver City", "Deport", "Desoto", "Detroit", "Devers", "Devine", "Deweyville", "Diboll", "Dickens", "Dickinson", "Dilley", "Dimmitt", "Dodd City", "Dodson", "Doffing", "Domino", "Donna", "Doolittle", "Dorchester", "Double Oak", "Douglassville", "Doyle", "Dripping Springs", "Driscoll", "Dublin", "Dumas", "Duncanville", "Eagle Lake", "Eagle Mountain", "Eagle Pass", "Early", "Earth", "East Bernard", "Eastland", "East Mountain", "Easton", "East Tawakoni", "Ector", "Edcouch", "Eden", "Edgecliff Village", "Edgewater-Paisano", "Edgewood", "Edinburg", "Edmonson", "Edna", "Edom", "Edroy", "Eidson Road", "Elbert", "El Camino Angosto", "El Campo", "El Cenizo", "Eldorado", "Electra", "Elgin", "El Indio", "Elkhart", "El Lago", "Elm Creek", "Elmendorf", "El Paso", "El Refugio", "Elsa", "Emhouse", "Emory", "Encantada-Ranchito El Calaboz", "Enchanted Oaks", "Encinal", "Encino", "Ennis", "Escobares", "Estelline", "Euless", "Eureka", "Eustace", "Evadale", "Evant", "Everman", "Fabens", "Fairchilds", "Fairfield", "Fair Oaks Ranch", "Fairview", "Falcon Heights", "Falcon Lake Estates", "Falcon Mesa", "Falcon Village", "Falfurrias", "Falls City", "Falman-County Acres", "Farmers Branch", "Farmersville", "Farwell", "Fate", "Fayetteville", "Faysville", "Ferris", "Fifth Street", "Flatonia", "Florence", "Floresville", "Flowella", "Flower Mound", "Floydada", "Follett", "Forest Hill", "Forney", "Forsan", "Fort Bliss", "Fort Davis", "Fort Hancock", "Fort Hood", "Fort Stockton", "Fort Worth", "Four Corners", "Fowlerton", "Franklin", "Frankston", "Fredericksburg", "Freeport", "Freer", "Fresno", "Friendswood", "Friona", "Frisco", "Fritch", "Fronton", "Frost", "Fruitvale", "Fulshear", "Fulton", "Gainesville", "Galena Park", "Gallatin", "Galveston", "Ganado", "Garceno", "Gardendale", "Garden Ridge", "Garfield", "Garland", "Garrett", "Garrison", "Gary City", "Gatesville", "Georgetown", "George West", "Geronimo", "Gholson", "Giddings", "Gilmer", "Girard", "Gladewater", "Glenn Heights", "Glen Rose", "Godley", "Goldsmith", "Goldthwaite", "Goliad", "Golinda", "Gonzales", "Goodlow", "Goodrich", "Gordon", "Goree", "Gorman", "Graford", "Graham", "Granbury", "Grand Acres", "Grandfalls", "Grand Prairie", "Grand Saline", "Grandview", "Granger", "Granite Shoals", "Granjeno", "Grape Creek", "Grapeland", "Grapevine", "Grays Prairie", "Greatwood", "Green Valley Farms", "Greenville", "Gregory", "Grey Forest", "Groesbeck", "Groom", "Groves", "Groveton", "Gruver", "Guerra", "Gun Barrel City", "Gunter", "Gustine", "Hackberry", "Hale Center", "Hallettsville", "Hallsburg", "Hallsville", "Haltom City", "Hamilton", "Hamlin", "Happy", "Hardin", "Harker Heights", "Harlingen", "Harper", "Hart", "Hartley", "Haskell", "Haslet", "Havana", "Hawk Cove", "Hawkins", "Hawley", "Hays", "Hearne", "Heath", "Hebbronville", "Hebron", "Hedley", "Hedwig Village", "Heidelberg", "Helotes", "Hemphill", "Hempstead", "Henderson", "Henrietta", "Hereford", "Hermleigh", "Hewitt", "Hickory Creek", "Hico", "Hidalgo", "Higgins", "Highland Haven", "Highland Park", "Highlands", "Highland Village", "Hill Country Village", "Hillcrest", "Hillsboro", "Hilltop", "Hilshire Village", "Hitchcock", "Holiday Lakes", "Holland", "Holliday", "Hollywood Park", "Homestead Meadows North", "Homestead Meadows South", "Hondo", "Honey Grove", "Hooks", "Horizon City", "Horseshoe Bay", "Houston", "Howardwick", "Howe", "Hubbard", "Hudson", "Hudson Bend", "Hudson Oaks", "Hughes Springs", "Humble", "Hungerford", "Hunters Creek Village", "Huntington", "Huntsville", "Hurst", "Hutchins", "Hutto", "Huxley", "Idalou", "Impact", "Imperial", "Indian Hills", "Indian Lake", "Industry", "Inez", "Ingleside", "Ingleside On The Bay", "Ingram", "Iowa Colony", "Iowa Park", "Iraan", "Iredell", "Irving", "Italy", "Itasca", "Jacinto City", "Jacksboro", "Jacksonville", "Jamaica Beach", "Jasper", "Jayton", "Jefferson", "Jersey Village", "Jewett", "Joaquin", "Johnson City", "Jolly", "Jollyville", "Jones Creek", "Jonestown", "Josephine", "Joshua", "Jourdanton", "Junction", "Justin", "Karnes City", "Katy", "Kaufman", "K-Bar Ranch", "Keene", "Keller", "Kemah", "Kemp", "Kempner", "Kendleton", "Kenedy", "Kenefick", "Kennard", "Kennedale", "Kerens", "Kermit", "Kerrville", "Kilgore", "Killeen", "Kingsbury", "Kingsland", "Kingsville", "Kirby", "Kirbyville", "Kirvin", "Knippa", "Knollwood", "Knox City", "Kosse", "Kountze", "Kress", "Krugerville", "Krum", "Kyle", "La Blanca", "La Casita-Garciasville", "Lackland Afb", "Lacoste", "Lacy-Lakeview", "Ladonia", "La Feria", "La Feria North", "Lago", "Lago Vista", "La Grange", "La Grulla", "Laguna Heights", "Laguna Seca", "Laguna Vista", "La Homa", "La Joya", "Lake Bridgeport", "Lake Brownwood", "Lake City", "Lake Dallas", "Lakehills", "Lake Jackson", "Lake Kiowa", "Lakeport", "Lakeshore Gardens-Hidden Acres", "Lakeside", "Lakeside", "Lakeside City", "Lake Tanglewood", "Lakeview", "Lake View", "Lakeway", "Lakewood Village", "Lake Worth", "La Marque", "Lamesa", "Lampasas", "Lancaster", "La Paloma", "La Paloma-Lost Creek", "La Porte", "La Presa", "La Pryor", "La Puerta", "Laredo", "Laredo Ranchettes", "Larga Vista", "La Rosita", "Lasana", "Lasara", "Las Colonias", "Las Lomas", "Las Lomitas", "Las Palmas-Juarez", "Las Quintas Fronterizas", "Latexo", "Laughlin Afb", "Laureles", "La Vernia", "La Victoria", "La Villa", "Lavon", "La Ward", "Lawn", "League City",
#           "Leakey", "Leander", "Leary", "Lefors", "Leona", "Leonard", "Leon Valley", "Leroy", "Levelland", "Lewisville", "Lexington", "Liberty", "Liberty City", "Liberty Hill", "Lincoln Park", "Lindale", "Linden", "Lindsay", "Lindsay", "Lipan", "Lipscomb", "Little Elm", "Littlefield", "Little River-Academy", "Live Oak", "Liverpool", "Livingston", "Llano", "Llano Grande", "Lockhart", "Lockney", "Log Cabin", "Lolita", "Loma Linda East", "Lometa", "Lone Oak", "Lone Star", "Longview", "Lopeno", "Lopezville", "Loraine", "Lorena", "Lorenzo", "Los Alvarez", "Los Angeles Subdivision", "Los Ebanos", "Los Fresnos", "Los Indios", "Lost Creek", "Los Villareales", "Los Ybanez", "Lott", "Louise", "Lovelady", "Lowry Crossing", "Lozano", "Lubbock", "Lucas", "Lueders", "Lufkin", "Luling", "Lumberton", "Lyford", "Lyford South", "Lytle", "Mabank", "Mcallen", "Mccamey", "Mcgregor", "Mckinney", "Mclean", "Mclendon-Chisholm", "Mcqueeney", "Madisonville", "Magnolia", "Malakoff", "Malone", "Manor", "Mansfield", "Manvel", "Marathon", "Marble Falls", "Marfa", "Marietta", "Marion", "Markham", "Marlin", "Marquez", "Marshall", "Marshall Creek", "Mart", "Martindale", "Mason", "Matador", "Mathis", "Maud", "Mauriceville", "Maypearl", "Meadow", "Meadowlakes", "Meadows Place", "Medina", "Megargel", "Melissa", "Melvin", "Memphis", "Menard", "Mercedes", "Meridian", "Merkel", "Mertens", "Mertzon", "Mesquite", "Mexia", "Miami", "Midland", "Midlothian", "Midway", "Midway North", "Midway South", "Mila Doce", "Milam", "Milano", "Mildred", "Miles", "Milford", "Miller'S Cove", "Millican", "Millsap", "Mineola", "Mineral Wells", "Mingus", "Mirando City", "Mission", "Mission Bend", "Missouri City", "Mobeetie", "Mobile City", "Monahans", "Mont Belvieu", "Monte Alto", "Montgomery", "Moody", "Moore", "Moore Station", "Morales-Sanchez", "Moran", "Morgan", "Morgan Farm Area", "Morgan'S Point", "Morgan'S Point Resort", "Morning Glory", "Morse", "Morton", "Moulton", "Mountain City", "Mount Calm", "Mount Enterprise", "Mount Pleasant", "Mount Vernon", "Muenster", "Muleshoe", "Mullin", "Munday", "Muniz", "Murchison", "Murphy", "Mustang", "Mustang Ridge", "Nacogdoches", "Naples", "Nash", "Nassau Bay", "Natalia", "Navarro", "Navasota", "Nazareth", "Nederland", "Needville", "Nesbitt", "Nevada", "Newark", "New Berlin", "New Boston", "New Braunfels", "Newcastle", "New Chapel Hill", "New Deal", "New Fairview", "New Falcon", "New Home", "New Hope", "New London", "New Summerfield", "New Territory", "Newton", "New Waverly", "Neylandville", "Niederwald", "Nixon", "Nocona", "Nolanville", "Nome", "Noonday", "Nordheim", "Normangee", "Normanna", "North Alamo", "North Cleveland", "Northcliff", "North Escobares", "Northlake", "North Pearsall", "North Richland Hills", "North San Pedro", "Novice", "Nurillo", "Oak Grove", "Oakhurst", "Oak Leaf", "Oak Point", "Oak Ridge", "Oak Ridge", "Oak Ridge North", "Oak Trail Shores", "Oak Valley", "Oakwood", "O'Brien", "Odem", "Odessa", "O'Donnell", "Oglesby", "Oilton", "Old River-Winfree", "Olivarez", "Olmito", "Olmos Park", "Olney", "Olton", "Omaha", "Onalaska", "Onion Creek", "Opdyke West", "Orange", "Orange Grove", "Orchard", "Ore City", "Overton", "Ovilla", "Owl Ranch-Amargosa", "Oyster Creek", "O", "Paducah", "Paint Rock", "Palacios", "Palestine", "Palisades", "Palmer", "Palmhurst", "Palm Valley", "Palmview", "Palmview South", "Pampa", "Panhandle", "Panorama Village", "Pantego", "Paradise", "Paris", "Parker", "Pasadena", "Pattison", "Patton Village", "Pawnee", "Payne Springs", "Pearland", "Pearsall", "Pecan Acres", "Pecan Gap", "Pecan Grove", "Pecan Hill", "Pecan Plantation", "Pecos", "Pelican Bay", "Penelope", "Penitas", "Pernitas Point", "Perryton", "Petersburg", "Petrolia", "Petronila", "Pettus", "Pflugerville", "Pharr", "Pilot Point", "Pine Forest", "Pinehurst", "Pinehurst", "Pine Island", "Pineland", "Pinewood Estates", "Piney Point Village", "Pittsburg", "Plains", "Plainview", "Plano", "Pleak", "Pleasanton", "Pleasant Valley", "Plum Grove", "Point", "Point Blank", "Point Comfort", "Ponder", "Port Aransas", "Port Arthur", "Porter Heights", "Port Isabel", "Portland", "Port Lavaca", "Port Mansfield", "Port Neches", "Post", "Post Oak Bend City", "Poteet", "Poth", "Potosi", "Pottsboro", "Powell", "Poynor", "Prado Verde", "Prairie View", "Premont", "Presidio", "Primera", "Princeton", "Progreso", "Progreso Lakes", "Prosper", "Putnam", "Pyote", "Quail", "Quanah", "Queen City", "Quemado", "Quinlan", "Quintana", "Quitaque", "Quitman", "Radar Base", "Ralls", "Ranchette Estates", "Ranchitos Las Lomas", "Rancho Alegre", "Rancho Banquete", "Rancho Chico", "Ranchos Penitas West", "Rancho Viejo", "Ranger", "Rangerville", "Rankin", "Ransom Canyon", "Ratamosa", "Ravenna", "Raymondville", "Realitos", "Redford", "Red Lick", "Red Oak", "Redwater", "Redwood", "Reese Center", "Refugio", "Reid Hope King", "Reklaw", "Relampago", "Rendon", "Reno", "Reno", "Retreat", "Rhome", "Rice", "Richardson", "Richland", "Richland Hills", "Richland Springs", "Richmond", "Richwood", "Riesel", "Rio Bravo", "Rio Grande City", "Rio Hondo", "Rio Vista", "Rising Star", "River Oaks", "Riverside", "Roanoke", "Roaring Springs", "Robert Lee", "Robinson", "Robstown", "Roby", "Rochester", "Rockdale", "Rockport", "Rocksprings", "Rockwall", "Rocky Mound", "Rogers", "Rollingwood", "Roma", "Roma Creek", "Roman Forest", "Ropesville", "Roscoe", "Rosebud", "Rose City", "Rose Hill Acres", "Rosenberg", "Rosita North", "Rosita South", "Ross", "Rosser", "Rotan", "Round Mountain", "Round Rock", "Round Top", "Rowlett", "Roxton", "Royse City", "Rule", "Runaway Bay", "Runge", "Rusk", "Sabinal", "Sachse", "Sadler", "Saginaw", "St. Hedwig", "St. Jo", "St. Paul", "St. Paul", "Salado", "Salineno", "Samnorwood", "San Angelo", "San Antonio", "San Augustine", "San Benito", "San Carlos", "Sanctuary", "Sanderson", "Sandia", "San Diego", "Sandy Hollow-Escondidas", "San Elizario", "San Felipe", "Sanford", "Sanger", "San Ignacio", "San Isidro", "San Juan", "San Leanna", "San Leon", "San Manuel-Linn", "San Marcos", "San Patricio", "San Pedro", "San Perlita", "San Saba", "Sansom Park", "Santa Anna", "Santa Clara", "Santa Cruz", "Santa Fe", "Santa Maria", "Santa Monica", "Santa Rosa", "Savoy", "Scenic Oaks", "Schertz", "Schulenburg", "Scissors", "Scotland", "Scottsville", "Seabrook", "Seadrift", "Seagoville", "Seagraves", "Sealy", "Sebastian", "Seguin", "Selma", "Seminole", "Serenada", "Seth Ward", "Seven Oaks", "Seven Points", "Seymour", "Shady Hollow", "Shady Shores", "Shallowater", "Shamrock", "Shavano Park", "Sheldon", "Shenandoah", "Shepherd", "Sherman", "Shiner", "Shoreacres", "Sienna Plantation", "Sierra Blanca", "Siesta Shores", "Silsbee", "Silverton", "Simonton", "Sinton", "Skellytown", "Skidmore", "Slaton", "Smiley", "Smithville", "Smyer", "Snook", "Snyder", "Socorro", "Solis", "Somerset", "Somerville", "Sonora", "Sour Lake", "South Alamo", "South Fork Estates", "South Houston", "Southlake", "Southmayd", "South Mountain", "South Padre Island", "South Point", "Southside Place", "South Toledo Bend", "Spade", "Sparks", "Spearman", "Splendora", "Spofford", "Spring", "Spring Garden-Terra Verde", "Springlake", "Springtown", "Spring Valley", "Spur", "Stafford", "Stagecoach", "Stamford", "Stanton", "Star Harbor", "Stephenville", "Sterling City", "Stinnett", "Stockdale", "Stonewall", "Stowell", "Stratford", "Strawn", "Streetman", "Study Butte-Terlingua", "Sudan", "Sugar Land", "Sullivan City", "Sulphur Springs", "Sundown", "Sunnyvale", "Sunray", "Sunrise Beach Village", "Sunset", "Sunset Valley", "Sun Valley", "Surfside Beach", "Sweeny", "Sweetwater", "Taft", "Taft Southwest", "Tahoka", "Talco", "Talty", "Tatum", "Taylor", "Taylor Lake Village", "Teague", "Tehuacana", "Temple", "Tenaha", "Terrell", "Terrell Hills", "Texarkana", "Texas City", "Texhoma", "Texline", "The Colony", "The Hills", "The Woodlands", "Thompsons", "Thorndale", "Thornton", "Thorntonville", "Thrall", "Three Rivers", "Throckmorton", "Tierra Bonita", "Tierra Grande", "Tiki Island", "Timbercreek Canyon", "Timberwood Park", "Timpson", "Tioga", "Tira", "Toco", "Todd Mission", "Tolar", "Tomball", "Tom Bean", "Tool", "Tornillo", "Toyah", "Tradewinds", "Trent", "Trenton", "Trinidad", "Trinity", "Trophy Club", "Troup", "Troy", "Tuleta", "Tulia", "Tulsita", "Turkey", "Tuscola", "Tye", "Tyler", "Tynan", "Uhland", "Uncertain", "Union Grove", "Universal City", "University Park", "Utopia", "Uvalde", "Uvalde Estates", "Valentine", "Valley Mills", "Valley View", "Val Verde Park", "Van", "Van Alstyne", "Vanderbilt", "Van Horn", "Van Vleck", "Vega", "Venus", "Vernon", "Victoria", "Vidor", "Villa Del Sol", "Villa Pancho", "Villa Verde", "Vinton", "Waco", "Waelder", "Wake Village", "Waller", "Wallis", "Walnut Springs", "Warren City", "Waskom", "Watauga", "Waxahachie", "Weatherford", "Webster", "Weimar", "Weinert", "Weir", "Wellington", "Wellman", "Wells", "Wells Branch", "Weslaco", "West", "Westbrook", "West Columbia", "Westdale", "Westlake", "West Lake Hills", "West Livingston", "Westminster", "West Odessa", "Weston", "West Orange", "Westover Hills", "West Pearsall", "West Sharyland", "West Tawakoni", "West University Place", "Westway", "Westworth Village", "Wharton", "Wheeler", "White Deer", "Whiteface", "Whitehouse", "White Oak", "Whitesboro", "White Settlement", "Whitewright", "Whitney", "Wichita Falls", "Wickett", "Wild Peach Village", "Willamar", "Willis", "Willow Park", "Wills Point", "Wilmer", "Wilson", "Wimberley", "Windcrest", "Windemere", "Windom", "Windthorst", "Winfield", "Wink", "Winnie", "Winnsboro", "Winona", "Winters", "Wixon Valley", "Wolfe City", "Wolfforth", "Woodbranch", "Woodcreek", "Woodloch", "Woodsboro", "Woodson", "Woodville", "Woodway", "Wortham", "Wyldwood", "Wylie", "Yantis", "Yoakum", "Yorktown", "Yznaga", "Zapata", "Zapata Ranch", "Zavalla", "Zuehl"]


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        x = -1
        y = 0
        room_count = 0
        direction = 1
        previous_room = None
        while room_count < num_rooms:

            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                room_direction = "n"
                y += 1
                direction *= -1
            room = Room(title=room_title[room_count],
                        description=room_descriptions[room_count], x=x, y=y)
            room.save()
            self.grid[y][x] = room

            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)
            previous_room = room
            room_count += 1


# w = World()
# num_rooms = 100
# width = 10
# height = 10
# w.generate_rooms(width, height, num_rooms)
