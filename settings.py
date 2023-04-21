from handlers.start import cmd_start
from handlers.wallet import cmd_get_balance, create_wallet, cmd_rmv_wallet, cmd_create_wallet, show_wallet_menu, cmd_get_all_wallets
from handlers.spendings import show_spendings_menu, spendings_go_back


message_handlers = [cmd_start, cmd_get_balance, cmd_rmv_wallet, create_wallet, cmd_create_wallet]

callback_handlers = [show_wallet_menu, cmd_get_all_wallets, show_spendings_menu, spendings_go_back]