from app.entities.main_menu.handlers import *
#from app.handlers.wallet import cmd_get_balance, create_wallet, cmd_rmv_wallet, cmd_create_wallet, show_wallet_menu, cmd_get_all_wallets
#from app.handlers.spendings import show_spendings_menu, spendings_go_back
from app.entities.wallet.handlers import *

message_handlers = [process_start, process_first_wallet]

callback_handlers = [show_wallet_menu, wallet_go_back, wallet_create, get_all_wallets_names,
                     process_single_wallet_choose, process_delete_wallet]