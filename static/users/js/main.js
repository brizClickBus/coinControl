

function strongPassword(){
    const buttonNext  = document.getElementById('nextbutton')

    
    var card = document.getElementById("card_body")
    var ok = "password1"
    var nok = "password0"
    var forca = 0;
    var password = document.getElementById("password1").value
    console.log(password)
    if(password.length >= 8){
		changeClassPasword(nok,ok,"maior8")
        forca += 20;
	}else{
        changeClassPasword(ok,nok,"maior8")
    }

    if(password.match(/[a-z]+/)){
		changeClassPasword(nok,ok,"letra")
        forca += 20
	}else{
        changeClassPasword(ok,nok,"letra")
    }

	if(password.match(/[A-Z]+/)){
		changeClassPasword(nok,ok,"letraMaiu")
        forca += 20;
	}else{
        changeClassPasword(ok,nok,"letraMaiu")
    }

	if(password.match(/[!@#$%ˆ&*;*({}),<>?:'"]/)){
		changeClassPasword(nok,ok,"caractere")
        forca += 20;
	}else{
        changeClassPasword(ok,nok,"caractere")
    }

    if(password.match(/[1-9]+/)){
		changeClassPasword(nok,ok,"numero")
        forca += 20;
	}else{
        changeClassPasword(ok,nok,"numero")
    }

    progress(forca)

}


function checkPassword(){
    
}


function clickPss(){
    document.getElementById("about_password").style.display = 'block';
    document.getElementById("about_password").style.opacity = 1;

}


function clickOffPss(){
    var display = document.getElementById("about_password").style.display;
    if(display == "none"){
        document.getElementById("about_password").style.display = 'none';
    }else{
        document.getElementById("about_password").style.display = 'none';
    }
}


function changeClassPasword (oldClass,newClass,id){
    document.getElementById(id).classList.remove(oldClass);
    document.getElementById(id).classList.add(newClass);
}

function progress(forca){
	/*Imprimir a força da senha*/
	/*document.getElementById("impForcaSenha").innerHTML = "Força: " + forca;*/

	if(forca <1 ){
		document.getElementById("progressBar").innerHTML = '<div class="progress"><div class="progress-bar bg-success" role="progressbar" style="width: 0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div></div>';
	}else if((forca > 1) && (forca < 21)){
		document.getElementById("progressBar").innerHTML = '<div class="progress"><div class="progress-bar bg-success" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div></div>';
	}else if((forca > 20) && (forca < 41)){
		document.getElementById("progressBar").innerHTML = '<div class="progress"><div class="progress-bar bg-success" role="progressbar" style="width: 40%" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div></div>';
	}else if((forca > 40) && (forca < 61)){
		document.getElementById("progressBar").innerHTML = '<div class="progress"><div class="progress-bar bg-success" role="progressbar" style="width: 60%" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div></div>';
	}else if((forca > 60) && (forca < 81)){
		document.getElementById("progressBar").innerHTML = '<div class="progress"><div class="progress-bar bg-success" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div></div>';
    }else if((forca > 80) && (forca < 101)){
		document.getElementById("progressBar").innerHTML = '<div class="progress"><div class="progress-bar bg-success" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div></div>';
    }
}