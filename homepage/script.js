function whenLoaded(){
    document.addEventListener("DOMContentLoaded", () =>{
        for(let i = 0; i < link.length; i++){
            let links = document.querySelectorAll(".link");
            links.addEventListener("hover", () =>{
                links[i].className = "animated fade";
            });
        }
    });
}

whenLoaded();