import os
import random
from scipy.misc import imread
import requests
def open_waste_slot():

    """
        open the machine so that
        an user can enter the machine

    :return:
    """

    send_command_to_machine("open_waste_slot")
    return True


def close_waste_slot():
    """
    close the waste box for user safety
    :return:
    """

    send_command_to_machine("close_waste_slot")
    return True


def process_waste(waste_type):

    """
    move the good slot and shredd the waste
    :return:
    """

    move_container(waste_type)
    was_sucessful = shred_waste()

    return was_sucessful


def move_container(waste_type):

    BOTTLE_BOX = 0
    GLASS_BOX = 1
    command_name = "move_container"

    if waste_type == "bottle":
        send_command_to_machine(command_name, BOTTLE_BOX)
    elif waste_type == "glass":
        send_command_to_machine(command_name, GLASS_BOX)

    return True


def send_command_to_machine(command_name, value=None):

    """
    simulate command sending to rasberry pi
    do nothing to work even if the machine is not connected

    :param command_name:
    :param value:
    :return:
    """
    return True



def shred_waste():

    send_command_to_machine("shred_waste")

    return True


def take_trash_picture():

    """
        function simulating the picture taking
        inside the machine. 

        Call this function to ask the machine to 
        take picutre of the trash

        return : np array of the picture
    """

    send_command_to_machine("take_picture")

    paths = os.listdir('camera')
    path = random.choice(paths)

    return imread(os.path.join("./camera", path))

# def make_classification():
#     paths = os.listdir('camera')
#     path = random.choice(paths)
#     prefix = 'C:\\Users\\bezl\\Desktop\\cours juillet\\app_flask\\triof\\camera\\'
#     url = 'https://flask-app-triof.cognitiveservices.azure.com/customvision/v3.0/Prediction/c128869d-0d91-4b70-addf-e88d892a9d47/classify/iterations/Iteration1/image'
#     headers = {'content-type' :'application/octet-stream', 'Prediction-Key': '7a7f46f7232e42528eae0b6fb21781d6'}
#     r = requests.post(url, data = open(prefix + path, "rb"), headers = headers)
#     json = r.json
#     return json()

def make_classification(): 
    camera_dir = '/camera/'
    paths = os.getcwd()+camera_dir
    path = random.choice(os.listdir(paths))
    picture = os.path.join(paths, path)
    url = 'https://flask-app-triof.cognitiveservices.azure.com/customvision/v3.0/Prediction/c128869d-0d91-4b70-addf-e88d892a9d47/classify/iterations/Iteration1/image'
    headers = {'content-type' :'application/octet-stream', 'Prediction-Key': '7a7f46f7232e42528eae0b6fb21781d6'}
    r = requests.post(url, data = open(picture, "rb"), headers = headers)
    json = r.json
    return json()