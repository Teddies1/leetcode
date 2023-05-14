/**
 * @return {Function}
 */
var createHelloWorld = function() {
    const func = () => {
        return "Hello World";
    }
    return func;
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */