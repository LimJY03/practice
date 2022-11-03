var userOne = {
    email: 'ryu@ninja.com',
    name: 'Ryu',
    login() {
        console.log(this.email, 'has logged in')
    },
    logout() {
        console.log(this.email, 'has logged out')
    }
}

var userTwo = {
    email: 'ryu@ninja.com',
    name: 'Ryu',
    login() {
        console.log(this.email, 'has logged in')
    },
    logout() {
        console.log(this.email, 'has logged out')
    }
}

var userThree = {
    email: 'ryu@ninja.com',
    name: 'Ryu',
    login() {
        console.log(this.email, 'has logged in')
    },
    logout() {
        console.log(this.email, 'has logged out')
    }
}

userOne.name = 'Yoshi'
console.log(userOne.name);

class User {
    constructor(email, name) {
        this.email = email
        this.name = name
        this.score = 0
    }
    login() {
        console.log(this.email, 'has logged in at' , new Date())
        return this
    }
    logout() {
        console.log(this.email, 'has logged out', new Date())
        return this
    }
    updateScore() {
        this.score++;
        console.log(this.email, 'score is now', this.score);
        return this;
    }
}


class Admin extends User{
    deleteUser(user) {
        users = users.filter(u => {
            return u.email != user.email
        })
    }
}
userOne = new User('whleexd@gmail.com', 'Wh')
userTwo = new User('nick@grannys.com', 'Nick')
var admin = new Admin('jack@valorant.com', 'jack')
var users = [userOne, userTwo, admin]
admin.deleteUser(userOne)
admin.login()
console.log(users)