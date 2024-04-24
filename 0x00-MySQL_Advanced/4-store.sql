-- creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER items_order
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE item_name = name;
