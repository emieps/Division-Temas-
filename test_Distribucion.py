import pytest            
import Distribucion as dis 

#division 
@pytest.mark.parametrize(
   "lst, div, expect",
   [ 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi"], 5, 1),
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise",  "Ashleigh", "Jaxx"], 3, 3),  
      (["Jameson", "Thelma", "Carla", "Emely", "Oz"], 2, 2), 
      (["Deidre", "Tiffany", "Linzi", "Sheelagh", "Kaylani","Lawrence", "Dashiell", "Caitlin", "Guridi"], 4, 2), #cambiarlos 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 6, 2),
      (["Kylee", "Keaton", "Isaac", "Antonette", "Angus", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 5, 2),

   ]
)


def test_div(lst, div, expect):
    assert dis.div_numbers(lst, div) == expect

@pytest.mark.parametrize(
   "lst, ren, expect",
   [ 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi"], 5, 0),
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise",  "Ashleigh", "Jaxx"], 3, 0),  
      (["Jameson", "Thelma", "Carla", "Emely", "Oz"], 2, 1), 
      (["Deidre", "Tiffany", "Linzi", "Sheelagh", "Kaylani","Lawrence", "Dashiell", "Caitlin", "Guridi"], 4, 1), #cambiarlos 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 6, 1),
      (["Kylee", "Keaton", "Isaac", "Antonette", "Angus", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 5, 4),

   ]
)

def test_rem(lst, ren, expect):
    assert dis.rem_numbers(lst, ren) == expect
