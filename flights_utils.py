place_to_id_map = {}
place_to_id_map['Bari'] = '0c66m.'
place_to_id_map['Napoli'] = '0fhsz.'
place_to_id_map['Milano'] = '0947l.' 
place_to_id_map['Ginevra'] = '03902.'
place_to_id_map['Venezia'] = '07_pf.'
place_to_id_map['Parigi'] = '05qtj.'

def get_place_id(place_str):
    if place_str not in place_to_id_map:
        print("place not known in my map")
        return ""
    else:
        return place_to_id_map[place_str]
    

def create_url(start, destination, date, currency):
    '''
    start=0c66m. #Bari
    destination=0947l. #Milano
    date=2020-01-01
    currency=CHF
    '''
    url='https://www.google.com/flights?hl=it#flt=/m/'+str(start)+'/m/'+str(destination)+date+';c:'+currency+';e:1;sd:1;t:f;tt:o'
    return url

