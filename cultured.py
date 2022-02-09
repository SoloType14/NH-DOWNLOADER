import requests
from bs4 import BeautifulSoup
import os
import re
import sys
import io


def main():
    while True:   
        sauce = input("Sauce: ")
        url = 'https://nhentai.net/g/' + sauce + '/'
        folder = input('Name:')
        os.mkdir(os.path.join(os.getcwd(), folder))
        os.chdir(os.path.join(os.getcwd(), folder))

        r= requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        soup.prettify()

        imgCount = soup.find_all('div', 'thumb-container')

        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(len(imgCount))

        countImg = new_stdout.getvalue()
        sys.stdout = old_stdout

        countImg = int(countImg)

        #print(type(countImg))

        nums = 0

        while nums < countImg :
            #print(nums)
            nums += 1

            dlurl = url + str(nums) + '/'
            req = requests.get(dlurl)
            soup = BeautifulSoup(req.text, 'html.parser')
            
            #img = soup.find_all('img')
            #for image in  img:
                #    if re.findall(r".+(?=jpg|png|jpeg)"): 
                #      print(image['src'])
            for img in soup.find_all("img" , src=True):
                if re.findall(r".+(?=jpg|png|jpeg)",img['src']): 
                # find out if the url contain jpg or png or jpeg , if not return a empty list. empty list is False
                    #print(img['src'])
                    link = img['src']
                    i=1
                    while os.path.exists(f"{i}.jpg"):
                        i+=1  
                    file = open(f'{i}.jpg', 'wb')
                    dl = requests.get(link)
                    file.write(dl.content)
                    print('Downloading:', file.name)
                    
        os.chdir('..')
        if input('Do you want to repeat(y/n)') == 'n':
            break
                                    
                
    
if __name__ == '__main__':
    main()



  
    
    
    
    
    




    
    
    

    
    







