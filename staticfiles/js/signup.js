document.getElementById("form-create").addEventListener('submit', function(event){
    event.preventDefault()
    const isValid=formValidate()
   if(isValid){
    alert("You have successfully registered with InfoNest. You can now login")
    window.location.href= "login.html"
   }


})
function formValidate(){
    let isValid=true
    const name=document.getElementById("name")
    if(!name.value.trim(name)){
        name.classList.add('invalid')
        name.nextElementSibling.style.display="block"
        isValid=false
    }
    else{
        name.classList.remove('invalid')
        name.nextElementSibling.style.display="none"
    }
    const email =document.getElementById("email")
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailRegex.test(email.value.trim(email))){
        email.classList.add("invalid")
        email.nextElementSibling.style.display="block"
        isValid=false
    }
    else{
        email.classList.remove('invalid')
        email.nextElementSibling.style.display="none"
    }
    const school=document.getElementById('school')
    if(!school.value.trim()){
        school.classList.add('invalid')
        school.nextElementSibling.style.display="block"
        isValid=false
    }
    else{
        school.classList.remove('invalid')
        school.nextElementSibling.style.display="none"
    }

    const pass=document.getElementById("pass")
    if(!pass.value.trim(pass)){
        pass.classList.add("invalid")
        pass.nextElementSibling.style.display="block"
        isValid=false
    }
    else{
        pass.classList.remove("invalid")
        pass.nextElementSibling.style.display="none"
    }
    return isValid
}
