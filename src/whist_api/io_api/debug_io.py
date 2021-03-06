''' Module for handling I/O in debug mode. '''
import logger

def _to_int(curr_str):
    '''Tries to turn a string to int, returns -1 if not possible'''
    try:
        return int(curr_str)
    except ValueError:
        return -1


def get_player_cnt():
    ''' Console prompts for number of players. '''
    return int(input('Enter number of players: '))


def get_names(player_cnt):
    ''' Console prompts for player names. '''
    print('Please enter your names in a circular, clockwise order.')
    names = []
    for i in range(player_cnt):
        curr_name = input('Enter player ' + str(i + 1) + ' name: ')
        while curr_name == '':
            curr_name = input('Enter player ' + str(i + 1) + ' name: ')

        names.append(curr_name)

    return names


def get_bid(name, possible_bids):
    ''' Console prompts for a valid bid. '''
    bid = _to_int(input('Enter ' + name + '\'s bid from ' + str(possible_bids) + ': '))
    while bid not in possible_bids:
        bid = _to_int(input('Invalid bid, again: '))

    return bid


def get_result(name, possible_results):
    ''' Console prompts for a valid bid. '''
    result = _to_int(input('Enter ' + name + '\'s result from ' + str(possible_results) + ': '))
    while result not in possible_results:
        result = _to_int(input('Invalid result, again: '))

    return result


def show_scoreboard(player_names, target_round, scoreboard):
    ''' Prints scoreboard in console. '''
    logger.log_info('\nScoreboard - Round ' + str(target_round + 1))
    logger.log_info(player_names)

    if target_round > 0:
        logger.log_info('Previous: ' + str(scoreboard[target_round - 1]))
    logger.log_info('New: ' + str(scoreboard[target_round]))
