# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    order_code_ghm = fields.Text('Código da Ordem')
    name_english_ghm = fields.Text('Nome em Inglês')
    name_french_ghm = fields.Text('Nome em Francês')
    name_spanish_ghm = fields.Text('Nome em Espanhol')
    name_portuguese_ghm = fields.Text('Nome em Português')
    typical_delivery_time_ghm = fields.Text('Tempo de Entrega Típico')
    discount_group_ghm = fields.Text('Grupo de Desconto')
    price_structure_group_ghm = fields.Text('Grupo de Estrutura de Preço')
    release_for_processing_ghm = fields.Text('Liberação para Processamento')
    goods_n_ghm = fields.Text('Número do Recebimento')
    gtin_ghm = fields.Text('GTIN')
    max_qty_for_delivery_time = fields.Text('Quantidade Máxima para o Tempo de Entrega')
    last_production_ghm = fields.Text('Última Produção')
    article_category = fields.Text('Categoria do Artigo')
