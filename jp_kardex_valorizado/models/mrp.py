# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def picking_mrp(self):
        
        tipo_salida = self.env['type.operation.kardex'].search([
            ('code','=','19')
        ])
        salida = self.env['stock.picking'].create({
            'picking_type_id':self.picking_type_id[0].id,
            'location_id': self.move_raw_ids[0].location_id.id,
            'location_dest_id': self.move_raw_ids[0].location_dest_id.id
        })
        salida.type_operation_sunat_id =  tipo_salida[0].id 
        
        for t in self.move_raw_ids:
            t.picking_id = salida.id

            for p in t.move_line_ids:
                p.picking_id = salida.id

        entrada =  self.env['stock.picking'].create({
            'picking_type_id':self.picking_type_id.id,
            'location_id': self.move_finished_ids[0].location_id.id,
            'location_dest_id': self.move_finished_ids[0].location_dest_id.id
        })
        tipo_entrada = self.env['type.operation.kardex'].search([
            ('code','=','10')
        ])
        entrada.type_operation_sunat_id =  tipo_entrada[0].id 

        for k in self.move_finished_ids:
            k.picking_id = entrada.id
            for p in k.move_line_ids:
                p.picking_id = salida.id
            
        
        print(entrada.id)
        print(salida.id)
    #587 , 589, 588