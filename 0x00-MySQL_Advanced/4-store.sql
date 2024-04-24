CREATE TRIGGER items_order
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = OLD.quantity - NEW.number
WHERE name = item_name;
