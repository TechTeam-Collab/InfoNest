document.getElementById('form-container').addEventListener('submit', function(event){
  event.preventDefault()
  const isValid=formValidate()


  })
function formValidate(){
  let isValid=true
  const mail = document.querySelector("#email")
  mailRegex=/^[^\s@]+@[^\s@]+\.[^\s@]+$/
if(!mailRegex.test(mail.value.trim())){
  mail.classList.add("invalid")
  mail.nextElementSibling.style.display="block"
  isValid=false
}
else{
  mail.classList.remove("invalid")
}
const password=document.querySelector("#password")
if(!password.value.trim()){
  password.classList.add("invalid")
  password.nextElementSibling.style.display="block"
  isValid=false
}
else{
  password.classList.remove("invalid")
  password.nextElementSibling.style.display="none"
}

return isValid
}
