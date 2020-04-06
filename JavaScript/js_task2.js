let data = [
    {principal:2500, time:1.8},
    {principal:1000, time:5},
    {principal:3000, time:1},
    {principal:2000, time:3},
];

function interestCalculator(arrayIn) {
    const arrayOut = []
    for (let objIn of arrayIn) {
        if (objIn.principal>=2500 && 1<objIn.time<3) {
            var rateOut = 3;
        } else if (objIn.principal>=2500 && 1<objIn.time<3) {
            var rateOut = 4;
        } else if (objIn.principal>=2500 && 1<objIn.time<3) {
            var rateOut = 2;
        } else {
            var rateOut = 1;
        } let interestOut = objIn.principal*rateOut*objIn.time/100;
        
        let objOut = {
            principal:objIn.principal,
            rate:rateOut,
            time:objIn.time,
            interest:interestOut,
        }; 
        arrayOut.push(objOut);
    }; console.log(arrayOut);
    return arrayOut;
}

interestCalculator(data)
