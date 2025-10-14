import random
from copy import deepcopy


#the main function of the game
def generate_horses(horse_quantity : int):
    horse_template = {'horse_n': 1,'speed':0, 'status':'playing','distance': 0}
    horse_list = []

    #function to generate the horse list
    for horse_n in range(1,horse_quantity+1):
        #copy the template
        horse = deepcopy(horse_template)
        #set horse n
        horse['horse_n'] = horse_n
        #set horse on list
        horse_list.append(horse)
    return horse_list

def play(horse_list,output_type):
    #VARS
    simulated_time = 10
    podium = []

    #PLAY THE GAME
    while True:
        #update speed horse
        for horse in horse_list:
            #check if horse finished or is DQ
            if horse['status'] not in ('finished', 'DQ'):
                #apply the new speed
                apply_dice(random.randint(1,6), horse)

            if horse['status'] not in ('finished', 'DQ'):
                match horse['speed']:
                    case 0:
                        pass
                    case 1:
                        horse['distance']+=23
                    case 2:
                        horse['distance']+=46
                    case 3:
                        horse['distance']+=69
                    case 4:
                        horse['distance']+=92
                    case 5:
                        horse['distance']+=115
                    case 6:
                        horse['distance']+=138

                if horse['distance'] >= 2500:
                    horse['status'] = 'finished'
                    podium.append(horse)
                    horse['distance'] = 2500

        #check if all horses have finished or are Disqualified
        if all(horse['status'] in ['finished', 'DQ'] for horse in horse_list):
            #convert the inserted case into a int
            num_output_type = 0
            match output_type.lower():
                case 'tiercé':
                    num_output_type = 3
                case 'quarté':
                    num_output_type = 4
                case 'quinté':
                    num_output_type = 5
            # cut the podium list
            podium = podium[:num_output_type]

            #print podium
            barrier()
            # print a map
            print_map(horse_list)
            barrier()
            print("Le jeu vient de finir")
            for i,h in enumerate(podium):
                print(f"Place {i+1} | Cheval {h['horse_n']} | Vitesse : {h['speed']} | Distance {h['distance']} | Status {h['status']}")
            barrier()
            break
        else:
            #print properly
            barrier()
            for h in horse_list:
                print(f"Cheval {h['horse_n']} | Vitesse : {h['speed']} | Distance {h['distance']} | Status {h['status']}")


            #print the time
            print(f'Le temps actuel de course est de {simulated_time} secondes')
            barrier()
            #print a map
            print_map(horse_list)
            #add12
            simulated_time += 10
            input('Taper sur Enter pour continuer...')

def apply_dice(dice : int, horse : dict):
    """
    Fonction pour appliquer la vitesse correcte d'apres le dé
    :param dice: valeur du dé
    :param horse: cheval à mettre à jour
    :return:
    """
    match dice:
        case 1:
            if horse['speed'] in [3, 4]:
                horse['speed'] -= 1
            elif horse['speed'] in [5, 6]:
                horse['speed'] -= 2
        case 2:
            if horse['speed'] == 0:
                horse['speed'] += 1
            elif horse['speed'] in [5, 6]:
                horse['speed'] -= 1
        case 3:
            if horse['speed'] in [0, 1, 2]:
                horse['speed'] += 1
        case 4:
            if horse['speed'] in [0, 1, 2,3]:
                horse['speed'] += 1
        case 5:
            if horse['speed'] == 0:
                horse['speed'] += 2
            elif horse['speed'] in [1, 2, 3, 4]:
                horse['speed'] += 1
        case 6:
            if horse['speed'] in [0, 1, 2]:
                horse['speed'] += 2
            elif horse['speed'] in [3, 4, 5]:
                horse['speed'] += 1
            elif horse['speed'] == 6:
                horse['status'] = 'DQ'


def barrier():
    print('-' * 30)


def print_map(horse_list : dict):
    for h in horse_list:
        # TESTS
        progress = h['distance'] // 30
        progress_bar = '▓' * progress + '░' * (2500 // 30 - progress)
        if h['status'] == 'playing':
            print(f'{h['horse_n']} : {progress_bar}')
        elif h['status'] == 'DQ':
            print(f"\033[91m{h['horse_n']} : {progress_bar}\033[0m")
        elif h['status'] == 'finished':
            print(f"\033[92m{h['horse_n']} : {progress_bar}\033[0m")







def main():
    """
    La fonction principale pour le jeu
    """
    # inputs
    horse_quantity = input("Inserer la quantité de chevaux qui vont jouer (12-20) : ")
    output_type = input("Inserer le type de sortie desiré (tiercé, quarté, quinté) : ").lower()

    if output_type in ['tiercé', 'quarté', 'quinté']:
        #check if horse_quantity is a number
        if horse_quantity.isdigit():
            #convert to int
            horse_quantity = int(horse_quantity)

            #check if between 12 and 20
            if 12<=horse_quantity<=20:
                #generate the horse list
                horse_list = generate_horses(horse_quantity)

                #play with the horse list
                play(horse_list,output_type)

            else:
                print('Inserer une quantité entre 12 et 20')
        else:
            print("Inserer un numero entre 12 and 20")
    else:
        print('Inserer un type de sortie correct (tiercé, quarté, quinté)')






if __name__ == '__main__':
    main()