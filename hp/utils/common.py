import frappe

def update_item_price(doc, method):
	for d in doc.items:
		if frappe.db.exists('Item Price', {'item_code': d.item_code, 'price_list': doc.selling_price_list}):
			frappe.db.set_value('Item Price', {'item_code': d.item_code, 'price_list': doc.selling_price_list}, 'inward_discount', d.discount_percentage_custom)
			frappe.db.set_value('Item Price', {'item_code': d.item_code, 'price_list': doc.selling_price_list}, 'outward_margin', d.margin_rate_or_amount_custom)