
function yu_gi_oh(num) {
    const yu_gi_oh = "yu-gi-oh";
    let processed = [];
    for (let i=1; i<=num; i++) {
        if (i%2==0 && i%3==0 && i%5==0) {
            processed.push(yu_gi_oh);
        } else if (i%2==0 && i%3==0) {
            processed.push(yu_gi_oh.substr(0,5));
        } else if (i%2==0 && i%5==0) {
            processed.push(yu_gi_oh.substr(0,2)+yu_gi_oh.substr(5,3));
        } else if (i%3==0 && i%5==0) {
            processed.push(yu_gi_oh.substr(3,5));
        } else if (i%2==0) {
            processed.push(yu_gi_oh.substr(0,2));
        } else if (i%3==0) {
            processed.push(yu_gi_oh.substr(3,2));
        } else if (i%5==0) {
            processed.push(yu_gi_oh.substr(6,2));
        } else {
            processed.push(i);
        };
    };
    return processed;
};

console.log(yu_gi_oh(100));
console.log(yu_gi_oh(20));
