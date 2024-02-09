

def graph_user_distribution(processedList):

    '''
    processedList = ['user', 'activity', 'time', 'x', 'y', 'z']
    get max and min about user number, then make user list []
    make user list and count list, then make graph
    '''
    

    from collections import defaultdict

    user_cnt_dict = defaultdict(int)
    user_max = 1
    for  seq in processedList:
        user = int(seq[0])
        user_cnt_dict[user]+=1
        if user > user_max:
            user_max = user

    print(user_cnt_dict)

    import matplotlib.pyplot as plt
    plt.clf()
    plt.bar(user_cnt_dict.keys(), user_cnt_dict.values())

    plt.savefig('graph_user_distribution.png')

def graph_action_distribution(processedList):
    '''
    action :     Walking, Jogging ,Upstairs ,Downstairs ,Sitting, Standing
    '''

    Walking_cnt, Jogging_cnt ,Upstairs_cnt ,Downstairs_cnt ,Sitting_cnt, Standing_cnt = 0, 0, 0, 0, 0, 0

    for  seq in processedList:
        action = seq[1]
        if      action == 'Walking':        Walking_cnt += 1
        elif    action == 'Jogging':        Jogging_cnt += 1
        elif    action == 'Upstairs':       Upstairs_cnt += 1
        elif    action == 'Downstairs':     Downstairs_cnt += 1
        elif    action == 'Sitting':        Sitting_cnt += 1
        elif    action == 'Standing':       Standing_cnt += 1

    action_list = ["Walking", "Jogging" ,"Upstairs" ,"Downstairs" ,"Sitting", "Standing"]
    action_cnt = [Walking_cnt, Jogging_cnt, Upstairs_cnt, Downstairs_cnt, Sitting_cnt, Standing_cnt]

    import matplotlib.pyplot as plt
    plt.clf()
    plt.bar(action_list, action_cnt)

    plt.savefig('graph_action_distribution.png')
