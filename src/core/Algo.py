import logging
import threading
import time

''' This module is for running algo , registering strategies and run threads for each strategy 
    Imported modules are instruments, trademanager  and strategies
                                                                                                '''
from instruments.Instruments import Instruments
from trademgmt.TradeManager import TradeManager

from strategies.SampleStrategy import SampleStrategy # registered strategy
from strategies.BNFORB30Min import BNFORB30Min       # registered strategy

#from Test import Test

class Algo:   #Run Algo
  isAlgoRunning = None

  @staticmethod
  def startAlgo():    
    if Algo.isAlgoRunning == True:    #check if algo running
      logging.info("Algo has already started..") 
      return
    
    logging.info("Starting Algo...")  
    Instruments.fetchInstruments()    #Fetch instruments from Instruments module

    # start trade manager in a separate thread
    tm = threading.Thread(target=TradeManager.run)
    tm.start()

    # sleep for 2 seconds for TradeManager to get initialized
    time.sleep(2)

    # start running strategies: Run each strategy in a separate thread
    threading.Thread(target=SampleStrategy.getInstance().run).start()
    threading.Thread(target=BNFORB30Min.getInstance().run).start()
    
    Algo.isAlgoRunning = True
    logging.info("Algo started.")
