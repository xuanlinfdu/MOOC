X = [3, 2, 4, 0];
y = [4, 1, 3, 1]';
theta = [0, 1];
X = [ones(1, 4); X];
hx = (theta * X)';
J = 1/8 * sum((hx - y).^2);
fprintf J;


