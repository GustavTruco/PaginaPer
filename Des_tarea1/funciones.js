function agrandar(el){
    var modal= document.getElementById("myModal");
    var modalImg = document.getElementById("img01");
    modal.style.display = "block";
    modalImg.src = el.src;
}

function achicar(){
    var modal= document.getElementById("myModal");
    modal.style.display = "none";
}

function masMascota(){
    var original= document.getElementById("infomascota");
    var duplicado= original.cloneNode(true);
    duplicado.id="";
    original.parentNode.appendChild(duplicado);
}