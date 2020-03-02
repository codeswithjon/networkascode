import os

 from genie.harness.main import gRun

 def main():
     test_path = os.path.dirname(os.path.abspath(__file__))

     gRun(trigger_uids=('TriggerShutNoShutBgp'),
         trigger_datafile='new_trigger_datafile.yaml')
