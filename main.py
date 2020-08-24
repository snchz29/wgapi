import config
import TankAccounts

if __name__ == '__main__':
    player = TankAccounts.Players(config.APP_ID, config.ACCESS_TOKEN)
    print(player.get_players("HACBAN_GEROJ", fields=['account_id']))
    player_id = player.get_player_id('HACBAN_GEROJ')
    print(player.get_personal_data(player_id, ['private.boosters', 'private.garage'],
                                   ['private.boosters', 'private.garage']))
    print(player.get_vehicles(player_id))
