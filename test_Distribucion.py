import pytest            
import Distribucion as dis 

#division 
@pytest.mark.parametrize(
   "lst, div, expect",
   [ 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi"], 5, 1),
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise",  "Ashleigh", "Jaxx"], 3, 3),  
      (["Deidre", "Tiffany", "Linzi", "Sheelagh", "Kaylani","Lawrence", "Dashiell", "Caitlin", "Guridi"], 4, 2), 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 6, 2),
      (["Kylee", "Keaton", "Isaac", "Antonette", "Angus", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 5, 2)

   ]
)

def test_div(lst, div, expect):
    assert dis.div_numbers(lst, div) == expect

@pytest.mark.parametrize(
   "lst, ren, expect",
   [ 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi"], 5, 0),
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise",  "Ashleigh", "Jaxx"], 3, 0),  
      (["Deidre", "Tiffany", "Linzi", "Sheelagh", "Kaylani","Lawrence", "Dashiell", "Caitlin", "Guridi"], 4, 1),  
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 6, 1),
      (["Kylee", "Keaton", "Isaac", "Antonette", "Angus", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 5, 4)

   ]
)

def test_rem(lst, ren, expect):
    assert dis.rem_numbers(lst, ren) == expect

@pytest.mark.parametrize(
   "num, expect",
   [ 
      ("5", 5),
      ("4", 4), 
      ("10", 10)
   ]
)

def test_num_ask(num, expect):
    assert dis.num_ask(num) == expect


@pytest.mark.parametrize(
   "path, expected",
   [ 
      (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std_1.txt", ["Lenore", "Candice", "Chanel", "Chet", "Leroi"]),
      (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std_2.txt", ["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx"]) 
   ]
)

def test_read_file(path, expected):
    assert dis.read_file(path) == expected

@pytest.mark.parametrize(
   "num, std_list, themes_list",
   [ 
      (5, ["Lenore", "Candice", "Chanel", "Chet", "Leroi"], ["Summer", "Pillars", "Honourable", "Bottle", "Cloudy"]),
      (13, ["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 
      ["Valuable", "Thistled", "Fragile", "Entwined", "Treasure", "Elves", "Rigid", "Spring", "Fairies", "Guardian", "Key", "Words", "Angelic"]) 
   ]
)

def test_req(num, std_list, themes_list):
    assert dis.req(num, std_list, themes_list) == True