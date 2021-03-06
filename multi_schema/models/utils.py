from odoo import fields, models, api


def get_rate(self):

    self.env.cr.execute("SELECT max(rate_date), rate "
                        "FROM multi_currency_rate "
                        "WHERE currency_id = %s "
                        "GROUP BY rate_date, rate "
                        "ORDER BY rate_date desc ",
                        [self.operation_currency.id])

    value = self._cr.fetchone()

    if not value:
        return

    return value[1]


def get_schema_rate(self):
    self.env.cr.execute("SELECT max(rate_date), rate "
                        "FROM multi_currency_rate "
                        "WHERE currency_id = %s "
                        "GROUP BY rate_date, rate "
                        "ORDER BY rate_date desc ",
                        [self.currency_id.id])

    value = self._cr.fetchone()

    if not value:
        return

    return value[1]


def get_invoice_rate(self):
    self.env.cr.execute("SELECT max(rate_date), rate "
                        "FROM multi_currency_rate "
                        "WHERE currency_id = %s "
                        "GROUP BY rate_date, rate "
                        "ORDER BY rate_date desc ",
                        [self.currency_from_id.id])

    value = self._cr.fetchone()

    if not value:
        return

    return value[1]




