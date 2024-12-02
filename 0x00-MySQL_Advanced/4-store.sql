-- creates a trigger when an item is ordered
CREATE TRIGGER decrease_quantity_item
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
