-- Create an index idx_name_first on the first letter of the name
CREATE INDEX idx_name_first ON names (name(1));

