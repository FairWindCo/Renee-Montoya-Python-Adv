from actions import AddNewEmployeeAction, AddNewPlantAction, GetEmployeeByIdAction, GetPlantByIdAction, \
    ListAllPlantsAction
from controller import Controller

if __name__ == '__main__':
    controller = Controller(
        AddNewPlantAction(),
        AddNewEmployeeAction(),
        GetPlantByIdAction(),
        GetEmployeeByIdAction(),
        ListAllPlantsAction(),
    )
    controller.run()
