import os
def docker():
    while True:
        print("\t\t\tWELCOME TO THE DOCKER WORLD")
        print("""  1: Get Information About Docker
   2: To Check Images Already Present
   3: To Check Container Running
   4: To Download Docker Image from Docker Hub
   5: To Launch a Container (from )
   6: To Check History of Images
   7: To Relaunch Stopped Containers
   8: To Stop a running Container (Container name Needed)
   9: To Remove a Container (Container Id need)
  10: To Remove a Image from System
  11: To Delete All Containers 
   0:to exit from Docker's World""")
        choice =int(input("ENTER THE CHOICE : "))
        if choice == 1:
            os.system("docker info")
        elif choice == 2:
            os.system("docker image ls")
        elif choice == 3:
            os.system("docker container ps")
        elif choice == 4:
            nameOfImage=input("ENTER THE NAME OF IMAGE YOU WANT TO PULL")
            os.system("docker pull {}".format(nameOfImage))
        elif choice == 5:
            nameOfImage=input("Enter the name of Image")
            option = input("Do you want to Nomaenclature of container:yes/No")
            if option =='No':
                A=input("Do you want to launch your image in default network:yes/No")
                if A=='yes':
                    os.system("docker run -it -d {}".format(nameOfImage))
                else:
                    net=input("Enter the name of network[warning :network must be created]")
                    os.system("docker run -it -d --network {0} {1}".format(net,nameOfImage))
            else:
                Name = input("Enter the name of container you want to keep")
                B=input("Do you want to launch your image in default network:yes/No")
                if B=='yes':
                    os.system("docker run -it -d --name {} {}".format(Name,nameOfImage))
                else:
                    net=input("Enter the name of network[warning :network must be created]")
                    os.system("docker run -it -d --name {0} --network {1} {2}".format(Name,net,nameOfImage))
        elif choice ==6:
            os.system("docker container ps -a")
        elif choice ==7:
            ContainerName =input("Enter the name of container")
            os.system("docker start {}".format(ContainerName))
            option =input("Do you want to enter in container :yes/No")
            if option =='yes':
                os.system("docker attach {}".format(ContainerName))
        elif choice ==8:
            nameofContainer= input("Enter the name of container to be stoped")
            os.system("docker container stop {}".format(nameofContainer))

        elif choice ==9:
            IdOfContainer =input("Enter the ID of container to be removed")
            os.system("docker container rm {}".format(IdOfContainer))
        elif choice ==10:
            nameOfImage =input("Enter the Name of Image to be removed")
            os.system("docker image rmi {}".format(nameOfImage))
        elif choice ==11:
            War =input("Warning :: you may lose your important data :yes/No")
            if War =='yes':
                os.system("docker container rm -f $(docker container ls -a -q)")
        elif choice ==0:

            os.system("tput setab 0")
            os.system("tput setaf 7")
            break

#----------------------------------------------------------------------


