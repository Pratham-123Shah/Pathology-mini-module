CREATE TABLE pathology_test (

id INT AUTO_INCREMENT PRIMARY KEY,

test_name VARCHAR(100),

test_code VARCHAR(20) UNIQUE,

sample_type VARCHAR(50),

normal_range VARCHAR(100),

price DECIMAL(10,2),

is_active BOOLEAN DEFAULT TRUE

);


CREATE TABLE lab_test_order (

id INT AUTO_INCREMENT PRIMARY KEY,

order_id VARCHAR(20) UNIQUE,

patient_name VARCHAR(100),

patient_phone VARCHAR(15),

pathology_test_id INT,

order_date DATE,

status ENUM(
'Draft',
'Ordered',
'Completed',
'Cancelled'
) DEFAULT 'Draft',

FOREIGN KEY(pathology_test_id)
REFERENCES pathology_test(id)

);


CREATE TABLE lab_test_result (

id INT AUTO_INCREMENT PRIMARY KEY,

test_order_id INT,

result_value VARCHAR(100),

technician_notes TEXT,

status ENUM(
'Draft',
'Completed'
) DEFAULT 'Draft',

FOREIGN KEY(test_order_id)
REFERENCES lab_test_order(id)

);