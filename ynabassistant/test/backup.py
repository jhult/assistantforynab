import ynabassistant as ya
import copy

ya.utils.backup.save(1)
ya.utils.backup.save(2)
assert ya.utils.backup.load(int) == [1, 2]

ts = [t for t in ya.ynab.api_client.get_all_transactions() if t.account_name == 'Test Data']
ya.utils.backup.save(ts)
ts_loaded = ya.utils.backup.load(type(ts[0]))
assert ts == ts_loaded
assert str(ts) == str(ts_loaded)
moved = copy.deepcopy(ts)
for t in moved:
    t.account_name = ya.settings.account_name
ya.ynab.queue_update(moved)
ya.ynab.update()

ts_moved = [t for t in ya.ynab.api_client.get_all_transactions() if t.account_name == ya.settings.account_name]
ya.utils.log_info(*moved)
ya.utils.log_info(*ts_moved)
