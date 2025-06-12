import traceback
from utils.logger import log_msg, logging


class TenantDBRouter:

    DEFAULT = "default"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        try:
            model = hints.get("model")
            if model:
                if db == self.DEFAULT:
                    return True

                migrate_to_tenant = getattr(model, "migrate_to_tenant", False)
                if migrate_to_tenant:
                    return False

            return True

        except Exception:
            log_msg(logging.ERROR, traceback.format_exc())
            return False
