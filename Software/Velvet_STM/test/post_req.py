from loguru import logger
import requests
import json 

ScalesSerialNumber = "Google"
array = [100.01000213623047, 123.09999847412109, 345.20001220703125, 678.29998779296875]
Weighting_Start = 1000
Weighting_End = 2000
RFID_Number = "101010101010"
size_of_float_array = 4


JSON_STRING ={"ScalesSerialNumber": "velvet_test_max", 
             "WeighingStart": 100,
             "WeighingEnd": 1000,
             "RFIDNumber": "001001001001",
             "Data": [100, 200, 300, 100]}


def post_array_data(type_scales, animal_id, weight_list, weighing_start_time, weighing_end_time):
    try:
        logger.debug(f'Post data function start')
        url = 'https://smart-farm.kz:8502/v2/OneTimeWeighings'
        headers =  {'Content-Type': 'application/json; charset=utf-8'}
        data = {
                "ScalesSerialNumber": type_scales,
                "WeighingStart": weighing_start_time,
                "WeighingEnd": weighing_end_time,
                "RFIDNumber": animal_id,
                "Data": weight_list
                }  
        post = requests.post(url, data=json.dumps(data), headers=headers, timeout=3)
        logger.debug(f'Answer from server: {post}') # Is it possible to stop on this line in the debug?
        logger.debug(f'Content from main server: {post.content}')
    except Exception as e:
        logger.error(f'Error post data: {e}')



def post_2():
    try:
        logger.debug(f'Post data function start')
        url = 'https://smart-farm.kz:8502/v2/OneTimeWeighings'
        headers =  {'Content-Type': 'application/json; charset=utf-8'}
        data =         {
        "ScalesSerialNumber":   "Facebook",
        "WeighingStart":        1000,
        "WeighingEnd":  2000,
        "RFIDNumber":   "101010101010",
        "Data": [100.01000213623047, 123.09999847412109, 345.20001220703125, 678.29998779296875]
} 
        post = requests.post(url, data=json.dumps(data), headers=headers, timeout=3)
        logger.debug(f'Answer from server: {post}') # Is it possible to stop on this line in the debug?
        logger.debug(f'Content from main server: {post.content}')
    except Exception as e:
        logger.error(f'Error post data: {e}')

def main():
    #post_array_data(ScalesSerialNumber, RFID_Number, array, Weighting_Start, Weighting_End)
    post_2()

main()
