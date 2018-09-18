
cache_hit = 0
cache_miss = 0
i = 0
cache_size = int(input("cache size: "))
#list size 초기화
cache_list = [None] * int(cache_size)
#input value == str 정수형으로 반드시 바꿀것
city_size = int(input("city size: "))
cities = list()

while i < city_size :
    cities.append((input("city name: ")))
    i += 1
cache_time = [0] * cache_size

for i in range(cache_size):
    cache_list[i] = cities[i]
    cache_time[i] = cache_size - i
    cache_miss += 5    
i = 0
j = cache_size
getcha = False

while j < city_size : 
    while i <cache_size:
        #python 대소문자 무시 코드
        if cities[j].lower() == cache_list[i] :
            
            print(cities[j])
            k = 0
            #cache time ++
            while k < cache_size:
                cache_time[k] += 1
                k+=1
            
            cache_time[i] = 0
            getcha = True
            print("hit")
            cache_hit += 1
        i+=1    

        #cache delete
    if getcha == False and cache_size != 0:
        temp = 0
        i = 0
        get = 0
        max_size = 0

        for temp in cache_time: 
            print(cache_time)
            if int(temp) > max_size:
                max_size = int(temp)
                get = i
            i += 1

        k =0
        while k < cache_size:
                cache_time[k] += 1
                k+=1
        cache_time[get] = 0
        cache_list[get] = cities[j]
        cache_miss += 5
        print("miss")
    else:
        cache_hit = 0
        cache_miss = city_size*5
    getcha = False
    j+=1
    i=0 
    print(cache_time)
    print(cache_list)

print(cache_hit+cache_miss)