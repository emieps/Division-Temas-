import pytest            
import Distribucion as dis

@pytest.mark.parametrize(
   "num",
   [    
      ("srt"),
      ("4fwermkflw"), 
      (" "), 
      ("")
   ]
)

def test_num_ask_exit(num):
    with pytest.raises(SystemExit) as e:
        dis.num_ask(num) 
    assert e.type == SystemExit

@pytest.mark.parametrize(
   "path",
   [ 
      (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std_1"),
      (r"C:\Users\Emily\Desktop\1.Tendencias\Prueba\std5.txt")    
   ]
)

def test_read_file_exit(path):
    with pytest.raises(SystemExit) as e:
        dis.read_file(path) 
    assert e.type == SystemExit

@pytest.mark.parametrize(
   "num, std_list, themes_list",
   [ 
      (5, ["Lenore", "Chanel", "Chet", "Leroi"], ["Summer", "Pillars", "Honourable", "Bottle", "Cloudy"]),
      (13, ["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise", "Ashleigh", "Jaxx", "Cherish", "Teodoro", "Marcus", "Dante"], 
      ["Valuable", "Spring", "Fairies", "Guardian", "Key", "Words", "Angelic"]) 
   ]
)

def test_req_exit(num, std_list, themes_list):
    with pytest.raises(SystemExit) as e:
        dis.req(num, std_list, themes_list) 
    assert e.type == SystemExit