let name = "Babatunde";
const courses = ['html-css-js', 'php', 'node.js', 'java', 'flutter', 'kotlin', 'go',];
const data = []

if (courses.length%2!==0){
    for (let i=0; i<=200; i++){
        if (i%2!==0){
            data.push(i);
        }
    }
} else {
    for (let i=0; i<=200; i++){
        if (i%2==0){
            data.push(i);
        }
    }
}

console.log(data);