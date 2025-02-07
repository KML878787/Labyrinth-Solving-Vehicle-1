from time import sleep
from Logger.Logger import Logger
from Motor import Motor

class Vehicle:

    def __init__(self, motorR, motorL) -> None:
        self.sensores: list = []
        self.motorR: Motor = Motor(motorR)
        self.motorL : Motor = Motor(motorL)
    
    def turn90Left(self) -> None:
        # todo
        try:
            self.motorR = 2
            self.motorL = 1
            sleep(1)
            self.stop()
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)

    def turn90Right(self) -> None:
        # todo
        try:
            self.motorR = 1
            self.motorL = 2
            sleep(1)
            self.stop()
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)

    def driveForwards(self) -> None:
        try:
            self.motorL.setPower(3)
            self.motorR.setPower(3)
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)
    
    def stop(self) -> None:
        self.motorL.setPower(0)
        self.motorR.setPower(0)
    
    def getAllSensorData(self) -> dict: 
        # todo
        try:
            output: dict = {}
            for index in range(self.sensores):
                output[index] = self.sensores[index].getData()
            return output
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)
    
    def getSensorDataByID(self, id: int) -> dict:
       # todo
        try:
            return self.sensores[id].getData()
        except Exception as err:
            logger = Logger(None)
            logger.log_err(err)
