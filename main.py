from instance import Instance
from alns import ALNS
from visualizer import Visualizer
import os
from datetime import datetime

def get_all_instances(filePath):
    txt_files = []
    for file in os.listdir(filePath):
        if file.endswith('.txt') or file.endswith(".TXT"):
            txt_files.append(file)
    return txt_files

def get_timestamped_filename(prefix="results", extension=".md"):
    """
    Generate a time-stampled filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
    return f"{prefix}_{timestamp}{extension}"

if __name__ == "__main__":
    folder = "./benchmark/Gehring&Homberge/"
    instList = get_all_instances(folder)
    category = "Gehring&Homberge"
    
    # test list : C2_6_3.txt (checked)
    folder = "./benchmark/Solomon/"
    instList = get_all_instances(folder)
    category = "Solomon"
    instList.sort()
    # print(instList)
    
    os.makedirs("./Logger", exist_ok=True)
    file_path = os.path.join("./Logger", get_timestamped_filename())
    file_exists = os.path.exists(file_path)
    # print(instList[10:20] + instList[60:70] + instList[110:120] + instList[160:170] + instList[210:220] )

    for inst in instList:
        # 200 customer instances ... 
        fileName = folder + inst
        curInstance = Instance.readInstance(fileName)
        curInstance.updateBKS(category, inst.split(".")[0] ) # Update Best Known Solution ... 
        alns_solver = ALNS(curInstance)
        alns_solver.execute()
        tempResult = alns_solver.returnBrief()
        
        with open(file_path, "a") as file:
            if not file_exists:
                file.write("| Inst   |  Obj     | #.Truck | CPU (s) | Gap to BKS | BKS #. Trucks |\n")
                file.write("| :----: | :------: | :-----: | :-----: | :--------: | :-----------: |\n")
                file_exists = True
            file.write(f"| {inst[:-4]} | {round(tempResult[0],2)} | {tempResult[1]} | {round(tempResult[2],2)} | {round(tempResult[3],2)} | {tempResult[4]} |\n")

        # vrptw_visualizer = Visualizer(curInstance, alns_solver.currentSolution)
        # vrptw_visualizer.show()
        