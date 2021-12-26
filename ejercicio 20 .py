if __name__ == '__main__':
     print("ubique el numero  : ")
     num = int(input())
     c1 = (num-(num%100))/100
     r1 = num%100
     c2 = (r1-(r1%10))/10
     r2 = r1%10
     if num==((r2*100)+(c2*10)+c1):
          print("este numero es capicuo ")
     else:
          print("este numero no es capicuo")