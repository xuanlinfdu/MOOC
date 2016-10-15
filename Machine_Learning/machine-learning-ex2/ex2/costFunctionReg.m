function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
n = length(theta);

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%% calculate the cost
sum = 0;
for num = 1:m
    sum = sum + ((-y(num) * log(sigmoid(theta' * X(num, :)')))-...
        ((1 - y(num)) * log(1 - sigmoid(theta' * X(num, :)'))));
end
J = sum / m;

sum = 0;
for num = 2:n
    sum = sum + theta(num)^2;
end

J = J + (lambda / (2 * m)) * sum;

%% calculate the gradient
for item = 1:n
    if item > 1
        total = 0;
        for j = 1:m
            total = total + ((sigmoid(theta' * X(j, :)') - y(j)) * X(j, item));
        end
        grad(item) = total / m + (lambda * theta(item) / m);
    else
        total = 0;
        for j = 1:m
            total = total + ((sigmoid(theta' * X(j, :)') - y(j)) * X(j, item));
        end
        grad(item) = total / m;
    end
end

% =============================================================

end
