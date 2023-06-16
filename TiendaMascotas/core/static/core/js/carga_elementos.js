// Navbar
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById('navbar').innerHTML =this.responseText;
    }
}
xhttp.open('GET','navbar.html',true);
xhttp.send();

// Footer
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById('footer').innerHTML =this.responseText;
    }
}
xhttp.open('GET','footer.html',true);
xhttp.send();