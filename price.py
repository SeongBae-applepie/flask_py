def shopping(shop_file):
  shop_dict = {}  # 생성할 사전 객체
  with open("data/" + shop_file, 'r') as f:
      lines = f.readlines()
      for i in lines:
          if i == '\n':
              None
          else:
              name, won = i.strip().split()
              if name != '#쇼핑몰':
                  shop_dict[name] = won

  return shop_dict

def item_price(shop_file, item):


  shop_dict = {} # 생성할 사전 객체

  with open("data/"+shop_file,'r') as f:
    lines = f.readlines()
    for i in lines:
      if i == '\n':
        None
      else :
        name, won = i.strip().split()
      if name != '#쇼핑몰':
        shop_dict[name] = won

  for a in shop_dict :
    if a == item :
      return shop_dict[a]
