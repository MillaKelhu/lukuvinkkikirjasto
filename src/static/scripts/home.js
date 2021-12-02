function setClass() {
    elements = document.getElementsByClassName("link-card")
    console.log(elements)
    let i = 10
    Array.prototype.forEach.call(elements, function(elem){
        console.log(elem)
        console.log("here")
        elem.style["transition-delay"]=`${i*100}ms`
        elem.classList.add("appear-animation")
    })
}
