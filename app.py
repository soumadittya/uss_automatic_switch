from flask import Flask
# import RPi.GPIO as GPIO
app = Flask(__name__)


status_relay = {'1' : 0, '2' : 0, '3' : 0, '4' : 0}

@app.route('/switch/<relay>')
def switch(relay):
    if(relay == '1'):
        try:
            if status_relay['1'] == 0:
                status_relay['1'] = 1
                return "on_1"
            elif status_relay['1'] == 1:
                status_relay['1'] = 0;
                return "off_1"
        except:
            print("Cannot on relay_1....")
    elif(relay == '2'):
        try:
            if status_relay['2'] == 0:
                status_relay['2'] = 1
                return "on_2"
            elif status_relay['2'] == 1:
                status_relay['2'] = 0;
                return "off_2"
        except:
            print("Cannot on relay_2....")

    elif(relay == '3'):
        try:
            if status_relay['3'] == 0:
                status_relay['3'] = 1
                return "on_3"
            elif status_relay['3'] == 1:
                status_relay['3'] = 0;
                return "off_3"
        except:
            print("Cannot on relay_3....")
    elif(relay == '4'):
        try:
            if status_relay['4'] == 0:
                status_relay['4'] = 1
                return "on_4"
            elif status_relay['4'] == 1:
                status_relay['4'] = 0;
                return "off_4"
        except:
            print("Cannot on relay_4....")
    else:
        try:
            return 'Specified relay does not exist....'
        except:
            print('Invalid relay selected. Cannot inform the client....')

@app.route('/status')
def status():
    try:
        return status_relay
    except:
        print('Cannot return status to client....')
if __name__ == "__main__":
    app.run(debug = True)
