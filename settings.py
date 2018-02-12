from optparse import OptionParser
parser = OptionParser()

settings = {
    "url": "http://api.arbetsformedlingen.se/af/v0",
    "headers": {'Accept': "application/json", 'Accept-Language': "sv"}
}

options = {
    parser.add_option("-l", "--lan", dest="lan",help="Visa antal lediga jobb per län. Använd \"-l all\" för att visa alla län."),
    parser.add_option("-k", "--kommun", dest="kom",help="Visa lediga jobb per kommun. Använd \"-k all\" för att visa alla kommuner."),
    parser.add_option("-t", "--total", dest="total",help="Visa totalt antal platsannonser samt lediga jobb.", action="store_true")
}
(options, args) = parser.parse_args()
