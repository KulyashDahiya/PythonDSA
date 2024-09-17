import time

def convertMillis(mil):
    seconds = (mil/1000)%60
    return seconds





if __name__ == '__main__' :
    #INPUTS HERE

    start = convertMillis(time.time())

    ## CODE HERE

    end = convertMillis(time.time())
    print("Time Execution: ", (end - start) * 10 ** 3, "seconds")