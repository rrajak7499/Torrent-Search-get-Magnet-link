# Torrent Search And Get Magnet Link

import requests
import subprocess,sys

def main():
    search_for_torrnets = input("Search Here : \n")
    print(f"Searching for {search_for_torrnets}")
    base_url = f"https://api.sumanjay.cf/torrent/?query={search_for_torrnets}"
    torrent_results = requests.get(base_url).json()
    index = 1
    magnet= []
    for result in torrent_results:
        if 'app' in result['type'].lower():
            print('\n')
            print(index,") ",result['name'],"\n\tSize ->",result['size'],", Seed ->",result['seeder'])
            index+=1
            magnet.append(result['magnet'])
        if 'movie' in result['type'].lower():
            print('\n')
            print(index,") ",result['name'],"\n\tSize ->",result['size'],", Seed ->",result['seeder'])
            index+=1
            magnet.append(result['magnet'])

    choice = int(input("\n\nEnter the index of the search result which you want to download\n"))
    magnet_link = magnet[choice-1]
    print(magnet_link)

if __name__ == "__main__":
    main()
    
    #Thanks for the api Suman sir
