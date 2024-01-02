from notification import *
from file_saver import *

def main():
  time = float(input('Loop interval (In hours):'))
  rep = int(input('Repetitions:'))
  openurl = input('Open Browser (True/False):')
  url = build_url()
  search_loop_demo(time, rep, openurl)
  get_info(url)
  parse_temp()
  
  return

main()
