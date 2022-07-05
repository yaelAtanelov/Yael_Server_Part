
function myFunction() {
 document.querySelector('#myform')?.addEventListener('submit', (e) => {
        e.preventDefault()
    const user_id = e.target.id.value
    console.log(user_id)
    fetch('https://reqres.in/api/users/'+user_id).then(/*good web to play with req & res*/
        response => response.json()/*like pars*/
    ).then(
        responseOBJECT => createUsersList(responseOBJECT.data)
    ).catch(
        err => console.log(err)/*מדפיס את השגיאה בקונסולה*/
    );
})
}


function createUsersList(user) {
        console.log(user.data)

    const currMain=document.querySelector("form")

    const section = document.getElementById('frontend_section')
    section.innerHTML = `
        <br>
            <fieldset>
            <h3>This is ${user.first_name} ${user.last_name}:</h3>
            <img src="${user.avatar}" alt="Profile Picture"/>
            <p>You can always contact us via:</p>
            <a href="mailto:${user.email}">${user.first_name}s Email</a><br><br>
        </fieldset>
    
    `
    currMain.appendChild(section)

}

/*נשים לב שהוא רגיש ל '""' בתוך `` אפשר להכניס מה שאני רוצה*/
