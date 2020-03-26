let name = "Babatunde Adenowo";
const courses = ['html-css-js', 'php', 'node.js', 'java', 'flutter', 'kotlin', 'go',];

// Printing out my name and courses
console.log(name);
console.log("Courses:");
for (index=0; index < courses.length; index++) { 
    console.log(courses[index]);
} 

const data = []

if (courses.length%2!==0) {
    for (let i=0; i<=200; i++) {
        if (i%2!==0) {
            data.push(i);
        }
    }
} else {
    for (let i=0; i<=200; i++) {
        if (i%2==0) {
            data.push(i);
        }
    }
}

console.log(data);