const inputs = require('./input');

const valids = []

for (const input of inputs) {
    const [rule, password] = input.split(':');
    const [ruleAmount, ruleLetter] = rule.split(' ');
    const [ruleMin, ruleMax] = ruleAmount.split('-');

    const amountOfChars = (password.match(new RegExp(ruleLetter, 'g')) || []).length;


    const isValid = (ruleMin <= amountOfChars) && (amountOfChars <= ruleMax)
    //console.log(`${password} contains ${amountOfChars} times ${ruleLetter} and isValid: ${isValid}, ${input}`);

    if (isValid) {
        valids.push(password)
    }

}

console.log(`${valids.length}/${inputs.length} valid passwords`);

valids.length = 0

// ---------------- part 2


for (const input of inputs) {
    let [rule, password] = input.split(':');
    const [ruleAmount, ruleLetter] = rule.split(' ');
    const [pos1, pos2] = ruleAmount.split('-');

    password = password.trim()

    const containsOne = (password[pos1 - 1] === ruleLetter) || (password[pos2 - 1] === ruleLetter)
    const containsBoth = (password[pos1 - 1] === ruleLetter) && (password[pos2 - 1] === ruleLetter)

    const isValid = containsOne && !containsBoth

    if (isValid) {
        valids.push(password)
    }
}

console.log(`${valids.length}/${inputs.length} valid passwords`);