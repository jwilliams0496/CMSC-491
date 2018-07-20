from geopy import geocoders

Bing_Key = 'Ag0T3odWUsHkFyVhp8Lw8oruQo1tsWUw1PuHC_yiiy3edtmXnWZ2WMKHob6504ZL'
g = geocoders.Bing(Bing_Key)

print g.geocode("Nashville, AR", exactly_one = False)