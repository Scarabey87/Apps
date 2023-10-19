


// ReactDOM.render(<div>
//    <h3>Welcome</h3>
//    <h3>to Terminal</h3>
// </div>, document.getElementById("app"))

// ReactDOM.render(React.createElement('input',{
//     placeholder:'Enter name',
//     onClick: ()=> console.log('Terminal'),
//     onMouseEnter: ()=> console.log('Mouse')
// }), document.getElementById("app"))

// const inputClick = ()=> console.log('Clicked')
// const elements1 = <input placeholder = 'Name' onClick = {inputClick}/>
// const app = document.getElementById("app")

// ReactDOM.render(elements1, app)



const user = {
    id : 5,
    age: 33,
    firstName: 'Tom',
    lastName: 'Smit',
    getFullName: function(){ 
        return `${this.firstName} ${this.lastName}`;
    }
};
const user2 = {
    id : 52,
    age: 12,
    firstName: 'asd',
    lastName: 'Smit',
    getFullName: function(){ 
        return `${this.firstName} ${this.lastName}`;
    }
};
ReactDOM    
    .createRoot(document.getElementById("app"))
    .render(
        <div id={user.id}>
            <p>Полное имя: {user.getFullName()}</p>
            <p>Возраст: {user.age}</p>
            <p>Время генерации данных: {new Date().toLocaleTimeString()}</p>
        </div>
    );
let g = ''
    ReactDOM    
    .createRoot(document.getElementById("app2"))
    .render(<input
        type = 'input'
        placeholder='Name'

    />
    );
    ReactDOM    
    .createRoot(document.getElementById("app3"))
    .render(<p>asd</p>
    );