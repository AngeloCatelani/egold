/**
 * @return {Function}
 */
var createHelloWorld =(args)=>{
   
    return ()=>{
        return "Hello World"
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */