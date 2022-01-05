import _server
import time
# from dotenv import load_dotenv

if __name__ == '__main__':
    

    log_object = _server.logger('./logs/','hi.log')
    log_object.create_log()
    log_object.log_item(time.time(), 'Created log file')

    print('Hello')
    log_object.log_item(time.time(), 'printed hello there')