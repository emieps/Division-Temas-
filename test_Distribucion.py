import pytest            
import Distribucion as dis 

 
@pytest.mark.parametrize(
   "lst, div, expected",
   [ 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi"], 5, 1)
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise",  "Ashleigh", "Jaxx"], 3, 3),  
      (["Jameson", "Thelma", "Carla", "Emely", "Oz"], 2, 2), 
      (["Deidre", "Tiffany", "Linzi", "Sheelagh", "Kaylani","Lawrence", "Dashiell", "Caitlin"], 8, 3 ), 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 6, 2),
      (["Kylee", "Keaton", "Isaac", "Antonette", "Angus", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 5, 2),

   ]
)

def test_div():
    assert dis.div_numbers(["Lenore", "Candice", "Chanel", "Chet", "Leroi"], 5) == 


 
@pytest.mark.parametrize(
   "lst, div, expected",
   [ 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi"], 5, 1)
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise",  "Ashleigh", "Jaxx"], 3, 3),  
      (["Jameson", "Thelma", "Carla", "Emely", "Oz"], 2, 2), 
      (["Deidre", "Tiffany", "Linzi", "Sheelagh", "Kaylani","Lawrence", "Dashiell", "Caitlin"], 8, 3 ), 
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 6, 2),
      (["Kylee", "Keaton", "Isaac", "Antonette", "Angus", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 5, 2),

   ]
)
