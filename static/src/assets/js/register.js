const emailField=document.querySelector("#email");
const usernameField=document.querySelector("#username");
const nomField=document.querySelector("#nom");
const prenomField=document.querySelector("#prenom");
const telephoneField=document.querySelector("#telephone");
const zipField=document.querySelector("#zip");
const villeField=document.querySelector("#ville");
const passwordField=document.querySelector("#password");
const password2Field=document.querySelector("#password2");

nomField.addEventListener("keyup",(e) =>{
    const nomVal=e.target.value;

    if(nomVal.length>0){
        nomField.classList.add("is-valid");
    }else{
        nomField.classList.remove("is-valid");
        nomField.classList.add("is-invalid");
    }

});


passwordField.addEventListener("keyup",(e) =>{
    const passVal=e.target.value;

    if(passVal.length>0){
        passwordField.classList.add("is-valid");
    }else{
        passwordField.classList.remove("is-valid");
        passwordField.classList.add("is-invalid");
    }

});

password2Field.addEventListener("keyup",(e) =>{
    const pass2Val=e.target.value;

    if(pass2Val.length>0){
        password2Field.classList.add("is-valid");
    }else{
        password2Field.classList.remove("is-valid");
        password2Field.classList.add("is-invalid");
    }

});




prenomField.addEventListener("keyup",(e) =>{
    const prenomVal=e.target.value;

    if(prenomVal.length>0){
        prenomField.classList.add("is-valid");
    }else{
        prenomField.classList.remove("is-valid");
        prenomField.classList.add("is-invalid");
    }

}); 

villeField.addEventListener("keyup",(e) =>{
    const villeVal=e.target.value;

    if(villeVal.length>0){
        villeField.classList.add("is-valid");
    }else{
        villeField.classList.remove("is-valid");
        villeField.classList.add("is-invalid");
    }

}); 


zipField.addEventListener("keyup",(e) =>{
    const zipVal=e.target.value;

    if(zipVal.length>0){
        zipField.classList.add("is-valid");
    }else{
        zipField.classList.remove("is-valid");
        zipField.classList.add("is-invalid");
    }

}); 

telephoneField.addEventListener("keyup",(e) =>{
    const telVal=e.target.value;

    if(telVal.length>0){
        telephoneField.classList.add("is-valid");
    }else{
        telephoneField.classList.remove("is-valid");
        telephoneField.classList.add("is-invalid");
    }

}); 




usernameField.addEventListener("keyup",(e) =>{
    const usernameVal=e.target.value;

    if(usernameVal.length>0){
        usernameField.classList.add("is-valid");
    }else{
        usernameField.classList.remove("is-valid");
        usernameField.classList.add("is-invalid");
    }

}); 


emailField.addEventListener("keyup",(e) =>{
    const emailVal=e.target.value;

    if(emailVal.length>0){
        fetch("/accounts/validate_email/",{
            body:JSON.stringify({ email: emailVal}),
            method: "POST"
        }).then(res=>res.json()).then(data=>{
            if(data.email_error){
                emailField.classList.add("is-invalid");
            }else{
                emailField.classList.remove("is-invalid");
                emailField.classList.add("is-valid");
            }
        });
    }
    
});
