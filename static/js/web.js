function LoginToogle() {
  let signup = document.getElementById("id-signin");
  let login = document.getElementById("id-login");
  signup.style.display = "none";
  login.style.display = "block";
}
function SigninToogle() {
  let signup = document.getElementById("id-signin");
  let login = document.getElementById("id-login");
  signup.style.display = "block";
  login.style.display = "none";
}
function openOurInitiative() {
  document.getElementById("our-initiative").style.display = "flex";
}
function closeOurInitiative() {
  document.getElementById("our-initiative").style.display = "none";
}

