% In the body pf a function narging and nargout indicate the actual number
% of input and output supplied in the call

function [res] = myVector(a, b, c)

    switch nargin
        case 1
            res = [0:a];
        case 2
            res = [a:b];
        case 3
            res = [a:b:c];
        otherwise
            error("Wrong number of params")
    end
end
