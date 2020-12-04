const fs = require('fs');

const data = fs.readFileSync('input.txt', 'utf8').split('\n')

const passports = [];
let currPassport = [];

for (const line of data) {
    if (line !== '') {
        currPassport.push(line);
    } else {
        passports.push(currPassport.join(' '));
        currPassport = [];
    }
}


const expectedFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];

const fields = {
    byr: (_) => {
        const x = parseInt(_, 10);
        if (!Number.isInteger(x)) {
            return false;
        }

        return (x >= 1920) && (x <= 2002)
    },
    iyr: (_) => {
        const x = parseInt(_, 10);
        if (!Number.isInteger(x)) {
            return false;
        }

        return (x >= 2010) && (x <= 2020)
    },
    eyr: (_) => {
        const x = parseInt(_, 10);
        if (!Number.isInteger(x)) {
            return false;
        }

        return (x >= 2020) && (x <= 2030)
    },
    hgt: (_) => {
        const unit = _.slice(_.length - 2, _.length);
        const val = parseInt(_.slice(0, _.length - 2), 10);

        if (!Number.isInteger(val)) {
            return false;
        }

        if (unit === 'cm') {
            return (val >= 150) && (val <= 193)
        }


        if (unit === 'in') {
            return (val >= 59) && (val <= 76)
        }

        return false;

    },
    hcl: (_) => {
        return /#[0-9a-f]{6}/g.test(_);
    },
    ecl: (_) => {
        return ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].some(col => _ === col);
    },
    pid: (_) => {
        return /^[0-9]{9}$/gm.test(_);
    },
}

let validPassports = 0;

const isValid = (passport) => {
    const containsRequiresFields = expectedFields.every(_ => passport.includes(_ + ':'));

    const splitProps = passport.split(' ');

    const validates = splitProps.every(prop => {
        const splitProp = prop.split(':')
        const [propName, propValue] = splitProp;
        if (fields[propName]) {
            return fields[propName](propValue);
        } else {
            // No validation available for this field, so all good
            return true
        }
    })


    return containsRequiresFields && validates;

}

for (const passport of passports) {
    if (isValid(passport)) {
        validPassports++
    }
}

console.log(`${validPassports}/${passports.length} passports are valid`);