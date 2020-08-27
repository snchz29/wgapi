import config
import TankAccounts
import Tankopedia

if __name__ == '__main__':
    p = TankAccounts.Players(config.APP_ID)
    p.get_players('HACBAN_GEROJ')
    p_id = p.get_player_id('HACBAN_GEROJ')
    p.get_personal_data(p_id, extra=['private.boosters'])
