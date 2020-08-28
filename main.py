import Accounts
import config
import TankAccounts
import Clans
import Tankopedia

if __name__ == '__main__':
    # # 1.Accounts
    # a = Accounts.Accounts(config.APP_ID)
    # print(a.get_accounts('HACBAN', game=['wot', 'wotb']))
    # a_id = a.get_account_id('HACBAN_G')
    # print(a.get_account_information(a_id))

    # # 2.TankAccounts
    # ta = TankAccounts.Players(config.APP_ID)
    # print(ta.get_players('HACBAN', fields=['account_id', 'nickname'], language='ko'))
    # ta_id = ta.get_player_id('HACBAN_GEROJ')
    # print(ta.get_personal_data(ta_id, fields="statistics.all.frags statistics.all.stun_number"))
    # print(ta.get_vehicles(ta_id, tank_id=['609', 43841, 1]))
    # print(ta.get_achievements(ta_id))

    # # 3.Tankopedia
    # tp = Tankopedia.Tankopedia(config.APP_ID)
    # print(tp.get_list_vehicles(page_no=4))

    # 4. Clans
    c = Clans.Clans(config.APP_ID)
    print(c.get_clans())
    c_id = c.get_clan_id('YETTI')
    print(c_id)
    print(c.get_details(c_id))
    print

